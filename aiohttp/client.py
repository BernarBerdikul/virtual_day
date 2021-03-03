import aiohttp
import asyncio
import ujson


async def main():
    timeout = aiohttp.ClientTimeout(total=600)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        url = 'http://127.0.0.1:8000/users/user/get_profile/'
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2LCJ1c2VybmFtZSI6IkJlcm5hcjMiLCJleHAiOjE2MTMyNTMwNzcsImVtYWlsIjoiYmVybmFyLmJlcmRpa3VsQG1haWwucnUiLCJsb2dpbiI6IkJlcm5hcjMifQ.FKkbNTmnMvY-nItD4ct8FGWJ4YOwqtIzQLXp_JOR7_E"
        headers = {'content-type': 'image/gif',
                   "Authorization": f"JWT {token}"}
        async with session.ws_connect('http://example.org/ws') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    if msg.data == 'close cmd':
                        await ws.close()
                        break
                    else:
                        await ws.send_str(msg.data + '/answer')
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
