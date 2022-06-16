import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize('test_order', ['banana', 'apple', 'pear'])
def test_post_order(test_order:str):
    response = client.post(
        '/order',
        params={'order': test_order}
    )
    assert response.status_code == 200
    assert response.json() == {'Order Received': test_order}