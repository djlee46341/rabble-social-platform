import pytest
from django.urls import reverse
from rest_framework import status
from rabble.models import Posts
from rest_framework.test import APIClient
from rabble.tests.factories import (
    UserFactory,
    CommunityFactory,
    SubrabbleFactory,
    PostFactory,
)

@pytest.mark.django_db
def test_post_post(api_client):
    user = UserFactory()
    api_client.force_authenticate(user=user)

    subrabble = SubrabbleFactory(community=CommunityFactory())
    url = reverse("subrabble-posts", args=[subrabble.identifier])
    payload = {
        "title": "Non-Cs courses?",
        "body": "I know this is a CS subRabble, but I was wondering if anyone had recommendations for fun non-CS courses.",
        "author": user.username 
    }
    resp = api_client.post(url, payload, format="json")
    #print(resp.json())
    assert resp.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_post_patch(api_client):
    user = UserFactory()
    api_client.force_authenticate(user=user)

    post = PostFactory(user=user)
    url = reverse("post-detail", args=[post.subrabble.identifier, post.pk])

    response = api_client.patch(url, {"title": "Updated!!!"}, format="json")
    assert response.status_code == 200
    post.refresh_from_db()
    assert post.title == "Updated!!!"

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_subrabble_get(api_client):
    subrabble = SubrabbleFactory()
    response = api_client.get(reverse("subrabble-detail", args=[subrabble.identifier]))
    data = response.json()
    assert data["identifier"] == subrabble.identifier
    assert data["subrabble_name"] == subrabble.subrabble_name
