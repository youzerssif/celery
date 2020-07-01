from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .. import manager

def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(manager.collection_api, 'interval', seconds=5)
    # scheduler.add_job(manager.data_collection, 'interval', seconds=5)
    # scheduler.add_job(getInfo.getUrl, 'cron', hour=10, minute=7)
    scheduler.start()
