#pip install opencv-python
#pip install mediapipe
import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solucao_reconhecimento = mp.solutions.face_detection
reconhecedor_face=solucao_reconhecimento.FaceDetection()
desenho= mp.solutions.drawing_utils

while True:
    verificador, frame = webcam.read()
    if not verificador:
        break
    lista_rosto=reconhecedor_face.process(frame)
    if lista_rosto.detections:
        for rosto in lista_rosto.detections:
            desenho.draw_detection(frame,rosto)
    cv2.imshow("rostos_webcam",frame)
    if cv2.waitKey(5)==27:
        break
webcam.release()
cv2.destroyAllWindows()

