from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    lessons = LessonSerializers(many=True)

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    course_count_lesson = serializers.SerializerMethodField()
    lessons = LessonSerializers(many=True)

    def get_course_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'course_count_lesson', 'lessons')

