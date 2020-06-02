#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install opencv-python

import cv2
import numpy as np
import face_recognition


# BGR使用是需要转RGB
def open_camera():
    cap = cv2.VideoCapture(0)

    for i in range(0, 19):
        print(cap.get(i))

    while True:
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        print(face_recognition.face_locations(rgb_small_frame))

        # print(frame.shape)
        print(frame.size)
        #
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #
        # lower_blue = np.array([100, 47, 47])
        # upper_blue = np.array([124, 255, 255])
        #
        # mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 蓝色掩模
        #
        # res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow(u"Capture", frame)
        # cv2.imshow(u"mask", mask)
        # cv2.imshow(u"res", res)

        key = cv2.waitKey(1)
        if key & 0xff == ord('q') or key == 27:
            print(frame.shape, ret)
            break
    cap.release()
    cv2.destroyAllWindows()


def operate_RGB():
    img = cv2.imread("/Users/zhangxin/Desktop/4.png")

    # numb = img[50, 100]
    # print(numb)
    #
    # img[50, 100] = (0, 0, 255)

    img[0:100, 100:200, 0] = 255
    img[100:200, 200:300, 1] = 255
    img[200:300, 300:400, 1] = 255

    cv2.imshow("img", img)
    cv2.waitKey()


if __name__ == "__main__":
    open_camera()
    # operate_RGB()
