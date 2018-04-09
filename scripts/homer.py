import rospy
from std_msgs.msg import String

_publisher = rospy.Publisher('/robot_face/text_out', String, queue_size=10)
_finisher = rospy.Publisher('/robot_face/talking_finished', String, queue_size=10)


def say(text):
    _publisher.publish(text)
    _finisher.publish('')


def change_face(mode):
    _publisher.publish(mode)
    _finisher.publish('')
