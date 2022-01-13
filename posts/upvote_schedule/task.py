from apscheduler.schedulers.background import BackgroundScheduler
from posts.api.views import PostsAPIView
from posts.api.views import UpvoteAPIView


def start():
    scheduler = BackgroundScheduler()
    post = UpvoteAPIView()
    scheduler.add_job(post.reset_upvote, "interval", hours=24, id="reset_001")
    scheduler.start()