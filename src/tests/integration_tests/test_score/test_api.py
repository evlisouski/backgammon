from src.tests.conftest import ac, open_mock_json


async def test_calculate_score(ac: ac):
    json_array = open_mock_json('score')
    for i in json_array:
        response = await ac.post("/score/calculate_score", json=i["request"])
        assert response.json() == i["response"]
