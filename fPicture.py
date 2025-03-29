import cv2
def takephoto(photoname):
# Open the default camera (usually device 0 for the built-in webcam)
    camera = cv2.VideoCapture(0)

# Check if the camera is opened correctly
    if not camera.isOpened():
        print("Error: Could not open webcam.")
        exit()

# Capture a single frame
    ret, frame = camera.read()

# If frame is read correctly, save it
    if ret:
    # Save the captured image
        cv2.imwrite(photoname, frame)
        print("Image saved successfully!")
    else:
        print("Error: Could not read frame.")

# Release the camera
    camera.release()
    return