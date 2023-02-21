from demoqa.model.pages.practice_form import practice_form
from demoqa.data.user_data import Sponge_Bob
import time


def test_open_browser(browser_management):
    practice_form.open_chrome()
    practice_form.fill_registration_form(Sponge_Bob)
    practice_form.submit()
#    time.sleep(10)

    practice_form.validate_submitted_data(Sponge_Bob)