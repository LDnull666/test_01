import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):

    search_edit_text = By.ID, "android:id/search_src_text"

    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    @allure.step(title='输入关键字')
    def input_key_word(self, text):
        allure.attach("关键字：", text)
        self.input(self.search_edit_text, text)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title='点击返回')
    def click_back(self):
        self.click(self.back_button)