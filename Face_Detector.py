import cv2

#load some pre-trained dara on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose an image to detect face in 
#img = cv2.imread('johnny-depp.jpg')

# Capture video from webcam (0 means it is gonna get your default webcam)
webcam = cv2.VideoCapture(0)

#Iterate forever over frames
while True:
    
    #read the current frame
    succesful_frame_read, frame = webcam.read()
    #Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    #Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(frame)
    # Draw rectnagles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.imshow('Smart Programmer Face Detector', frame)
    cv2.waitKey(1)
    
    #stop if Q key is pressed 
    #if key==81 or key==113:
     #   break
     
    #relase the VideoCapture objet
   # webcam.release()



#Finding cordinates of picture 
#print(face_coordinates)


