#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def camera_publisher():
    rospy.init_node('camera_publisher', anonymous=True)
    rate = rospy.Rate(10)

    # Inicjalizacja obiektu CvBridge
    bridge = CvBridge()

    # Inicjalizacja kamer (dla uproszczenia przyjmujemy, że są podłączone pod indeksami 0, 1, 2)
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    cap3 = cv2.VideoCapture(2)

    # Publikowanie obrazów z kamer
    pub1 = rospy.Publisher('camera1/image_raw', Image, queue_size=10)
    pub2 = rospy.Publisher('camera2/image_raw', Image, queue_size=10)
    pub3 = rospy.Publisher('camera3/image_raw', Image, queue_size=10)

    while not rospy.is_shutdown():
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        ret3, frame3 = cap3.read()

        if ret1:
            pub1.publish(bridge.cv2_to_imgmsg(frame1, "bgr8"))
        if ret2:
            pub2.publish(bridge.cv2_to_imgmsg(frame2, "bgr8"))
        if ret3:
            pub3.publish(bridge.cv2_to_imgmsg(frame3, "bgr8"))

        rate.sleep()

    # Zatrzymanie kamer i zamknięcie okna
    cap1.release()
    cap2.release()
    cap3.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_publisher()
    except rospy.ROSInterruptException:
        pass
