import asyncio
import websockets
 
async def test():
    async with websockets.connect("ws://localhost:1234") as websocket:
        await websocket.send("1 rasbery")
        response = await websocket.recv()
        print(response)
 
asyncio.get_event_loop().run_until_complete(test())
asyncio.get_event_loop().run_forever()