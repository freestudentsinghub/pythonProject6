from rest_framework.test import APITestCase
from django.urls import reverse
from materials.models import Course, Lesson, Subscription
from users.models import CustomUser
from rest_framework import status


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@sky.com')
        self.course = Course.objects.create(title='English', description='English lessons B1', owner=self.user)
        self.lesson = Lesson.objects.create(title='English lesson', description='English lessons B1 start', course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.course.title
        )

    def test_course_create(self):
        self.assertEqual(
            Course.objects.all().count(), 1
        )

    def test_course_update(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))
        data = {
            'title': 'Python2'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Python2'
        )

    def test_course_delete(self):
        url = reverse('materials:course-detail', args=(self.course.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        url = reverse('materials:course-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "lessons": [
                        {
                            "id": self.lesson.pk,
                            "title": self.lesson.title,
                            "description": self.lesson.description,
                            "preview_image": None,
                            "video_url": None,
                            "course": self.course.pk,
                            "owner": None
                        }
                    ],
                    "title": self.course.title,
                    "preview_image": None,
                    "description": self.course.description,
                    "owner": self.user.pk
                }
            ]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@sky.com')
        self.course = Course.objects.create(title='English', description='English lessons B1', owner=self.user)
        self.lesson = Lesson.objects.create(title='English', description='English lessons B1 start', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson_detail', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.lesson.title
        )

    def test_lesson_create(self):

        self.assertEqual(
            Lesson.objects.all().count(), 1
        )

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            'title': 'Python2'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Python2'
        )

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview_image": None,
                    "video_url": None,
                    "course": self.course.pk,
                    "owner": self.user.pk
                }]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@sky.com')
        self.course = Course.objects.create(title='English', description='English lessons B1', owner=self.user)
        self.lesson = Lesson.objects.create(title='English', description='English lessons B1 start', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('materials:course_subscription')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'подписка добавлена'}
        )

    def test_subscription_delete(self):
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('materials:course_subscription')
        data = {
            'user': self.user,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'подписка удалена'}
        )