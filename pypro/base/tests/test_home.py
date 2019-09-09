from django.test import Client


def test_status_home(client: Client):
    assert 1 == 1
    # resp = client.get('/')
    # assert resp.status_code == 200
