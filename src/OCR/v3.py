import cv2
import numpy as np
import pyautogui

def template_match_and_click_on_screen(object_image_path):
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

    # Bewegen der Maus zum Zentrum des besten Matchs und Doppelklick
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click(clicks=2, interval=0.2)

# Pfad zum Template-Bild setzen
object_image_path = "C:\\Users\\Downloads\\object.png"

# Funktion aufrufen
template_match_and_click_on_screen(object_image_path)





