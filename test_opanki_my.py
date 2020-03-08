import pytest

def test_opanki(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    browser.get(link)

    element_email = browser.find_element_by_xpath('//input[@name="registration-email"]')
    element_email.send_keys("123@123")
    element_password = browser.find_element_by_xpath('//input[@name="registration-password1"]')
    element_password.send_keys("123")
    element_repeat_password = browser.find_element_by_xpath('//input[@name="registration-password2"]')
    element_repeat_password.send_keys("123")
    element_button = browser.find_element_by_xpath('//button[@name="registration_submit"]')
    element_button.click()

    element_strong = browser.find_element_by_xpath('//*[@id="register_form"]/div[1]/strong')
    element_strong_text = element_strong.text

    assert element_strong_text == "Опаньки! Мы нашли какие-то ошибки", "Соответствие не найдено, а найден текст [{}]".format(element_strong_text)