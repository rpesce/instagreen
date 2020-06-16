# Defining 'like' methods


# Todo: User needs to pass 'tags' argument
def like_by_tags(session, tags, amount=10, skip_top_posts=True, randomize=False, media=None):
    session.like_by_tags(tags, amount=amount, skip_top_posts=skip_top_posts, randomize=randomize, media=media)
    # Not included: use_smart_hashtags, use_smart_location_hashtags, interact


# Todo: User needs to pass 'tags' argument
def like_by_tags_and_interact(session, tags, like_amount=10, interact_amount=3, randomize=True, percentage=100,
                              media=None):
    session.set_user_interact(amount=interact_amount, randomize=randomize, percentage=percentage, media=media)
    session.like_by_tags(tags, amount=like_amount, interact=True)


def like_by_feed(session, amount=100, randomize=True, unfollow=True, interact=True):
    session.like_by_feed(amount=amount, randomize=randomize, unfollow=unfollow, inteact=interact)


# Todo: User needs to pass 'locations' argument
def like_by_locations(session, locations, amount=100, skip_top_posts=False):
    session.like_by_locations(locations, amount=amount, skip_top_posts=skip_top_posts)


# Defining 'follow' methods
def follow_by_tags(session, tags, amount=10, skip_top_posts=True, randomize=False, media=None):
    session.follow_by_tags(tags, amount=amount, skip_top_posts=skip_top_posts, randomize=randomize, media=media)
    # Not included: use_smart_hashtags, use_smart_location_hashtags, interact


# Todo: User needs to pass 'locations' argument
def follow_by_locations(session, locations, amount=100, skip_top_posts=False):
    session.follow_by_locations(locations, amount=amount, skip_top_posts=skip_top_posts)


# Todo: Get the list of followers
def follow_user_followers(session, users, amount=10, randomize=False):
    session.follow_user_followers(users, amount=amount, randomize=randomize)


def follow_user_following(session, users, amount=10, randomize=False):
    session.follow_user_following(users, amount=amount, randomize=randomize)


def follow_and_interact_user_followers(session, followers, amount_interact=5, randomize_interact=True, percentage=50,
                                       media=None,
                                       amount_followers=10, randomize_followers=False, interact=True):
    session.set_user_interact(amount=amount_interact, randomize=randomize_interact, percentage=percentage, media=media)
    session.follow_user_followers(followers, amount=amount_followers, randomize=randomize_followers, interact=interact)


def follow_likers(session, users, amount=2, percentage=70, randomize_interact=True, media=None, photos_grab_amount=2,
                  follow_likers_per_photo=3, randomize=True, sleep_delay=600, interact=False):
    session.set_user_interact(amount=amount,
                              percentage=percentage,
                              randomize=randomize_interact,
                              media=media)
    session.follow_likers(users,
                          photos_grab_amount=photos_grab_amount,
                          follow_likers_per_photo=follow_likers_per_photo,
                          randomize=randomize,
                          sleep_delay=sleep_delay,
                          interact=interact)


# Defining 'unfollow' methods
def unfollow_instapy_users(session, amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501):
    session.unfollow_users(amount=amount, instapy_followed_enabled=instapy_followed_enabled,
                           instapy_followed_param=instapy_followed_param, style=style, unfollow_after=unfollow_after,
                           sleep_delay=sleep_delay)


def unfollow_users_who_dont_follow_back(session, amount=126, nonFollowers=True, style="RANDOM",
                                        unfollow_after=42 * 60 * 60,
                                        sleep_delay=655):
    session.unfollow_users(amount=amount, nonFollowers=nonFollowers, style=style, unfollow_after=unfollow_after,
                           sleep_delay=sleep_delay)


def accept_follow_requests(session, amount=100, sleep_delay=1):
    session.accept_follow_requests(amount=amount, sleep_delay=sleep_delay)


def remove_follow_requests(session, amount=200, sleep_delay=600):
    session.remove_follow_requests(amount=amount, sleep_delay=sleep_delay)


def skip_users(session, keywords):
    session.set_skip_users(skip_bio_keyword=keywords)


# Settings with restrictions and exclusions
def restricting_likes(session, keywords):
    session.set_dont_like(keywords)


def ignoring_users(session, users):
    session.set_ignore_users(users)


def excluding_friends(session, friends):
    session.set_dont_include(friends)


if __name__ == '__main__':
    # Todo: Remove this from here and just import session from create_sessions
    import create_sessions
    from Old_stuff.passwords import u, p

    session = create_sessions.create_session(u, p)
