import cv2
import numpy as np

def empty(a):
    pass

# Crear ventana de configuración de rango de colores
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)

# la 
cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue Max", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Val Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Val Max", "HSV", 255, 255, empty)

# Configurar la webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convertir la imagen a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Obtener los valores del rango de colores
    h_min = 0
    h_max = 179
    s_min = 160
    s_max = 255
    v_min = 170
    v_max = 255
    
    # Crear el rango de colores en HSV
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Crear una máscara para filtrar los colores deseados
    mask = cv2.inRange(hsv, lower, upper)

    # Dibujar los contornos de los objetos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar rectángulos alrededor de los objetos detectados
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"x 283{x} Y: {y}", (x+w+20,y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 1)
            print(f"Ubicación: X: {x} Y: {y}")

    # Mostrar la imagen con los rectángulos dibujados alrededor de los objetos detectados
    cv2.imshow("frame", frame)

    # Salir del bucle cuando la tecla 'q' es presionada
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Liberar recursos y cerrar ventanas
cap.release()
cv2.destroyAllWindows()