import time

import cv2
import numpy as np
import pyautogui
import pydirectinput

def template_match_and_click_on_second_screen(object_image_path):
    # Einen Screenshot des aktuellen Bildschirms machen
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    template = cv2.imread(object_image_path)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Template Matching anwenden
    result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Die beste Übereinstimmung finden
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Die Koordinaten des besten Matchs berechnen
    top_left = max_loc
    w, h = template.shape[1], template.shape[0]
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Zentrum des besten Matchs berechnen
    center_x, center_y = top_left[0] + w//2, top_left[1] + h//2

    # Maus auf dem zweiten Bildschirm bewegen und klicken
    # Hier musst du die Bildschirmkoordinaten des zweiten Monitors angeben
    # Beispiel: Wenn dein Hauptbildschirm 1920x1080 ist, könnte der Startpunkt des zweiten Bildschirms 1920,0 sein
    second_screen_x = center_x + 1920  # Die X-Koordinate für den zweiten Bildschirm anpassen
    second_screen_y = center_y

    pydirectinput.moveTo(second_screen_x, second_screen_y)
    pydirectinput.click()

# Pfad zum Template-Bild setzen
object_image_path = 'C:\\Users\\Downloads\\object.png'

# Funktion aufrufen
template_match_and_click_on_second_screen(object_image_path)
