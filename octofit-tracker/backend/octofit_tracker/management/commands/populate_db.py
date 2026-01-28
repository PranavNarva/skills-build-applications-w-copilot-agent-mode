from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC')

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30)
        Activity.objects.create(user='Captain America', activity_type='Cycling', duration=45)
        Activity.objects.create(user='Batman', activity_type='Swimming', duration=60)
        Activity.objects.create(user='Superman', activity_type='Yoga', duration=20)

        # Leaderboard
        Leaderboard.objects.create(user='Iron Man', score=100)
        Leaderboard.objects.create(user='Captain America', score=90)
        Leaderboard.objects.create(user='Batman', score=95)
        Leaderboard.objects.create(user='Superman', score=85)

        # Workouts
        Workout.objects.create(name='Full Body', description='A full body workout routine')
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
