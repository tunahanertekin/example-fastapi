from fastapi.testclient import TestClient

from app.main import app, empty_func

client = TestClient(app)

def test1():
    response = client.get("/test1")
    assert response.status_code == 200
    assert response.json() == {"echo": "test1"}

def test2():
    response = client.get("/test2")
    assert response.status_code == 200
    assert response.json() == {"echo": "test2"}

def test3():
    response = client.get("/test3")
    assert response.status_code == 200
    assert response.json() == {"echo": "test3"}


def test4():
    response = empty_func()
    assert response == "tunahan"

