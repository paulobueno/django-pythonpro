from django.test import Client


def test_status_home(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
