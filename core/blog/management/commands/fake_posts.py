from django.core.management.base import BaseCommand, CommandError
import faker
from blog.models import Post, Category
from accounts.models.profile import Profile
from accounts.models.user import CustomUser
import random


class Command(BaseCommand):
    help = "creates fake blog posts to work with in dev phase"

    def handle(self, *args, **options):
        fake = faker.Faker()

        user_profile = CustomUser.objects.get(email="admin@admin.com").profile.all()

        for i in range(10):
            post = Post.objects.create(
                author=user_profile[0],
                slug=fake.slug(),
                title=fake.sentence(nb_words=4),
                banner=None,
                body=fake.text(),
                status=True,
            )

            post.category.add(Category.objects.create(name=fake.name()))
        print("posts has been created")
