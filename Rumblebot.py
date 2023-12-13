import httpx
import random
import string
import asyncio

async def start_viewbotting(session, channel_id, num_viewers):
    try:
        url = f"https://wn0.rumble.com/service.php?video_id={channel_id}&name=video.watching-now"
        response = await session.get(url)
        if "data" not in response.json():
            print("Channel doesn't exist.")
            return

        url = "https://wn0.rumble.com/service.php?name=video.watching-now"
        tasks = []
        for _ in range(num_viewers):
            viewer_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
            data = {"video_id": channel_id, "viewer_id": viewer_id}
            task = session.post(url, data=data)
            tasks.append(task)

        await asyncio.gather(*tasks)
        print("Viewers sent.")
    except Exception as e:
        print(f"Error: {str(e)}")

async def main():
    channel_id = input("Enter Video ID: ")
    num_viewers = input("Enter Number of Bots: ")

    if not channel_id or not num_viewers:
        print("Please enter both fields.")
        return

    num_viewers = int(num_viewers)
    session = httpx.AsyncClient()
    await start_viewbotting(session, channel_id, num_viewers)
    await session.aclose()

if __name__ == "__main__":
    asyncio.run(main())
