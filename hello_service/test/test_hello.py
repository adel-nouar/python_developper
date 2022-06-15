import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize('test_hello', ['Hellooo', 'Good Morning', 'Hiiii'])
def test_post_hello(test_hello:str):
    response = client.post(
        '/hello',
        params={'hello': test_hello}
    )
    assert response.status_code == 200
    assert response.json() == {'hello': test_hello}
