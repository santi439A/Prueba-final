#from Configs.Config_selenium import iniciar_chrome #inicia el navegador con mis opciones
import csv
import json
import re
from selenium.webdriver.common.by import By
import time
from Configs.Config_selenium import * #clase con mis credenciales para iniciar session automaticamente
import Configs.Config_selenium as Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configs.Ususario_IG import *

#funcion para iniciar sesion en instagram
def cargar_pagina(url): 

    print("pagina de usbisoft de instagram")    
    driver.get(url)

def seguir():
    boton_seguir = driver.find_element(By.XPATH, "//button[div[div[text()='Seguir']]]")
    boton_seguir.click()
def iniciar_sesion():
    try:
        if os.path.exists("cookies.json"):
           cargar_coockies()
        else:
            boton_iniciar_sesion=driver.find_element(By.LINK_TEXT, "Iniciar sesión")
            boton_iniciar_sesion.click()#clickeamos el inicio de sesion
            time.sleep(2)#esperamos un lapso de tiempo para que cargue la pagina

            input_usuario = driver.find_element(By.NAME, "username")
            input_usuario.send_keys(USER_IG)  # se escribe el usuario

            input_password = driver.find_element(By.NAME, "password")
            input_password.send_keys(PASS_IG) #se escribe la contraseña
            time.sleep(2)#esperamos un lapso de tiempo para que cargue la pagina

            boton_siguiente = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            boton_siguiente.click()#se clickea para seguir con el inicio de sesion.
            time.sleep(4)

            boton_aceptar_guardar_sesion = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button")
            boton_aceptar_guardar_sesion.click()#se clickear el guardarr sesion
            time.sleep(4)
            guardar_cookies()    
    except Exception as e:
        print("la pagina ha cambiado:", e)
def guardar_cookies():
    # Obtener todas las cookies
    cookies = driver.get_cookies()
    
    # Guardar las cookies en un archivo JSON
    with open("cookies.json", "w") as file:
        json.dump(cookies, file, indent=4)
def cargar_coockies():
    with open("cookies.json", "r") as file:
        cookies = json.load(file)

    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)

    driver.refresh()
    return driver

def guardar_cuenta():

    tabla = driver.find_element(By.CLASS_NAME, 'x78zum5').text
    datos=r"(\d+(?:\s?[M|K]?)?)\s?(publicaciones|seguidores|seguidos)"
    sacar = re.findall(datos, tabla)

    with open('resultados.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        for saca in sacar[:3]:
            writer.writerow([saca[0], saca[1]])

# Iniciar el servicio y navegador junto con sus configs
driver=Config.iniciar_chrome()
# URL de instagram de ubisoft
url = f"https://www.instagram.com/ubisoft/"
res=cargar_pagina(url)
time.sleep(4)
iniciar_sesion()
time.sleep(3)
guardar_cuenta()
seguir()

input("enter pasa salir")
driver.quit()