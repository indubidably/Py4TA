import requests

url = "https://api.punkapi.com/v2/beers/8"


def test_get_method():
    response_get = requests.get(url)
    body_get = response_get.json()
    assert response_get.status_code == 200
    assert body_get[0]["name"] == "Fake Lager"
    assert body_get[0]["abv"] == 4.7


def test_del_method():
    response_del = requests.delete(url)
    body_del = response_del.json()
    assert response_del.status_code == 404
    assert body_del["message"] == "No endpoint found that matches '/v2/beers/8'"
