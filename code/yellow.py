import cv2
import numpy as np

def yellow(camera):
    # Inside your capture loop after capturing the image
    image_data = camera.image_array
    hsv_image = cv2.cvtColor(image_data, cv2.COLOR_RGB2HSV)

    yellow_lower = np.array([20, 100, 100]) 
    yellow_upper = np.array([30, 255, 255])

    # Create a mask for each color
    yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)  # Yellow mask

    # Add more masks for other colors as needed

    # Find contours for the yellow dots
    yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Yellow contours

    # Define a threshold area for the dots
    dot_area_threshold = 100

    for contour in yellow_contours:
        area = cv2.contourArea(contour)
        if area > dot_area_threshold:
            # Take action for red dot
            print("Yellow dot detected")
