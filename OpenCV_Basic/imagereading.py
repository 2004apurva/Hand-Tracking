# Importing OpenCV Library
import cv2

# Reading the photo and saving it in an variable
img = cv2.imread("./Face_Detection/Photos/cat.jpg")

# Setting an condition if the path is empty
if img is None:
    print("There is no Image ")

# Show the the image in different tab
else:
    cv2.imshow("Cat",img)
    
    # Waitkey will open the image tab until an button is pressed
    cv2.waitKey()
    # DestroyAllWindows will close the image tab after any button is pressed 
    cv2.destroyAllWindows()