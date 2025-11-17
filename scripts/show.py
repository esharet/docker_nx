import cv2
import numpy as np

# Create a black image of size 400x400
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a blue circle at the center
cv2.circle(img, center=(200, 200), radius=100, color=(255, 0, 0), thickness=-1)

# Draw a green rectangle
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), thickness=5)

# Put some text
cv2.putText(img, 'Hello OpenCV!', (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Show the image in a window
cv2.imshow('My Image', img)

# Wait for any key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
