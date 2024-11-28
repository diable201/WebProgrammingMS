from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from blog.models import Post


class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = self.get_jwt_token(self.user)
        self.post = Post.objects.create(
            title="Test Post", content="Test Content", author=self.user
        )
        self.api_namespace = "api_v2"

    def get_jwt_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_list_posts(self):
        url = reverse(f"{self.api_namespace}:post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.authenticate()
        data = {"title": "New Post", "content": "New Content"}
        url = reverse(f"{self.api_namespace}:post-list")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if self.api_namespace == "api_v1":
            self.assertEqual(response.data["author_username"], self.user.username)
        else:
            self.assertEqual(
                str(response.data["author_full_name"]).strip(),
                self.user.get_full_name(),
            )
        post_id = response.data["id"]
        post = Post.objects.get(id=post_id)
        self.assertEqual(post.author, self.user)

    def test_update_post(self):
        self.authenticate()
        data = {"title": "Updated Title", "content": "Updated Content"}
        url = reverse(f"{self.api_namespace}:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.put(url, data, format="json")  # Added format='json'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_retrieve_post(self):
        url = reverse(f"{self.api_namespace}:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        self.authenticate()
        url = reverse(f"{self.api_namespace}:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_post_unauthenticated(self):
        # Do not authenticate
        data = {"title": "Unauth Post", "content": "Content"}
        url = reverse(f"{self.api_namespace}:post-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_post_as_non_author(self):
        # Create another user
        other_user = User.objects.create_user(username="otheruser", password="testpass")
        # Obtain JWT token for the other user
        other_token = self.get_jwt_token(other_user)
        # Authenticate as the other user
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + other_token)
        data = {"title": "Updated by Non-Author", "content": "Still Unauthorized"}
        url = reverse(f"{self.api_namespace}:post-detail", kwargs={"pk": self.post.pk})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_rate_limiting(self):
        self.authenticate()
        url = reverse(f"{self.api_namespace}:post-list")
        for _ in range(200):
            response = self.client.post(url, {"title": "Rate Limit Test", "content": "Content"})
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
