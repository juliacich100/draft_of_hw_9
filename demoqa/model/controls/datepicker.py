import datetime
from selene.support.shared import browser


# def select_date_of_birth():
#     browser.element('[class = "react-datepicker__input-container"]').click()
#     browser.element('[class = "react-datepicker__month-select"]').click()
#     browser.element('[value= "10"]').click()
#     browser.element('[class = "react-datepicker__year-select"]').click()
#     browser.element('[value="1985"]').click()
#     browser.element('[class = "react-datepicker__day react-datepicker__day--014"]').click()


'''Создаем класс Datepicker'''


class Datepicker:
    def __init__(self, element):
        self.element = element

    def select_date_of_birth(self, date: datetime.date):
        self.element.click()
        browser.element('[class = "react-datepicker__month-select"]').click()
        browser.element(f'[value="{date.month - 1}"]').click()
        browser.element('[class = "react-datepicker__year-select"]').click()
        browser.element(f'[value="{date.year}"]').click()
        browser.element(f'.react-datepicker__day--0{date.day}').click()
        return self



