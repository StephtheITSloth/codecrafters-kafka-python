import socket  # noqa: F401
import asyncio

class KafkaServer:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.server = None

    async def start_server(self):
        self.server = await asyncio.start_server(self.handle_request, self.host, self.port)
        async with self.server:
            await self.server.serve_forever()

    async def handle_request(self, writer, reader):
        pass

async def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = KafkaServer("localhost", 9092)
    await server.start_server() # wait for client


if __name__ == "__main__":
    asyncio.run(main())
