import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



#abrir página
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.youtube.com/")
driver.get_screenshot_as_file("C:\\Users\\Daniel Baez\\Desktop\\Tareas_realizadas\\2023 C-3\\Programación 3\\ProyectoAutomatizaciónPython\\capturasdepantalla\\abrirpágina.png")

#Barra de busqueda
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='search_query']")))
driver.get_screenshot_as_file("C:\\Users\\Daniel Baez\\Desktop\\Tareas_realizadas\\2023 C-3\\Programación 3\\ProyectoAutomatizaciónPython\\capturasdepantalla\\barradebusqueda.png")

#Tema a buscar
search.clear()
search.send_keys("Píldora Informatica")
driver.get_screenshot_as_file("C:\\Users\\Daniel Baez\\Desktop\\Tareas_realizadas\\2023 C-3\\Programación 3\\ProyectoAutomatizaciónPython\\capturasdepantalla\\temaquequierobuscar.png")

#Pulsar lupa de búsqueda
button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID,"search-icon-legacy"))).click()
driver.get_screenshot_as_file("C:\\Users\\Daniel Baez\\Desktop\\Tareas_realizadas\\2023 C-3\\Programación 3\\ProyectoAutomatizaciónPython\\capturasdepantalla\\lupadebusqueda.png")

#Acceder al canal Principal
acceder = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"main-link"))).click()
driver.get_screenshot_as_file("C:\\Users\\Daniel Baez\\Desktop\\Tareas_realizadas\\2023 C-3\\Programación 3\\ProyectoAutomatizaciónPython\\capturasdepantalla\\busqueda.png")


#Abrir en segunda página Primer Video que aparece
openfirstvideo = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-channel-video-player-renderer/div[1]/ytd-player/div/div/div[3]/div[2]/div/a'))).click()
driver.get_screenshot_as_file("C:\\Users\\Daniel Baez\\Desktop\\Tareas_realizadas\\2023 C-3\\Programación 3\\ProyectoAutomatizaciónPython\\capturasdepantalla\\segundoventana.png")


#Volver a primera Página
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
driver.close()


#Tiempo de la página abierta
time.sleep(20)



