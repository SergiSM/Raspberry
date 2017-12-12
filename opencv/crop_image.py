
import cv2
img = cv2.imread("captura_pantalla.png")
crop_img = img[100:700, 800:1200] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imshow("cropped", crop_img)
cv2.imwrite("captura_pantalla_crop.png", crop_img)
cv2.waitKey(0)
