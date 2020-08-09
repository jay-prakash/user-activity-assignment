from django.core.management.base import BaseCommand, CommandError
from accounts.models import User
from user_activity.models import UserActivity
import faker
import datetime
from django.utils.timezone import make_aware
import random


class Command(BaseCommand):
    help = 'Create dummy user activities for users'

    def add_arguments(self, parser):
        parser.add_argument('number_of_activities', type=int, nargs='?', default=5)

    def handle(self, *args, **options):
        # this is to generate fake date times
        fake = faker.Faker()
        number_of_activities = options['number_of_activities']
        if number_of_activities > 20:
            raise CommandError('Can not create more than 20 activities at once. please enter a value below 20')
        else:
            users = User.objects.all()
            for user in users:
                for _ in range(number_of_activities):
                    # generate a random seconds duration
                    duration_in_seconds = random.choice(list(range(1000, 5000)))
                    start_time = fake.date_time_between(start_date='-1y', end_date='now')
                    end_time = start_time + datetime.timedelta(seconds=duration_in_seconds)
                    UserActivity.objects.create(
                        user=user,
                        start_time=make_aware(start_time),
                        end_time=make_aware(end_time)
                    )

            self.stdout.write(self.style.SUCCESS('{} Dummy user activities was created successfully for each user'.format(number_of_activities)))