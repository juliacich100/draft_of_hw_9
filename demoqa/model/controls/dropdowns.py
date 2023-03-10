from selene.support.shared import browser
from selene import command, have


# def select_option(selector, value):
#     browser.element(selector + ' [id^=react-select][id*=input]').type(value).press_enter()

class Dropdowns:
    def __init__(self, element):
        self.element = element

    def select_option(self, value):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()
        return self