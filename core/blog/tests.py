import pytest
from django.contrib.auth import get_user_model
from .models import Post, Category
import datetime

# Create your tests here.

User = get_user_model()


@pytest.fixture
def user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a@>/123456"
    )
    return user

@pytest.fixture
def category():
    category = Category.objects.create(name='CAT1')
    return category

@pytest.mark.django_db
class TestBlogPost:
    def test_post_create(self, user, category):
        
        time = datetime.datetime.now()
        post = Post.objects.create(
            author=user,
            category= category,
            title="sample_title",
            image=None,
            body="this is a body",
            created_date=time,
            published_date=None,
            updated_date=None
        )
        assert category.name == 'CAT1'
        assert post.created_date == time
        assert post.status == False
        assert post.author.email == "admin@admin.com"

