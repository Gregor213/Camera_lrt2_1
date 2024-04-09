#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    try:
        bridge = CvBridge()
        # Konwersja obrazu ROS na obraz OpenCV
        image = bridge.imgmsg_to_cv2(msg, "bgr8")
        # Wyświetlenie obrazu
        cv2.imshow("Camera Feed", image)
        cv2.waitKey(1)
    except Exception as e:
        print(e)

def camera_subscriber():
    rospy.init_node('camera_subscriber', anonymous=True)
    rospy.Subscriber("camera1/image_raw", Image, image_callback)
    rospy.Subscriber("camera2/image_raw", Image, image_callback)
    rospy.Subscriber("camera3/image_raw", Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        camera_subscriber()
    except rospy.ROSInterruptException:
        pass
