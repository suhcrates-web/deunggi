from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def send_key_really(driver0, id, letters, cmd=''):
    suc0 = False
    while suc0 == False:
        try:
            elem = driver0.find_element(By.ID, id)
            elem.send_keys('')

            suc0 = True
        except:
            pass

    suc0 = False
    print(letters)
    while suc0 == False:
        print(f"{letters} a")
        elem.send_keys('a')
        len0 = len(driver0.find_element(By.ID, id).get_attribute('value'))
        if len0 > 0:
            suc0 = True

        for _ in range(len0):
            elem.send_keys(Keys.BACKSPACE)

    for i in letters:
        elem.send_keys(i)

    if cmd == 'go':
        elem.send_keys('\n')