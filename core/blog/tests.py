import pytest
from django.contrib.auth import get_user_model
from .models import Post, Category
from accounts.models.profile import Profile

# Create your tests here.

User = get_user_model()


@pytest.fixture
def user_profile():
    user = User.objects.create_user(email="admin@admin.com", password="a@>/123456")
    profile = Profile.objects.get(user=user)
    return profile


@pytest.fixture
def category():
    category = Category.objects.create(name="CAT1")
    return category


@pytest.mark.django_db
class TestBlogPost:
    def test_post_create(self, user_profile, category):

        post = Post.objects.create(
            author=user_profile,
            title="sample_title",
            banner=None,
            body="this is a body",
            published_date=None,
            updated_date=None,
        )
        post.category.add(category)
        assert category.name == "CAT1"
        assert post.status == False
        assert post.author.user.email == "admin@admin.com"

    def test_post_list(self):
        pass

    def test_post_detail(self):
        pass
