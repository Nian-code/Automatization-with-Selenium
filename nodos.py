from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from colorama import Fore
from seleniumwire import webdriver
import time
import yaml



options = Options()
options.page_load_strategy = 'none'
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--log-level=3')
browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)

radios = {}

def extract(username, password, sg, botton, n,v):
    try:
        browser.find_element_by_id(username).send_keys("USER")
        browser.find_element_by_id(password).send_keys("PASSWORD")
        browser.find_element_by_css_selector(botton).click()
        time.sleep(sg * 0.8)
        nombre = browser.find_element_by_xpath(n).text
        velocidad = browser.find_element_by_xpath(v).text
        print(Fore.YELLOW, nombre + "\x1b[0m velocidad: " + Fore.RED , velocidad)
        radios[nombre] = velocidad
        return "OK"
    except:
        return None

def radio_web(url,  username, password, sg, botton, n,v):  
    a = None  
    try:
        browser.get(url)
        time.sleep(sg/10)
        for request in browser.requests:
            if request.response.status_code == 200:
                extract(username, password, sg, botton, n,v)
                break
    except:            
        radios[url] = "Lento o no funciona"
        return print('\033[91m',f"No se pudo acceder a \033[94m{url}",'\x1b[0m')
  
with open(r'urls.yaml') as file:
    u = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    

radio_web("http://10.1.250.6", u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])         # Martinica to oficina1
radio_web("http://10.1.250.4", u["air_user"], u["air_pass"], 4,u["air_submit"],
    u["air_path_name"],u["air_path_speed"])         # Martinica to oficina2
radio_web("http://10.1.250.5", u["air_user"], u["air_pass"], 4,u["air_submit"],
    u["air_path_name"],u["air_path_speed"])         # Oficina to Martinica1
radio_web("http://10.1.250.3", u["air_user"], u["air_pass"], 4,u["air_submit"],
    u["air_path_name"],u["air_path_speed"])         # Oficina to Martinica2
radio_web("https://10.1.1.97", u["RP_user"], 
    u["RP_pass"], 6,   u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])   # Martinica to Picalena
radio_web("https://10.1.1.99", u["RP_user"], 
    u["RP_pass"],6, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])   # Martinica to Sector Totumo
radio_web("https://10.1.8.100",u["air_user"], u["air_pass"], 5, u["air_submit"],
    u["air_path_name"],u["air_path_speed"]) # Martinica to Sector Ibague
radio_web("https://10.1.4.110 ",u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"]) # Aeropuerto
radio_web("https://10.1.8.102 ",u["air_user"], u["air_pass"], 5, u["air_submit"],
    u["air_path_name"],u["air_path_speed"]) # Sector sur
radio_web("https://10.1.8.103 ",u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"]) # RF Jordan
radio_web("https://10.1.8.101", u["RP_user"], 
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])   # Sector Jordan
radio_web("https://10.1.100.31 ", u["RP_user"], 
    u["RP_pass"],7, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"]) # Martinica to Asamblea
radio_web("https://10.1.33.106",u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])   # Martinica to beneficiencia
radio_web("https://10.1.1.106",u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"]) # Martinica to San Luis Gonzaga
radio_web("https://10.1.200.120",u["air_user"], u["air_pass"], 7, u["air_submit"],
    u["air_path_name"],u["air_path_speed"]) # Martinica to Vibra Salado
radio_web("https://10.1.9.105", u["RP_user"], 
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"]) # Martinica to Tesorito
radio_web("https://10.1.51.101",u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])
radio_web("https://10.1.9.104", u["RP_user"], # Martinica To Cumbre
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica To Gallo
radio_web("https://10.1.1.34", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Gobernación
radio_web("https://10.1.66.105", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to los Llanos
radio_web("https://10.1.3.150", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to los Pico de Oro
radio_web("https://10.1.100.82", u["RP_user"],
    u["RP_pass"],7, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to los Porvenir
radio_web("https://10.1.6.103", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Amarillas 
radio_web("https://10.1.80.101", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Cima 
radio_web("https://10.1.41.100",u["air_user"], u["air_pass"], 4, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])                                 # Martinica to Vibra Golupo
radio_web("https://10.1.15.200", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Luz
radio_web("https://10.1.102.107", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to La Maria
radio_web("https://10.1.100.91", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Samaria
radio_web("https://10.1.5.200", u["RP_user"],
    u["RP_pass"],5, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to cumbre
radio_web("https://10.1.101.101", u["RP_user"],
    u["RP_pass"],7, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to San dimas
radio_web("https://10.1.50.110",u["air_user"], u["air_pass"], 6, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])                                 # Martinica to Samoa
radio_web("https://10.1.60.93", u["RP_user"],
    u["RP_pass"],8, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Chinca
radio_web("https://10.1.55.1",u["air_user"], u["air_pass"], 6, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])                                 # Martinica to Tolima real
radio_web("https://10.1.1.128", u["RP_user"],
    u["RP_pass"],8, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Ramos y astilleros
radio_web("https://10.1.1.188", u["RP_user"],
    u["RP_pass"],8, u["RP_submit"], u["RP_path_name"], u["RP_path_speed"])  # Martinica to Nazareth
radio_web("https://10.1.15.101",u["air_user"], u["air_pass"], 6, u["air_submit"],
    u["air_path_name"],u["air_path_speed"])                                 # Martinica to Villalobos
browser.close()
print(radios)

# 10.1.9.100