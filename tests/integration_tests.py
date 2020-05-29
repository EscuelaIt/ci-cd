import requests


def test_admin_url():
    r = requests.get('https://meetup.carlosmart.co/admin/')
    assert r.status_code == 200


def test_root_url():
    r = requests.get('https://meetup.carlosmart.co/')
    assert r.status_code == 404