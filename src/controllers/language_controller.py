from flask import render_template, Blueprint, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


language_controller = Blueprint("language_controller", __name__)


@language_controller.route("/", methods=["GET"])
def translate_index():
    languages = LanguageModel.list_dicts()
    phrases = {
        "languages": languages,
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }
    return render_template("index.html", **phrases)


@language_controller.route("/", methods=["POST"])
def translate_post():
    text_to_translate = request.form.get("text_to_translate")
    translate_from = request.form.get("translate_from")
    translate_to = request.form.get("translate_to")

    translator = GoogleTranslator(
        source=translate_from, target_language=translate_to
    ).translate(text_to_translate)

    languages = LanguageModel.list_dicts()
    phrases = {
        "languages": languages,
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translator,
    }

    return render_template("index.html", **phrases)
