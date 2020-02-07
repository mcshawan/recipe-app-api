from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from recipe.serializers import TagSerializer

TAG_URL = reverse('recipe:tag-list')

class PublicTagesApiTests(TestCase):
    """Tests publicly available api"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that the user is logged in for retrieving tags"""
        res =  self.client.get(TAG_URL)