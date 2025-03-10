from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import YouTubeValidator


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YouTubeValidator(field='video_url')]


class CourseSerializers(serializers.ModelSerializer):
    lessons = LessonSerializers(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    course_count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializers(many=True)
    subscription = serializers.SerializerMethodField()

    def get_course_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = ('title', 'description', 'course_count_lesson', 'lessons', 'subscription')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("sign_of_subscription",)