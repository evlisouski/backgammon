import json
from src.score.score_calculator import calculate
from box import Box


def open_json(dataset: str):
    with open(f"src/tests/unit_tests/test_score/{dataset}.json", encoding="utf-8") as file:
        return json.load(file)


def test_calculate():
    koks = open_json("koks")
    mars = open_json("mars")
    oin = open_json("oin")

    for i in koks:
        box_data = Box(i)
        assert calculate(box_data) == {"points": 3, "win_type": "koks"}
        assert calculate(box_data) != {"points": 2, "win_type": "mars"}
        assert calculate(box_data) != {"points": 1, "win_type": "oin"}

    for i in mars:
        box_data = Box(i)
        assert calculate(box_data) != {"points": 3, "win_type": "koks"}
        assert calculate(box_data) == {"points": 2, "win_type": "mars"}
        assert calculate(box_data) != {"points": 1, "win_type": "oin"}

    for i in oin:
        box_data = Box(i)
        assert calculate(box_data) != {"points": 3, "win_type": "koks"}
        assert calculate(box_data) != {"points": 2, "win_type": "mars"}
        assert calculate(box_data) == {"points": 1, "win_type": "oin"}
