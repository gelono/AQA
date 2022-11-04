from selenium.common import TimeoutException

from locators.widgets_page_locators import AccordianPageLocators
from pages.basepage import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_FIRST_CONTENT},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_CONTENT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_CONTENT},
                     }
        section_title = self.is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]