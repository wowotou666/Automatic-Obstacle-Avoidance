from AlphaBot import AlphaBot
import numpy as np
import cv2
import math
import time

Ab = AlphaBot()
Ab.stop()
cap = cv2.VideoCapture(0)
while True:
    # Read in and grayscale the image
    ret, image = cap.read()
    cap.release()
    cap = cv2.VideoCapture(0)
    image = cv2.resize(image, (600, 600))
    cv2.imwrite('./input.jpg',image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    equ = cv2.equalizeHist(gray)
    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(equ, (kernel_size, kernel_size), 0)

    # Define our parameters for Canny and apply
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    cv2.imwrite('./edges.jpg',edges)
    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 1
    theta = np.pi / 180
    threshold = 100
    min_line_length = 60
    max_line_gap = 30
    line_image = np.copy(image) * 0  # creating a blank to draw lines on
    x = 0
    tup_1 = []
    tup_2 = []
    sum_1 = 0
    sum_2 = 0
    # Run Hough on edge detected image
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

    # Iterate over the output "lines" and draw lines on the blank


    for line in lines:
        print(lines)
        num = len(lines)
        print(num)
        for x1, y1, x2, y2 in line:

            angle = math.atan2(y2 - y1, x2 - x1)
            angle = angle / math.pi * 180
            cv2.line(image,(x1,y1),(x2,y2),(255,0,0),10)
            if abs(angle)<85:
                if angle > 0:
                    tup_1.append(angle)
                if angle < 0:
                    tup_2.append(angle)
        print(tup_1)
        print(tup_2)
    len_1 = len(tup_1)
    len_2 = len(tup_2)
    cv2.imwrite('./output.jpg',image)
    if len_1 != 0 and len_2 != 0:

        for i in range(len_1):
            sum_1 = tup_1[i] + sum_1
        for j in range(len_2):
            sum_2 = tup_2[j] + sum_2
            mean_1 = sum_1 / len_1
            mean_2 = sum_2 / len_2
            print("more than  zero ", mean_1)
            print("less than  zero ", mean_2)
    elif len_1 != 0 and len_2 == 0:
        len_1 = len(tup_1)

        for i in range(len_1):
            sum_1 = tup_1[i] + sum_1

            mean_1 = sum_1 / len_1
            mean_2 = 0
            print("more than  zero ", mean_1)
            print("less than  zero ", mean_2)
    elif len_1 == 0 and len_2 != 0:

        len_2 = len(tup_2)

        for j in range(len_2):
            sum_2 = tup_2[j] + sum_2
            mean_1 = 0
            mean_2 = sum_2 / len_2
            print("more than  zero ", mean_1)
            print("less than  zero ", mean_2)
    elif len_1 == 0 and len_2 == 0:
        mean_1 = 0
        mean_2 = 0
        print("more than  zero ", mean_1)
        print("less than  zero ", mean_2)

    if (round(round(-20) <= mean_1 + mean_2 <= round(20))):
        Ab.forward()
        time.sleep(0.2)
        Ab.stop()
        time.sleep(0.1)
    if (round(round(-20) > mean_1 + mean_2)):
        Ab.right()
        time.sleep(0.2)
        Ab.stop()
        time.sleep(0.1)
    if (round(round(20) < mean_1 + mean_2)):
        Ab.left()
        time.sleep(0.2)
        Ab.stop()
        time.sleep(0.1)
