import cv2
import mediapipe as mp
import time




Video = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()


while True:
    success , img = Video.read()

    cv2.imshow("WebCam", img)

    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        
        break


Video.release()
cv2.destroyAllWindows()


