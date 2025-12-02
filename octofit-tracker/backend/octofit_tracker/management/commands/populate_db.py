"""
Django management command to populate the octofit_db database with test data.
Uses Django ORM for data deletion and insertion.
Sample data uses super heroes from Team Marvel and Team DC.
"""

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        team_marvel = Team.objects.create(name='Team Marvel')
        team_dc = Team.objects.create(name='Team DC')

        # Create Users (Superheroes)
        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users_data = [
            # Team Marvel
            {'email': 'ironman@avengers.com', 'name': 'Tony Stark', 'team': 'Team Marvel', 'is_superhero': True},
            {'email': 'captain@avengers.com', 'name': 'Steve Rogers', 'team': 'Team Marvel', 'is_superhero': True},
            {'email': 'blackwidow@avengers.com', 'name': 'Natasha Romanoff', 'team': 'Team Marvel', 'is_superhero': True},
            {'email': 'thor@avengers.com', 'name': 'Thor Odinson', 'team': 'Team Marvel', 'is_superhero': True},
            {'email': 'hulk@avengers.com', 'name': 'Bruce Banner', 'team': 'Team Marvel', 'is_superhero': True},
            # Team DC
            {'email': 'batman@justice.com', 'name': 'Bruce Wayne', 'team': 'Team DC', 'is_superhero': True},
            {'email': 'superman@justice.com', 'name': 'Clark Kent', 'team': 'Team DC', 'is_superhero': True},
            {'email': 'wonder@justice.com', 'name': 'Diana Prince', 'team': 'Team DC', 'is_superhero': True},
            {'email': 'flash@justice.com', 'name': 'Barry Allen', 'team': 'Team DC', 'is_superhero': True},
            {'email': 'aquaman@justice.com', 'name': 'Arthur Curry', 'team': 'Team DC', 'is_superhero': True},
        ]

        for user_data in users_data:
            User.objects.create(**user_data)

        # Create Activities
        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        activities_data = [
            {'user': 'Tony Stark', 'type': 'Running', 'duration': 45},
            {'user': 'Tony Stark', 'type': 'Strength Training', 'duration': 60},
            {'user': 'Steve Rogers', 'type': 'Running', 'duration': 90},
            {'user': 'Steve Rogers', 'type': 'Boxing', 'duration': 75},
            {'user': 'Natasha Romanoff', 'type': 'Martial Arts', 'duration': 120},
            {'user': 'Thor Odinson', 'type': 'Weightlifting', 'duration': 80},
            {'user': 'Bruce Banner', 'type': 'Yoga', 'duration': 60},
            {'user': 'Bruce Wayne', 'type': 'Martial Arts', 'duration': 180},
            {'user': 'Bruce Wayne', 'type': 'Running', 'duration': 30},
            {'user': 'Clark Kent', 'type': 'Flying', 'duration': 120},
            {'user': 'Diana Prince', 'type': 'Combat Training', 'duration': 100},
            {'user': 'Barry Allen', 'type': 'Sprinting', 'duration': 15},
            {'user': 'Arthur Curry', 'type': 'Swimming', 'duration': 180},
        ]

        for activity_data in activities_data:
            Activity.objects.create(**activity_data)

        # Create Leaderboard entries
        self.stdout.write(self.style.SUCCESS('Creating leaderboard entries...'))
        leaderboard_data = [
            {'team': 'Team Marvel', 'points': 450},
            {'team': 'Team DC', 'points': 525},
        ]

        for lb_data in leaderboard_data:
            Leaderboard.objects.create(**lb_data)

        # Create Workouts
        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workouts_data = [
            {
                'name': 'Superhero Cardio Blast',
                'description': 'High-intensity interval training designed for heroes. Includes sprints, jumping jacks, and burpees.',
                'difficulty': 'Hard'
            },
            {
                'name': 'Avengers Strength Circuit',
                'description': 'Full body strength workout with push-ups, squats, lunges, and planks.',
                'difficulty': 'Medium'
            },
            {
                'name': 'Justice League Combat Training',
                'description': 'Combat-style workout featuring shadowboxing, kicks, and defensive moves.',
                'difficulty': 'Hard'
            },
            {
                'name': 'Hero Flexibility Flow',
                'description': 'Yoga-inspired routine for flexibility and recovery. Perfect for rest days.',
                'difficulty': 'Easy'
            },
            {
                'name': 'Power Up Endurance',
                'description': 'Long-duration endurance workout including jogging, cycling, and rowing.',
                'difficulty': 'Medium'
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data!'))
        self.stdout.write(self.style.SUCCESS(f'Created: 2 teams, {len(users_data)} users, {len(activities_data)} activities, {len(leaderboard_data)} leaderboard entries, {len(workouts_data)} workouts'))
