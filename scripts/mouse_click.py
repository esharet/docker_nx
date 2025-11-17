import cv2
import numpy as np

#!/usr/bin/env python3

WIDTH, HEIGHT = 800, 600
WINDOW_NAME = "mouse_draw"

def on_mouse(event, x, y, flags, img):
    # Draw a small filled circle on left button click
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 4, (0, 255, 0), -1)
        cv2.imshow(WINDOW_NAME, img)

def main():
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)  # black image
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(WINDOW_NAME, img)
    cv2.setMouseCallback(WINDOW_NAME, on_mouse, img)

    while True:
        key = cv2.waitKey(1) & 0xFF
        # press 'q' or ESC to quit
        if key == ord('q') or key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()