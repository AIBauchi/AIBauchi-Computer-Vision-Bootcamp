import cv2

# Function to convert image to pencil sketch
def pencil_sketch(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    inverted_gray = 255 - gray
    
    # Apply Gaussian blur to the inverted grayscale image
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    
    # Invert the blurred image
    inverted_blurred = 255 - blurred
    
    # Create the pencil sketch image by blending the grayscale image and the inverted blurred image
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    
    return sketch

# Open a connection to the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to a pencil sketch
    sketch = pencil_sketch(frame)

    # Display the original frame and the pencil sketch frame
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Pencil Sketch Frame', sketch)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
