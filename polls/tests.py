from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        opts.add_argument("--headless")
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)

        # creem superusuari
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_tasca_professor(self):
        # 1. LOGIN
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        self.selenium.find_element(By.NAME, "username").send_keys('isard')
        self.selenium.find_element(By.NAME, "password").send_keys('pirineus')
        self.selenium.find_element(By.XPATH, '//input[@type="submit"]').click()
        self.assertIn("Site administration", self.selenium.title)

        # 2. PRIMERA QUESTION
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/add/'))
        self.selenium.find_element(By.NAME, "question_text").send_keys("Quin és el teu color preferit?")
        self.selenium.find_element(By.XPATH, "//a[text()='Today']").click()
        self.selenium.find_element(By.XPATH, "//a[text()='Now']").click()
        self.selenium.find_element(By.NAME, "choice_set-0-choice_text").send_keys("Blau")
        self.selenium.find_element(By.NAME, "choice_set-1-choice_text").send_keys("Vermell")
        self.selenium.find_element(By.NAME, "_save").click()

        # 3. SEGONA QUESTION
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/add/'))
        self.selenium.find_element(By.NAME, "question_text").send_keys("Quin és el teu videojoc preferit?")
        self.selenium.find_element(By.XPATH, "//a[text()='Today']").click()
        self.selenium.find_element(By.XPATH, "//a[text()='Now']").click()
        self.selenium.find_element(By.NAME, "choice_set-0-choice_text").send_keys("Final Fantasy")
        self.selenium.find_element(By.NAME, "choice_set-1-choice_text").send_keys("Expedition 33")
        self.selenium.find_element(By.NAME, "_save").click()

        # 4. COMPROVAR CHOICES
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/choice/'))
        pagina_font = self.selenium.page_source
        self.assertIn("Blau", pagina_font)
        self.assertIn("Vermell", pagina_font)
        self.assertIn("Final Fantasy", pagina_font)
        self.assertIn("Expedition 33", pagina_font)
