# --- 1. CREAR LA PRIMERA QUESTION AMB 2 CHOICES ---
        # Naveguem a la URL per afegir una nova Question
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/add/'))
        
        # Omplim el text de la Question
        self.selenium.find_element(By.NAME, "question_text").send_keys("Quina és la teva estació de l'any preferida?")
        
        # Fem servir els accessos directes "Today" i "Now" de Django per omplir la data de publicació automàticament
        self.selenium.find_element(By.XPATH, "//a[text()='Today']").click()
        self.selenium.find_element(By.XPATH, "//a[text()='Now']").click()

        # Omplim les opcions (Choices) dins dels formularis inline
        # Django nomena els inlines per defecte com choice_set-0, choice_set-1, etc.
        self.selenium.find_element(By.NAME, "choice_set-0-choice_text").send_keys("Estiu")
        self.selenium.find_element(By.NAME, "choice_set-1-choice_text").send_keys("Hivern")
        
        # Cliquem el botó de desar
        self.selenium.find_element(By.NAME, "_save").click()

        # --- 2. CREAR LA SEGONA QUESTION AMB 2 CHOICES ---
        # Repetim el procés per a la segona Question
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/add/'))
        
        self.selenium.find_element(By.NAME, "question_text").send_keys("Quin és el teu llenguatge de programació preferit?")
        
        self.selenium.find_element(By.XPATH, "//a[text()='Today']").click()
        self.selenium.find_element(By.XPATH, "//a[text()='Now']").click()

        self.selenium.find_element(By.NAME, "choice_set-0-choice_text").send_keys("Python")
        self.selenium.find_element(By.NAME, "choice_set-1-choice_text").send_keys("JavaScript")
        
        self.selenium.find_element(By.NAME, "_save").click()

        # --- 3. COMPROVAR AL MENÚ CHOICES QUE HI SÓN LES 4 ---
        # Anar a la llista de l'apartat de Choices
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/choice/'))
        
        # Obtenim tot el codi font de la pàgina de llistat de Choices per fer els asserts
        pagina_font = self.selenium.page_source
        
        # Comprovem que les 4 opcions (Choices) que hem creat apareixen efectivament a la pantalla
        self.assertIn("Estiu", pagina_font)
        self.assertIn("Hivern", pagina_font)
        self.assertIn("Python", pagina_font)
        self.assertIn("JavaScript", pagina_font)
