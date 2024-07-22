import cv2

# Open a connection to the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the threshold value
threshold_value = 127
max_value = 255

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply the binary threshold
    _, thresholded_frame = cv2.threshold(gray_frame, threshold_value, max_value, cv2.THRESH_BINARY)

    # Display the original frame and the thresholded frame
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Thresholded Frame', thresholded_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
