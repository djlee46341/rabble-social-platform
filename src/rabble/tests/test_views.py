import pytest
from django.urls import reverse
from rabble.tests.factories import (
    UserFactory,
    CommunityFactory,
    SubrabbleFactory,
    PostFactory,
    CommentFactory,
)
from rabble.models import Posts

@pytest.mark.django_db
def test_index_view(client):
    default_comm = CommunityFactory(community_name="default")
    subrabbles = SubrabbleFactory.create_batch(5, community=default_comm)

    response = client.get(reverse("index"))
    assert response.status_code == 200
    html = response.content.decode()
    for sub in subrabbles:
        assert sub.subrabble_name in html
        assert sub.identifier in html

@pytest.mark.django_db
def test_subrabble_detail_view(client):
    subrabble = SubrabbleFactory()
    posts = [PostFactory(subrabble=subrabble) for _ in range(9)]
    for pt in posts:
        CommentFactory(post=pt)
    response = client.get(reverse("subrabble-detail", args=[subrabble.identifier]))
    assert response.status_code == 200
    assert len(posts) == 9
    data = response.json()
    assert data["identifier"] == subrabble.identifier
    assert data["subrabble_name"] == subrabble.subrabble_name

@pytest.mark.django_db
def test_post_create_view(client):
    user = UserFactory()
    client.force_login(user)

    subrabble = SubrabbleFactory()
    url = reverse("post-create", args=[subrabble.identifier])

    data = {"title": "TEST TEST", "body": "TEST TEST"}
    response = client.post(url, data)    
    post = Posts.objects.latest("id")
    assert post.title == data["title"]
    assert post.body == data["body"]
    assert post.subrabble == subrabble
    assert post.user == user
