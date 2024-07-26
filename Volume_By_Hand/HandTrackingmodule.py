# Importing the Important Libraries

import cv2
import mediapipe as mp
import time


class handdetector():
    # Self means providing it the value by the user
    def __init__(self , mode=False, maxHands= 2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon



        # Using the Mediapipe framework

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
    static_image_mode=self.mode,
    max_num_hands=self.maxHands,
    min_detection_confidence=self.detectionCon,
    min_tracking_confidence=self.trackCon
)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self , img , draw=True):

        #Converting the original video to RGB

        imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.results = self.hands.process(imgRGB)  # This will process the frame for us and give the result

    # Detects if there is an the hand in the webcam or not
    # Multi_hand  can also can be detected

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)  # mpHands.HAND_CONNECTIONS Basically connect all the hand points
        return img
    
    def findPosition(self, img , handNo=0, draw=True):
        lmlist = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]


        # This line show the coordinates of each landmark in x,y,z

            for id, lm in enumerate(myHand.landmark):


                
                h, w, c = img.shape  # Height , width , channel of the inage
                
                # For finding the position of the center cx,cy are the center position
                cx, cy = int(lm.x * w), int(lm.y * h)  # x and y here are the coordinates of landmark
                #print(id, cx, cy)
                lmlist.append([id,cx,cy])

                if draw:

                
                # Detecting the id:0 of landmark and circling it
                # Basically  tracking particular lm id in hand
                
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            
        return lmlist





def main():
    past_Time = 0
    current_Time = 0

    # Code to capture/Run the Webcam Continues unless break key
    # Saving the Webcam Video in an variable

    Video = cv2.VideoCapture(0)
    detector = handdetector()

    while True:
        success, img = Video.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        if len(lmlist) != 0:
            print(lmlist[4]) # This will give the desired point from the 21 hand points
        
        
        # Defining the FPS

        current_Time = time.time()
        fps = 1 / (current_Time - past_Time)
        past_Time = current_Time

        # Displaying the fps on Screen And font,size ETC

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        # showing the webcam video

        cv2.imshow("WebCam", img)

        # important line to break the webcam terminal after pressing any key

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # For closing the terminal after use

    Video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()
