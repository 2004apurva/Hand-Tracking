# Importing OpenCV library
import cv2

# Reading the video from Webcam
video = cv2.VideoCapture(0)

# While Conditon is used in videos because it contain multiple frame
while True:
    # Capture frame-by-frame
    success , img =video.read()

    # Display the video 
    cv2.imshow("Video", img)

    # Waitkey will open the image tab until an button is pressed
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        
        break

# When everything is done, release the capture
video.release()
cv2.destroyAllWindows()

