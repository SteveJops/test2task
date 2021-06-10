# imports
from apscheduler.schedulers.blocking import BlockingScheduler
from datadb import insertData
from datetime import datetime


def timeNow():
    """
    The Func starts function from datadb.py file
    :return: None
    """
    insertData()
    print(f'The time is: {datetime.now()}')


def main():
    """
    The func creates scheduler automatic job
    to start whole project at 9.00 o`clock daily
    :return: None
    """
    scheduler = BlockingScheduler()
    scheduler.add_job(timeNow, 'cron', day_of_week='1-6', hour=9, minute=0)
    scheduler.start()


if __name__ == '__main__':
    main()


