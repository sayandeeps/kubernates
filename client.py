import httpx
import asyncio
import time
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


# Define the servers
servers = [
    {"name": "Server 1", "url": "http://127.0.0.1:61512/hi"},
    {"name": "Server 2", "url": "http://127.0.0.1:61824/hi"}
]

# Define the timeout period (in seconds)
timeout = 3

# Define the client
async def client():
    async with httpx.AsyncClient(http2=True) as client:
        server_index = 0
        while True:
            server = servers[server_index]
            try:
                response = await client.post(server["url"], content="hi", timeout=timeout)
                logging.info(f"Received response from {server['name']} which is {server['url']}: {response.text}")
            except httpx.RequestError as e:
                logging.error(f"Error sending request to {server['name']}: {e}")
                logging.warning(f"{server['name']} which is {server['url']} is down, skipping to next server")


            except asyncio.TimeoutError:
                logging.warning(f"Timeout error while sending request to {server['name']}, skipping to next server")
            server_index = (server_index + 1) % len(servers)  # round-robin
            await asyncio.sleep(1)  # wait for 1 second before sending the next request

# Run the client
asyncio.run(client())