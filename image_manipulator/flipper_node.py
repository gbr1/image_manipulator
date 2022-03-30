#
# The MIT License
#
# Copyright (c) 2022 Giovanni di Dio Bruno https://gbr1.github.io
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge

class FlipperNode(Node):

    def __init__(self):
        self.cv_bridge = CvBridge()
        super().__init__('flipper_node')

        self.declare_parameter('flip_vertical', False)
        self.declare_parameter('flip_horizontal', False)

        self.flip_vertical = self.get_parameter('flip_vertical').get_parameter_value().bool_value
        self.flip_horizontal = self.get_parameter('flip_horizontal').get_parameter_value().bool_value

        self.publisher = self.create_publisher(Image, '/image/flipped', 1)
        self.subscription = self.create_subscription(Image,'/image/raw',self.listener_callback,1)
        self.subscription


    def listener_callback(self, msg):
        current_frame = self.cv_bridge.imgmsg_to_cv2(msg,"bgr8")
        if self.flip_vertical and self.flip_horizontal:
            current_frame = cv2.flip(current_frame,-1)
        elif self.flip_vertical==True:
            current_frame = cv2.flip(current_frame,0)
        elif self.flip_horizontal==True:
            current_frame = cv2.flip(current_frame,1)
        #cv2.imshow('test',current_frame)
        #cv2.waitKey(1)
        self.publisher.publish(self.cv_bridge.cv2_to_imgmsg(current_frame,"bgr8"))


def main(args=None):
    rclpy.init(args=args)

    flipper_node = FlipperNode()

    rclpy.spin(flipper_node)

    flipper_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()