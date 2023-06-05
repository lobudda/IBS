from selenium.webdriver.common.by import By

class PageLocators:
    GET_SINGLE_USER = (By.CSS_SELECTOR, 'li[data-id="users-single"]')
    GET_SINGLE_USER_STATUS = (By.CSS_SELECTOR, 'span[data-key="response-code"]')
    GET_SINGLE_USER_RESPONSE_BODY = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')