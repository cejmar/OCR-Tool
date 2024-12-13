import cv2
import numpy as np

# Bild und Template laden
image = cv2.imread("C:\\Users\\Downloads\\screen.png")
template = cv2.imread("C:\\Users\\Downloads\\object.png")

# Template Matching anwenden
res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Schwellenwert festlegen und Position des Templates finden
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Wechsel der Reihenfolge der Koordinaten
    cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0,255,255), 2)

# Ergebnis anzeigen
cv2.imshow('Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
