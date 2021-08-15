from django.test import TestCase, Client, client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="stupid@testemail.com",
            password="dummyPword"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@fakeemail.com",
            password="test123",
            name="Test User"
        )

    def test_for_users_listed(self):
        '''Test users are listed on user page'''
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)