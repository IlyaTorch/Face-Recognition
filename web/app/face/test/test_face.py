from django.test import TestCase
from django.test import Client
from django.urls import reverse
from face.models import Url, BoundingBox


class FaceTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_delete_item(self):
        """Test deleting image's url with bounding boxes from data base"""

        url = Url.objects.create(image_url='http://www.torch-ilya.com/picture.jpg')
        BoundingBox.objects.create(top=1, bottom=1, right=1, left=1, image=url)

        urls = Url.objects.all()
        boxes = BoundingBox.objects.all()

        self.client.get(reverse('delete', kwargs={'url_id': url.id}))
        urls = Url.objects.all()
        boxes = BoundingBox.objects.all()

        self.assertEqual(len(urls), 0)
        self.assertEqual(len(boxes), 0)
