# Importing the Important Libraries

import cv2
import mediapipe as mp
import time


# Saving the Webcam Video in an variable
Video = cv2.VideoCapture(0)

# Using the Mediapipe framework
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Code to capture/Run the Webcam Continues unless break key
while True:
    success , img = Video.read()

    # Converting the original video to RGB
    imgRGB = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)
    results = hands.process(imgRGB) # This will process the frame for us and give the result


    # Detects if there is an the hand in the webcam or not
    # Multi_hand  can also can be detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS) # mpHands.HAND_CONNECTIONS Basiclly connect all the hand points




    # showing the webcam video
    cv2.imshow("WebCam", img)

    # important line to break the webcam terminal after pressing any key
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        
        break

# For closing the terminal after use
Video.release()
cv2.destroyAllWindows()


