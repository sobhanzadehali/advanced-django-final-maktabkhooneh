import pytest
from .models.user import CustomUser


# Create your tests here.
@pytest.mark.django_db
class TestAccounts:

    def test_create_user(self):

        user = CustomUser.objects.create_user(
            email="email@email.com", password="eprqp12412sd12"
        )
        assert user != None
        assert user.is_staff == False
        assert user.is_superuser == False

    def test_create_superuser(self):

        user = CustomUser.objects.create_superuser(
            email="email@email.com", password="eprqp12412sd12"
        )
        assert user.is_superuser == True
