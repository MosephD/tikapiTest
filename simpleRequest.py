from tiktokapipy.async_api import AsyncTikTokAPI
import asyncio

# Function to get user information by unique_id


async def get_user_info(unique_id):
    async with AsyncTikTokAPI() as api:
        user = await api.user(unique_id)
        return user

# Function to iterate over challenge videos and print user signature and nickname


async def iterate_challenge_and_print_user_info(tag_name):
    async with AsyncTikTokAPI() as api:
        challenge = await api.challenge(tag_name)
        async for video in challenge.videos:
            num_views = video.stats.play_count
            print(f'Video: {video.id}, Views: {num_views}')

            # Get user info using the unique_id
            user = await get_user_info(video.author.unique_id)
            print(
                f'  Nickname: {user.nickname}, User Signature: {user.signature}')

# Create an event loop and run the asynchronous code


async def main():
    await iterate_challenge_and_print_user_info('excel')

if __name__ == '__main__':
    asyncio.run(main())
