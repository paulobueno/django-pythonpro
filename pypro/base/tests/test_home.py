from django.test import Client

from pypro.base.django_assertions import assert_contains


def test_status_home(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_title(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Python Project Fun - PPF</title>')
