import asyncio
import PyMajsoul.majsoul_pb2 as pb
from PyMajsoul.majsoul_msjrpc import Lobby
from PyMajsoul.msjrpc import MSJRpcChannel
import hmac
import hashlib
import getpass
import uuid 

async def main():
    channel = MSJRpcChannel("wss://mj-srv-7.majsoul.com:4131/")
    lobby = Lobby(channel)
    await channel.connect()
    req = pb.ReqLogin()
    req.account = input("Username:").encode()
    pwd = getpass.getpass()
    req.password = hmac.new(b'lailai', pwd.encode(), hashlib.sha256).hexdigest()
    req.device.device_type = 'pc'
    req.device.browser = 'safari'
    req.random_key = str(uuid.uuid1())
    req.client_version = 'v0.5.43.w'
    req.gen_access_token = True
    req.currency_platforms.append(2)
    res = await lobby.login(req)
    print(res)
    await channel.close()

asyncio.run(main())
