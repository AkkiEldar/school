from rest_framework.validators import UniqueTogetherValidator

from courses_app.models import Course
from rest_framework import serializers


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']
        # Это можно сделать если у фронта есть метод post
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.objects.all(),
        #         fields=['name', 'duration', 'price']
        #     )
        # ]
