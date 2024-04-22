import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    data_test = {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    }

    history = json.loads(HistoryModel.list_as_json())

    assert data_test["text_to_translate"] == history[1]["text_to_translate"]
    assert data_test["translate_from"] == history[1]["translate_from"]
    assert data_test["translate_to"] == history[1]["translate_to"]
