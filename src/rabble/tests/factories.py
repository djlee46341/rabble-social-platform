import factory
from django.contrib.auth import get_user_model
from rabble.models import Communities, Subrabbles, Posts, Comments

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Faker("email")
    password = "password"


class CommunityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Communities
    community_name = factory.Sequence(lambda n: f"Community{n}")
    user = factory.SubFactory(UserFactory)


class SubrabbleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subrabbles
    subrabble_name = factory.Sequence(lambda n: f"Subrabble{n}")
    identifier = factory.Sequence(lambda n: f"subrabble-{n}")
    description = factory.Faker("sentence")
    community = factory.SubFactory(CommunityFactory)
    is_public = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Posts
    title = factory.Faker("sentence")
    body = factory.Faker("paragraph")
    user = factory.SubFactory(UserFactory)
    subrabble = factory.SubFactory(SubrabbleFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comments
    body = factory.Faker("sentence")
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
