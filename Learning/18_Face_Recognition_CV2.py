#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 需要先安装cmake 不然dlib安装不了
# pip install cmake
# pip install face_recognition
# pip install dlib

# face_recognition --show-distance true --tolerance 0.5 know_people unknow_people

import cv2
import numpy as np
import face_recognition


def normal_usage():
    image1 = face_recognition.load_image_file("/Users/zhangxin/Desktop/know_people/renxianqi.jpg")
    image2 = face_recognition.load_image_file("/Users/zhangxin/Desktop/know_people/guofucheng.jpg")
    image3 = face_recognition.load_image_file("/Users/zhangxin/Desktop/know_people/gutianle.jpg")

    unknown_image = face_recognition.load_image_file("/Users/zhangxin/Desktop/unknow_people/gutianle.jpeg")
    print(face_recognition.face_locations(unknown_image))
    print(face_recognition.face_landmarks(unknown_image))

    # 获取每个图像文件中每个面部的面部编码
    # 由于每个图像中可能有多个面，所以返回一个编码列表。
    # 但是由于我知道每个图像只有一个脸，我只关心每个图像中的第一个编码，所以我取索引0。
    encoding1 = face_recognition.face_encodings(image1)[0]
    encoding2 = face_recognition.face_encodings(image2)[0]
    encoding3 = face_recognition.face_encodings(image3)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    known_faces = [
        encoding1,
        encoding2,
        encoding3
    ]

    # 结果是True / false的数组，未知面孔known_faces阵列中的任何人相匹配的结果
    results = face_recognition.compare_faces(known_faces, unknown_encoding, 0.5)
    print(results)

    # 人脸的差异数值
    print(face_recognition.face_distance(known_faces, unknown_encoding))

    print("这个未知面孔是 renxianqi 吗? {}".format(results[0]))
    print("这个未知面孔是 guofucheng 吗? {}".format(results[1]))
    print("这个未知面孔是 gutianle 吗? {}".format(results[2]))
    print("这个未知面孔是 我们从未见过的新面孔吗? {}".format(not True in results))


def capture_face():
    # 打开摄像头
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("/Users/zhangxin/Desktop/235694.png")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("/Users/zhangxin/Desktop/235694.png")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [
        obama_face_encoding,
        biden_face_encoding
    ]
    known_face_names = [
        "zhangxin",
        "Joe Biden"
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        # 图片大小对性能影响比较大，需要缩小
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        # 经过测试来看，BGR也可以识别人脸，但是特定角度可能不行
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    normal_usage()
    capture_face()
