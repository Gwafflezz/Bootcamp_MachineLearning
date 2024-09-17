import cv2
import numpy as np
import pandas as pd
import zipfile
import tensorflow
import keras
from keras.models import load_model
from keras.preprocessing.image import img_to_array 

imagem = cv2.imread('/home/davi/Documentos/GitHub/MLenv/Reconhecimento_emoções/Material/Material/testes/teste_gabriel.png')

cv2.imshow("imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Caminho para o modelo e classificador
cascade_faces = "/home/davi/Documentos/GitHub/MLenv/Reconhecimento_emoções/Material/Material/haarcascade_frontalface_default.xml" # detecção de face
caminho_modelo = "/home/davi/Documentos/GitHub/MLenv/Reconhecimento_emoções/Material/Material/modelo_01_expressoes.h5" # modelo pré treinado

# Carregando modelo e classificador para detecção de faces
face_detection = cv2.CascadeClassifier(cascade_faces)
from keras.layers import BatchNormalization
classificador_emocoes = load_model(caminho_modelo, compile = False) #modelo
expressoes = ["Raiva", "Nojo", "Medo", "Feliz", "Triste", "Surpreso", "Neutro"]