import pytest
from django.urls import reverse

from base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(
        reverse('base:home')
    )
    return resp


def test_status_home(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(
        resp,
        '<title>Python Projects Fun - Home</title>'
    )


def test_home_link(resp):
    assert_contains(
        resp,
        f'href="{reverse("base:home")}">Python Projects Fun</a>'
    )
