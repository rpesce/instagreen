from flask_login import UserMixin
from app import db
# from sqlalchemy import Table, Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    insta_account = db.relationship("InstagramAccount", backref="InstagramAccount")

    def __repr__(self):
        return '<User: {}>'.format(self.email)


class InstagramAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    instagram_username = db.Column(db.String(500))
    instagram_password = db.Column(db.String(500))

    def __repr__(self):
        return 'Instagram Account: {}'.format(self.instagram_username)


class InstagramConfigs(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    like_by_tags_enabled = db.Column(db.Boolean, default=False, nullable=False)
    like_by_tags_tags = db.Column(db.String(1000))
    like_by_tags_amount = db.Column(db.Integer, nullable=False)
    like_by_tags_skip_top_posts = db.Column(db.Boolean, default=True, nullable=False)
    like_by_tags_randomize = db.Column(db.Boolean, default=False, nullable=False)
    like_by_tags_media = db.Column(db.String(1000))

    like_by_tags_and_interact_enabled = db.Column(db.Boolean, default=False, nullable=False)
    like_by_tags_and_interact_tags = db.Column(db.String(1000), default=None) # I added default
    like_by_tags_and_interact_like_amount = db.Column(db.Integer, nullable=False, default=10) # I added default
    like_by_tags_and_interact_interact_amount = db.Column(db.Integer, nullable=False, default=3)  # I added default
    like_by_tags_and_interact_randomize = db.Column(db.Boolean, default=True, nullable=False) # I added default
    like_by_tags_and_interact_percentage = db.Column(db.Integer, nullable=False, default=100) # I added default
    like_by_tags_and_interact_media = db.Column(db.String(50), nullable=False, default=None) # I added default

    like_by_feed_enabled = db.Column(db.Boolean, default=False, nullable=False)
    like_by_feed_amount = db.Column(db.Integer, nullable=False, default=10) # I added default
    like_by_feed_randomize = db.Column(db.Boolean, nullable=False, default=True) # I added default
    like_by_feed_unfollow = db.Column(db.Boolean, nullable=False, default=True) # I added default
    like_by_feed_interact = db.Column(db.Boolean, nullable=False, default=True) # I added default

    like_by_locations_enabled = db.Column(db.Boolean, default=False, nullable=False)
    like_by_locations_locations = db.Column(db.String(1000), nullable=False, default=None)#My default
    like_by_locations_amount = db.Column(db.Integer, nullable=False, default=100)#My default
    like_by_locations_skip_to_posts = db.Column(db.Boolean, nullable=False, default=False)#My default

    follow_by_tags_enabled = db.Column(db.Boolean, default=False, nullable=False)
    follow_by_tags_tags = db.Column(db.String(1000), nullable=False, default=None) # I added default
    follow_by_tags_amount = db.Column(db.Integer, nullable=False, default=10) # I added default
    follow_by_tags_skip_top_posts = db.Column(db.Boolean, nullable=False, default=True) # I added default
    follow_by_tags_randomize = db.Column(db.Boolean, nullable=False, default=False) # I added default
    follow_by_tags_media = db.Column(db.String(50), nullable=False, default=None) # I added default

    follow_by_locations_enabled = db.Column(db.Boolean, default=False, nullable=False)
    follow_by_locations_locations = db.Column(db.String(1000), nullable=False, default=None)#My default
    follow_by_locations_amount = db.Column(db.Integer, nullable=False, default=100)#My default
    follow_by_locations_skip_to_posts = db.Column(db.Boolean, nullable=False, default=False)#My default

    follow_user_followers_enabled = db.Column(db.Boolean, default=False, nullable=False)
    follow_user_followers_users = db.Column(db.String(1000), nullable=False, default=None)
    follow_user_followers_amount = db.Column(db.Integer, nullable=False, default=10)#My default
    follow_user_followers_randomize = db.Column(db.Boolean, nullable=False, default=False)#My default

    follow_user_following_enabled = db.Column(db.Boolean, default=False, nullable=False)
    follow_user_following_users = db.Column(db.String(1000), nullable=False, default=None)
    follow_user_following_amount = db.Column(db.Integer, nullable=False, default=10)#My default
    follow_user_following_randomize = db.Column(db.Boolean, nullable=False, default=False)#My default

    follow_and_interact_user_followers_enabled = db.Column(db.Boolean, default=False, nullable=False)
    follow_and_interact_user_followers_followers = db.Column(db.String(1000), nullable=False, default=None)
    follow_and_interact_user_followers_amount_interact = db.Column(db.Integer, nullable=False, default=5)
    follow_and_interact_user_followers_randomize_interact =db.Column(db.Boolean, nullable=False, default=True)
    follow_and_interact_user_followers_percentage =db.Column(db.Integer, nullable=False, default=50)
    follow_and_interact_user_followers_media = db.Column(db.String(1000), nullable=False, default=None)
    follow_and_interact_user_followers_amount_followers =db.Column(db.Integer, nullable=False, default=10)
    follow_and_interact_user_followers_randomize_followers =db.Column(db.Boolean, nullable=False, default=False)
    follow_and_interact_user_followers_interact = db.Column(db.Boolean, nullable=False, default=True)

    follow_likers_enabled = db.Column(db.Boolean, default=False, nullable=False)
    follow_likers_users = db.Column(db.String(1000), nullable=False, default=None)
    follow_likers_amount = db.Column(db.Integer, nullable=False, default=2)
    follow_likers_percentage = db.Column(db.Integer, nullable=False, default=70)
    follow_likers_randomize_interact = db.Column(db.Boolean, nullable=False, default=True)
    follow_likers_media = db.Column(db.String(1000), nullable=False, default=None)
    follow_likers_photos_grab_amount = db.Column(db.Integer, nullable=False, default=2)
    follow_likers_follow_likers_per_photo = db.Column(db.Integer, nullable=False, default=3)
    follow_likers_randomize = db.Column(db.Boolean, nullable=False, default=True)
    follow_likers_sleep_delay = db.Column(db.Integer, nullable=False, default=600)
    follow_likers_interact = db.Column(db.Boolean, nullable=False, default=False)

    unfollow_instapy_users_enabled = db.Column(db.Boolean, default=False, nullable=False)
    unfollow_instapy_users_amount = db.Column(db.Integer, nullable=False, default=60)
    unfollow_instapy_users_instapy_followed_enabled = db.Column(db.Boolean, nullable=False, default=True)
    unfollow_instapy_users_instapy_followed_param = db.Column(db.String(1000), nullable=False, default="nonfollowers")
    unfollow_instapy_users_style = db.Column(db.String(1000), nullable=False, default="FIFO")
    unfollow_instapy_users_unfollow_after = db.Column(db.Integer, nullable=False, default=324000)
    unfollow_instapy_users_sleep_delay = db.Column(db.Integer, nullable=False, default=501)

    unfollow_users_who_dont_follow_back_enabled = db.Column(db.Boolean, default=False, nullable=False)
    unfollow_users_who_dont_follow_back_amount = db.Column(db.Integer, nullable=False, default=126)
    unfollow_users_who_dont_follow_back_nonFollowers = db.Column(db.Boolean, nullable=False, default=True)
    unfollow_users_who_dont_follow_back_style = db.Column(db.String(1000), nullable=False, default="RANDOM")
    unfollow_users_who_dont_follow_back_unfollow_after = db.Column(db.Integer, nullable=False, default=151200)
    unfollow_users_who_dont_follow_back_sleep_delay = db.Column(db.Integer, nullable=False, default=655)

    accept_follow_requests_enabled = db.Column(db.Boolean, default=False, nullable=False)
    accept_follow_requests_sleep_delay = db.Column(db.Integer, nullable=False, default=1)
    accept_follow_requests_amount = db.Column(db.Integer, nullable=False, default=100)

    remove_follow_requests_enabled = db.Column(db.Boolean, default=False, nullable=False)
    remove_follow_requests_amount = db.Column(db.Integer, nullable=False, default=200)
    remove_follow_requests_sleep_delay = db.Column(db.Integer, nullable=False, default=600)

    skip_users_enabled = db.Column(db.Boolean, default=False, nullable=False)
    skip_users_keywords = db.Column(db.String(2000), nullable=False, default=None)

    restricting_likes_keywords_enabled = db.Column(db.Boolean, default=False, nullable=False)
    restricting_likes_keywords = db.Column(db.String(2000), nullable=False, default=None)

    ignoring_users_friends_enabled = db.Column(db.Boolean, default=False, nullable=False)
    ignoring_users_friends = db.Column(db.String(2000), nullable=False, default=None)

    excluding_friends_friends_enabled = db.Column(db.Boolean, default=False, nullable=False)
    excluding_friends_friends = db.Column(db.String(2000), nullable=False, default=None)

