import cv2
import numpy as np


hand_cascade = cv2.CascadeClassifier('C:\\Users\\paart\\OneDrive\\Documents\\GitHub\\computer-vision\\haarcascade_hand.xml')

def count_fingers(hand_roi):
    # Convert the region of interest (ROI) to grayscale
    gray = cv2.cvtColor(hand_roi, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        return 0  # No fingers detected
    
    # Find the contour with the largest area (assuming it's the hand)
    max_contour = max(contours, key=cv2.contourArea)
    
    # Find the convex hull of the hand contour
    hull = cv2.convexHull(max_contour, returnPoints=False)
    
    # Use the convexity defects to count fingers
    defects = cv2.convexityDefects(max_contour, hull)
    finger_count = 0
    
    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(max_contour[s][0])
            end = tuple(max_contour[e][0])
            far = tuple(max_contour[f][0])

            # Use cosine rule to find the angle of the defect
            a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            angle = np.arccos((b**2 + c**2 - a**2) / (2*b*c))

            # If the angle is less than 90 degrees, it's a finger
            if angle < np.pi/2:
                finger_count += 1
    
    return finger_count

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect hands in the frame
    hands = hand_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        hand_roi = frame[y:y + h, x:x + w]
        finger_count = count_fingers(hand_roi)
        cv2.putText(frame, f"Fingers: {finger_count}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    cv2.imshow('Finger Count', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
