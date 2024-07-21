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

# Defining the variable for frame_rate change

past_Time = 0
current_Time = 0

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
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # mpHands.HAND_CONNECTIONS Basically connect all the hand points


            # This line show the coordinates of each landmark in x,y,z

            for id , lm in enumerate(handLms.landmark):

                h, w, c = img.shape # Height , width , channel of the inage

                # For finding the position of the center cx,cy are the center position
                cx, cy = int(lm.x*w),int(lm.y*h) # x and y here are the coordinates of landmark
                print(id,cx,cy)

                # Detecting the id:0 of landmark and circling it
                # Basically  tracking particular lm id in hand
                if id == 0:
                    cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)




    # Defining the FPS

    current_Time = time.time()
    fps = 1/(current_Time-past_Time)
    past_Time = current_Time

    # Displaying the fps on Screen And font,size ETC

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)




    # showing the webcam video

    cv2.imshow("WebCam", img)

    # important line to break the webcam terminal after pressing any key

    if cv2.waitKey(1) & 0xFF ==ord("q"):
        
        break

# For closing the terminal after use

Video.release()
cv2.destroyAllWindows()


