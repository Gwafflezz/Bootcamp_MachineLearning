import cv2
import numpy as np
 
cap = cv2.VideoCapture(0) #Abre a câmera para captura de vídeo;

##seleção de cores pelo usuário
while True: 
    print("Escolha uma cor para o filtro:")
    print("1 = Vermelho")
    print("2 = Azul")
    print("3 = Verde")
    print("4 = Amarelo")
    print("5 = Rosa")
    print("6 = Todas exceto branco")
    print("7 = cancelar")

    cor = input("Cor escolhida: ")
    if cor == "7": 
        break

    while True:
        
        _, frame = cap.read() # Lê e retorna um frame da captura de vídeo; 
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        #Intervalos para o vermelho:
        low_red1 = np.array([0, 100, 100])
        high_red1 = np.array([10, 255, 255])
        red_mask1 = cv2.inRange(hsv_frame, low_red1, high_red1)
        
        low_red2 = np.array([170, 100, 100])
        high_red2 = np.array([179, 255, 255])
        red_mask2 = cv2.inRange(hsv_frame, low_red2, high_red2)
        
        red_mask = red_mask1 | red_mask2 #combinação dos dois intervalos
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

        #Intervalo para o amarelo:
        low_yellow = np.array([20, 100, 100])
        high_yellow= np.array([30, 255, 255]) 
        yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
        yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

        #Intervalo para o rosa:
        low_pink = np.array([160, 100, 100])
        high_pink = np.array([170, 255, 255]) 
        pink_mask = cv2.inRange(hsv_frame, low_pink, high_pink)
        pink = cv2.bitwise_and(frame, frame, mask=pink_mask) 

        #todas as cores exeto branco
        low = np.array ([0,45,0]) 
        high = np.array ([179,255,255])
        excpBranco_mask = cv2.inRange(hsv_frame, low, high)
        excpBranco = cv2.bitwise_and(frame, frame, mask= excpBranco_mask)

        key = cv2.waitKey(1) #Delay de 1ms para um evento de tecla

        if cor == "1": 
            cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
            cv2.imshow("filtro vermelho", red)
            if key == 27: 
                cv2.destroyAllWindows()
                break
                
        elif cor == "2":
            cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
            cv2.imshow("filtro azul", blue)
            if key == 27: 
                cv2.destroyAllWindows()
                break
        elif cor == "3":
            cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
            cv2.imshow("filtro verde", green)
            if key == 27: 
                cv2.destroyAllWindows()
                break
         
        elif cor =="4" :
            cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
            cv2.imshow("filtro amarelo", yellow)
            if key == 27: 
                cv2.destroyAllWindows()
                break
         
        elif cor == "5":
            cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
            cv2.imshow("filtro rosa", pink)
            if key == 27: 
                cv2.destroyAllWindows()
                break
         
        elif cor == "6":
            cv2.imshow("frame", frame ) # Exibe a imagem em uma janela;
            cv2.imshow("todas exceto verde", excpBranco)
            if key == 27: 
                cv2.destroyAllWindows()
                break
                             

cap.release() # libera a câmera para outros processos
cv2.destroyAllWindows() # fecha todas as janelas abertas pelo OpenCV
