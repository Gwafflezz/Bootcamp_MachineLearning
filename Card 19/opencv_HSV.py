import cv2
import numpy as np
 
cap = cv2.VideoCapture(0) #Abre a câmera para captura de vídeo;

while True:
    
    _, frame = cap.read() # Lê e retorna um frame da captura de vídeo; 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
   
    #Intervalo para o vermelho:
    low_red = np.array([150, 50, 90])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    #Intervalo para o azul
    low_blue = np.array([100, 150,100 ])
    high_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    #Intervalo para o verde:
    low_green = np.array([35, 100, 100])
    high_green = np.array([85, 255, 255]) 
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask) 

    cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
    cv2.imshow("mascara_vermelha", red)

    key = cv2.waitKey(1) #Delay de 1ms para um evento de tecla
    if key == 27: 
        break



cap.release() # libera a câmera para outros processos
cv2.destroyAllWindows() # fecha todas as janelas abertas pelo OpenCV
