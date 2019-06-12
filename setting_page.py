import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"

    @allure.step(title='点击搜索')
    def click_search(self):
        self.click(self.search_button)