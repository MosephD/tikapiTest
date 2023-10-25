from tiktokapipy.api import TikTokAPI


def do_something(username):
    with TikTokAPI() as api:
        user = api.user("vanerdd")
        # Print the user ID and signature
        print(
            f' Nickname:{user.nickname},User Signature: {user.signature}')
        for video in user.videos:
            num_comments = video.stats.comment_count
            num_likes = video.stats.digg_count
            num_views = video.stats.play_count
            num_shares = video.stats.share_count
            # Output or store the statistics as needed
            print(
                f'Video: {video.id}, Likes: {num_likes}, Comments: {num_comments}, Views: {num_views}, Shares: {num_shares}')


# Call the function with a specific username
do_something('some_tiktok_username')
