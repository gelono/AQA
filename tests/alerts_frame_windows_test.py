import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'The new tab has not opened or an incorrect tab has opened'


        def test_new_window(self, driver):
            new_tab_window= BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_window.open()
            text_result = new_tab_window.check_opened_new_window()
            assert text_result == 'This is a sample page', 'The new window has not opened or an incorrect window has opened'


    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', 'Alert did not show up'

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert alert_text == f'You entered {text}', 'Alert did not show up'