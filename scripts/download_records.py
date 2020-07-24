#!/usr/bin/env python3
try:
    import script_env
except ImportError:
    pass
import asyncio
import PyMajsoul.majsoul_pb2 as pb
from PyMajsoul.majsoul_msjrpc import Lobby
from PyMajsoul.msjrpc import MSJRpcChannel
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict
import hmac
import hashlib
import getpass
import uuid 
import aiohttp
import random
import json
import os
import sys
import base64

if sys.argv[1] == "decode":
    basedir = sys.argv[2]
    decode_only = True
else:
    basedir = sys.argv[1]
    decode_only = False

async def manual_login(lobby, config):
    print("Manual Logging in")
    req = pb.ReqLogin()
    req.account = input("Username:").encode()
    pwd = getpass.getpass()
    req.password = hmac.new(b'lailai', pwd.encode(), hashlib.sha256).hexdigest()
    req.device.device_type = 'pc'
    req.device.browser = 'safari'
    uuid_key = str(uuid.uuid1())
    req.random_key = uuid_key
    req.client_version = lobby.version
    req.gen_access_token = True
    req.currency_platforms.append(2)
    res = await lobby.login(req)
    token = res.access_token
    res.access_token = "MASKED FOR PRINTING"
    print("Login Result:")
    print(res)
    print("Saving access token to config")
    config["random_key"] = uuid_key
    config["access_token"] = token

async def relogin(lobby, config):
    print(config)
    print("Checking access token and random key")
    if not "access_token" in config:
        print("Token not present, re-login")
        return False
    if not "random_key" in config:
        print("Random key not recorded, re-login")
        return False
    req = pb.ReqOauth2Check()
    req.access_token = config["access_token"]
    res = await lobby.oauth2Check(req)
    if not res.has_account:
        print("Invalid access token")
        return False
    print("Automatic logging in")
    req = pb.ReqOauth2Login()
    req.access_token = config["access_token"]
    req.device.device_type = 'pc'
    req.device.browser = 'safari'
    req.random_key = config["random_key"]
    req.client_version = lobby.version
    req.currency_platforms.append(2)
    res = await lobby.oauth2Login(req)
    res.access_token = "MASKED FOR PRINTING"
    print("Login Result:")
    print(res)
    return True

async def main():
    if os.path.exists(".majsoul"):
        print("Loading config")
        with open(".majsoul") as f:
            config = json.load(f)
    else:
        print("New config")
        config = {}

    async with aiohttp.ClientSession() as session:
        if not "version" in config:
            print("Querying version")
            async with session.get("https://game.maj-soul.com/1/version.json") as res:
                version = await res.json()
            version = version["version"]
            config["version"] = version
            print("Got version {}".format(version))
        else:
            version = config["version"]
            print("Use stored version {}".format(version))

        if "endpoint" in config:
            endpoint = config["endpoint"]
            print("Use last used endpoint {}".format(endpoint))
            channel = MSJRpcChannel(endpoint)
            try:
                await channel.connect()
            except Exception:
                print("Endpoint not avaliable")
                del endpoint
                del config["endpoint"]

        if not "endpoint" in config:
            print("Choosing an endpoint")
            async with session.get("https://game.maj-soul.com/1/v{}/config.json".format(version)) as res:
                client_config = await res.json()
            urls = client_config["ip"][0]["region_urls"]
            random.shuffle(urls)
            endpoint_found = False
            for url in urls:
                async with session.get(url + "?service=ws-gateway&protocol=ws&ssl=true") as res:
                    servers = await res.json()
                servers = servers["servers"]
                random.shuffle(servers)
                for server in servers:
                    endpoint = "wss://{}/gateway".format(server)
                    print("Chosen endpoint: {}".format(endpoint))
                    channel = MSJRpcChannel(endpoint)

                    try:
                        await channel.connect()
                        endpoint_found = True
                        config["endpoint"] = endpoint
                        break
                    except Exception:
                        print("Endpoint not avaliable")
                if endpoint_found:
                    break
            if not endpoint_found:
                raise Exception("No avaliable endpoint")
            

    print("Connection established with endpoint {}".format(endpoint))

    lobby = Lobby(channel)
    lobby.version = version

    result = await relogin(lobby, config)
    if not result:
        await manual_login(lobby, config)
    
    print("Login successful, saving config")
    with open(".majsoul", "w") as f:
        json.dump(config, f)

    print("Fetching record list")
    records = []
    current = 1
    step = 30
    while True:
        req = pb.ReqGameRecordList()
        req.start = current
        req.count = step
        print("Fetching {} record ids from {}".format(step, current))
        res = await lobby.fetchGameRecordList(req)
        records.extend([r.uuid for r in res.record_list])
        if len(res.record_list) < step:
            break
        current += step
    print("Found {} records".format(len(records)))

    total = len(records)
    for i, r in enumerate(records):
        path = os.path.join(basedir, r)
        if os.path.exists(path):
            print("({}/{})Skipping existing {}".format(i + 1, total, i))
            continue

        req = pb.ReqGameRecord()
        req.game_uuid = r 
        print("({}/{})Fetching {}".format(i + 1, total, r))
        res = await lobby.fetchGameRecord(req)
        with open(path, "w") as f:
            print("({}/{})Saving {}".format(i + 1, total, r))
            f.write(MessageToJson(res))

    await channel.close()
    print("Connection closed")
    await decode_records(records)


async def decode_records(records):
    total = len(records)
    print("Fetching details")
    async with aiohttp.ClientSession() as session:
        for i, r in enumerate(records):
            print("({}/{})Processing {}".format(i + 1, total, r))
            path = os.path.join(basedir, r)
            with open(path) as f:
                data = json.load(f)
            if "data" in data:
                print("({}/{})Data present in {}, skipping".format(i + 1, total, r))
                continue
            if "dataUrl" in data:
                url = data["dataUrl"]
                print("({}/{})Fetching details for {}".format(i + 1, total, r))
                async with session.get(url) as res:
                    details = await res.read()
                print("({}/{})Fetched details  for {}".format(i + 1, total, r))
                data["data"] = base64.b64encode(details).decode()
                with open(path, "w") as f:
                    print("({}/{})Saving {}".format(i + 1, total, r))
                    json.dump(data, f, indent=2, ensure_ascii=False)
                continue
            print("({}/{})Neither data or dataUrl in {}, skipping".format(i + 1, total, r))

    print("Decoding details")

    for i, r in enumerate(records):
        print("({}/{})Processing {}".format(i + 1, total, r))
        path = os.path.join(basedir, r)
        with open(path) as f:
            data = json.load(f)
        if "details" in data:
            print("({}/{})Details present in {}, skipping".format(i + 1, total, r))
            continue
        blob = base64.b64decode(data['data'])

        wrapper = pb.Wrapper()
        wrapper.ParseFromString(blob)
        assert wrapper.name == '.lq.GameDetailRecords'
        records_data = wrapper.data

        records = pb.GameDetailRecords()
        records.ParseFromString(records_data)
        records = records.records

        results = []
        for record in records:
            wrapper = pb.Wrapper()
            wrapper.ParseFromString(record)
            name = wrapper.name.replace(".lq.", "")
            cls = getattr(pb, name)
            obj = cls()
            obj.ParseFromString(wrapper.data)
            result = MessageToDict(obj)
            result['@type'] = name
            results.append(result)
        data["details"] = results

        with open(path, "w") as f:
            print("({}/{})Saving {}".format(i + 1, total, r))
            json.dump(data, f, indent=2, ensure_ascii=False)





if decode_only:
    asyncio.run(decode_records(os.listdir(basedir)))
else:
    asyncio.run(main())
