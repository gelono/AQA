from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage
import time


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name, 'the full_name does not match'
            assert email == output_email, 'the email does not match'
            assert current_address == output_cur_addr, 'the current_address does not match'
            assert permanent_address == output_per_addr, 'the permanent_address does not match'

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'a problem with the checkbox selecting'


    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            selected_button_text, selected_button_text_result = radio_button_page.select_radio_button()
            for i, j in zip(selected_button_text, selected_button_text_result):
                assert i == j, f'here is no matching with the value {i}'