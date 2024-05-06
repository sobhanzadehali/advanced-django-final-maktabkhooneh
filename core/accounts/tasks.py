import datetime
from celery import shared_task

from accounts.models.user import CustomUser



@shared_task
def delete_abandon_users():
    # users = CustomUser.objects.filter(created_date__lte=(datetime.now - datetime.timedelta(days=31)))
    counter = 0
    # for i in users:
    #     i.delete()
    #     counter +=1
    print(f"ATTENTION!, {counter} of Users just got removed due to not getting verified during last month!.\n\
          their email in available in Subscription part.")
