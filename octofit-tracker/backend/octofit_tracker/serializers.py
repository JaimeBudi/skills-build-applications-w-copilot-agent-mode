from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'team', 'is_superhero']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty']

    def get_id(self, obj):
        return str(obj._id) if hasattr(obj, '_id') and obj._id else None
