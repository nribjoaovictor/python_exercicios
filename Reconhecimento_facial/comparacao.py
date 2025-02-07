import cv2
from deepface import DeepFace
import mediapipe as mp
import tf_keras

webcam = cv2.VideoCapture(0) 
solucao_reconhecimento = mp.solutions.face_detection
reconhecedor_face = solucao_reconhecimento.FaceDetection(min_detection_confidence=0.2)
desenho = mp.solutions.drawing_utils


verificador, frame = webcam.read()


lista_rosto = reconhecedor_face.process(frame)

if lista_rosto.detections:
    for rosto in lista_rosto.detections:
        bboxC = rosto.location_data.relative_bounding_box
        ih, iw, _ = frame.shape
        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
        
        rosto_cortado = frame[y:y+h, x:x+w]

        desenho.draw_detection(frame, rosto)
        cv2.imshow("Rostos Webcam", frame)
        cv2.imwrite("rosto_webcam.png", rosto_cortado)  
        resultado = DeepFace.verify(img1_path="Reconhecimento_facial/perfil_joao.png",img2_path= "rosto_webcam.png")

if resultado["verified"]:
    print("Mesma pessoa!")
else:
    print("Pessoas diferentes.")

webcam.release()
cv2.destroyAllWindows()


