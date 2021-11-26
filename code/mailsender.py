import time
from config import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

print("Кому: ", end='')
mail = input()

print("Cообщение: ", end='')
mes = input()

browser = webdriver.Chrome(executable_path=r'C:\проги\питон\moduls\chromedriver.exe', options=options)
browser.get('https://account.mail.ru/')

for i in range(36, 0, -1):
    print(f'\rБраузер запускается...{float(i)}', end='', flush=True)
    time.sleep(1)

print('\nБраузер успешно запустился. Начинается авторизация...')

login = browser.find_element_by_xpath('//input[@name="username"]').send_keys(data['login'])
submit1 = browser.find_element_by_tag_name('button').click()

time.sleep(2)

password = browser.find_element_by_xpath('//input[@name="password"]').send_keys(data['password'])
submit2 = browser.find_element_by_tag_name('button').click()

print('Авторизация прошла успешно.')

for i in range(36, 0, -1):
    print(f'\rВходим в аккаунт...{float(i)}', end='', flush=True)
    time.sleep(1)

browser.get('https://e.mail.ru/compose/')

for i in range(16, 0, -1):
    print(f'\rЗагружаем форму для отправки письма...{float(i)}', end='', flush=True)
    time.sleep(1)

who = browser.find_element_by_xpath('//input[@style="width: 12px;"]').send_keys(mail)
print('\nУказываем почту получателя...')

message = browser.find_element_by_xpath('//div[@role="textbox"]/div[1]').send_keys(mes)
print('Вводим сообщение...')

time.sleep(2)

sender = browser.find_element_by_xpath('//span[@title="Отправить"]').click()
print('Отлично! Письмо успешно отправлено!')

browser.quit()
