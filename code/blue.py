import cv2
import numpy as np

def blue(camera):
    # Inside your capture loop after capturing the image
    image_data = camera.image_array
    hsv_image = cv2.cvtColor(image_data, cv2.COLOR_RGB2HSV)

    # Define the color ranges in HSV
    blue_lower = np.array([110, 150, 50])
    blue_upper = np.array([130, 255, 255])
    # Add more colors as needed

    # Create a mask for each color
    blue_mask = cv2.inRange(hsv_image, blue_lower, blue_upper)
    # Add more masks for other colors as needed

    # Find contours for the red dots
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Do the same for other colors

    # Define a threshold area for the dots
    dot_area_threshold = 100

    for contour in blue_contours:
        area = cv2.contourArea(contour)
        if area > dot_area_threshold:
            print("Blue detected")