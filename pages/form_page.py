import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.basepage import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.is_visible(self.locators.EMAIL).send_keys(person.email)
        self.is_visible(self.locators.GENDER).click()
        self.is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.is_visible(self.locators.SUBJECT).send_keys("Math")
        self.is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.is_visible(self.locators.HOBBIES).click()
        self.is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        time.sleep(1)
        self.go_to_elemenet(self.is_visible(self.locators.SELECT_STATE))
        time.sleep(1)
        self.is_visible(self.locators.SELECT_STATE).click()
        self.is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.is_visible(self.locators.SELECT_CITY).click()
        self.is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.are_visible(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_elemenet(item)
            data.append(item.text)
        return data