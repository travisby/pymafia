from django.test import LiveServerTestCase
from selenium import webdriver

class GameTest(LiveServerTestCase):

    GAME_NAME = 'test'
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_create_new_game(self):
        self.browser.get(self.live_server_url + '/pymafia/game/create')
        name_field = self.browser.find_element_by_id('id_name')
        name_field.send_keys(self.GAME_NAME)
        save_button = self.browser.find_element_by_css_selector("input[value='Submit']")
        save_button.click()
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn(self.GAME_NAME, body_text)
