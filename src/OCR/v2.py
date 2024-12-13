import cv2
import numpy as np

def template_match(screen_image_path, object_image_path, output_image_path):
    # Bilder laden
    screen = cv2.imread(screen_image_path)
    template = cv2.imread(object_image_path)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Template Matching anwenden
    result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Schwellenwert für die Erkennung setzen
    threshold = 0.9
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))  # Koordinaten umkehren und als Liste speichern

    # Ergebnisse auf dem Originalbild markieren
    w, h = template.shape[1], template.shape[0]
    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screen, top_left, bottom_right, (0, 255, 0), 2)  # grüner Rechteck

    # Das markierte Bild speichern
    cv2.imwrite(output_image_path, screen)

    # Überprüfen, ob mindestens eine Übereinstimmung gefunden wurde
    if locations:
        print("Objekt gefunden und markiert.")
    else:
        print("Kein Objekt gefunden.")

# Pfade zu den Bildern und zum Ausgabebild
screen_image_path = "C:\\Users\\user\\Downloads\\screen.png"
object_image_path = "C:\\Users\\user\\Downloads\\object.png"
output_image_path = 'C:\\Users\\user\\Downloads\\output_image.jpg'


# Funktion aufrufen
template_match(screen_image_path, object_image_path, output_image_path)
