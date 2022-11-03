import random
import time

from selenium.common import UnexpectedAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.basepage import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()
    def check_opened_new_tab(self):
        self.is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def see_alert(self):
        self.is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.is_visible(self.locators.APPEAR_ALERT_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f'autotest{random.randint(0,100)}'
        self.is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.is_present(self.locators.PROPMT_RESULT).text
        return text, text_result