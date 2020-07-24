from PyMajsoul import msjrpc
import asyncio
import PyMajsoul.majsoul_pb2 as pb
import hmac
import hashlib
import getpass
import uuid 

class testService(msjrpc.MSJRpcService):
    def get_package_name(self):
        return "lq"

    def get_service_name(self):
        return "Lobby"
    
    def get_req_class(self, method):
        if method == 'login':
            return pb.ReqLogin
        return None

    def get_res_class(self, method):
        if method == 'login':
            return pb.ResLogin
        return None

async def main():
    channel = msjrpc.MSJRpcChannel("wss://gateway-v2.maj-soul.com:6443/")
    lobby = testService(channel)
    await channel.connect()
    req = pb.ReqLogin()
    req.account = input("Username:").encode()
    pwd = getpass.getpass()
    req.password = hmac.new(b'lailai', pwd.encode(), hashlib.sha256).hexdigest()
    req.device.device_type = 'pc'
    req.device.browser = 'safari'
    req.random_key = str(uuid.uuid1())
    req.client_version = 'v0.8.64.w'
    req.gen_access_token = True
    req.currency_platforms.append(2)
    res = await lobby.call_method('login', req)
    print(res)
    await channel.close()

asyncio.run(main())
