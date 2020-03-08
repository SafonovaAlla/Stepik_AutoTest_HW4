import pytest

def test_add_to_basket_button_localized(browser, request):
    lang = request.config.getoption("language")

    langs_buttons = {
        "ru": "Добавить в корзину",
        "es": "Añadir al carrito"
    }

    link = "http://selenium1py.pythonanywhere.com/" + lang + "/catalogue/coders-at-work_207/"
    browser.get(link)

    element = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    button_text = element.get_attribute("value")

    if not(lang in langs_buttons):
        assert False, "Language {} is not in supported langs list".format(lang)

    pattern = langs_buttons[lang]

    assert button_text == pattern, "Bad button text {} (searching {} for lang {})".format(button_text, pattern, lang)