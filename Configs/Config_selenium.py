import os
import pickle
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# para modificar las opciones de webdriver en chrome
from selenium.webdriver.chrome.options import Options

#abre el chrome copn los ajustes predeterminados
def iniciar_chrome():

    #inicia chrome con los parametros indicados y devuelve el driver
    ruta = ChromeDriverManager().install()#se añadee una salida limpia enla terminal 

    options=Options() #instancia de las opciones del navegador
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}") # user agentm personalizado
    options.add_argument("--log_level=0")
    options.add_argument("--window-size=970,1080") # abre una ventana con instagram con los pixeles definidos
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications") #bloquea notificaciones de chrome
    options.add_argument("--ignore-certificate-errors") #evia el aviso de su conexzcion no es privada
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-running-insecure-content")#desactiva el aviso de contenido no seguro
    options.add_argument("--no-default-browser-check")#evita qye nchrome no es el navegador pord efecto
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationController")# evita que selenium sea detectado por el navegador. IMPORTANTE
    #PARAMETROS A OMITI EN EL INICIO DE CHROMEDRIVER
    #exp_opt=[
    #    'enable-automation' # para que no me muestre la notificacion de que un software esta manejando el navegador
    #    'ignore-certificate-errors'#ignora errores dew certificados
    #    'enable-logging' # para que no me muestre en la terminal devtool listening
    #]
    #options.add_experimental_option("--excludeSwitches", exp_opt)
    #PARAMETROS QUE DEFINEN PREFERENCIAS EN CHROMEDRIVER
    prefs={
        "profile.default_content_setting_values.notifications":2,
        "intl.acept_languages":["es-Es","es"], #idioma del navegador
        "credentials_enable_services": False #evita que chrome guarde la contrase;a
    }
    options.add_experimental_option("prefs", prefs)



    #intanciamos el servicion de chrome driver
    s= Service(ruta)
    #instanciamos webdriver de selenium
    driver = webdriver.Chrome(service=s, options=options)
    driver.set_window_position(0,0)
    # Cargar cookies si existen
    cookies_file = "cookies.pkl"
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
    #devolvemos el driver
    return driver