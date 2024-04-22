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
def post_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    phrases = {
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translated,
    }

    languages = LanguageModel.list_dicts()
    return render_template("index.html", languages=languages, **phrases)


@language_controller.route("/reverse", methods=["POST"])
def reverse_post():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    phrases = {
        "text_to_translate": translated,
        "translate_from": translate_to,
        "translate_to": translate_from,
        "translated": text_to_translate,
    }

    languages = LanguageModel.list_dicts()
    return render_template("index.html", languages=languages, **phrases)
