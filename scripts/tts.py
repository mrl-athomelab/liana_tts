#!/usr/bin/env python

import rospy
import setproctitle
import requests
import base64
import time
import playsound
import os
from liana_tts.srv import Liana

topic_name = 'liana_tts'
tts_server = 'http://localhost:8585'

setproctitle.setproctitle('ros_{}'.format(topic_name))


def send_request(text_to_speech):
    r = requests.get("{}/tts?text={}".format(tts_server, text_to_speech))
    r = r.json()
    return r


def say(text):
    resp = send_request(text)
    if resp["status"] == "ok":
        content = resp["content"]
        content = base64.b64decode(content)

        file_name = 'voice_{}.mp3'.format(int(time.time()))
        with open(file_name, 'wb') as f:
            f.write(content)

        playsound.playsound(file_name, True)

        os.remove(file_name)
    else:
        print resp["message"]


def service_handler(req):
    text = req.input
    say(text)
    return 'ok'


rospy.loginfo("Initializing node ...")
rospy.init_node(topic_name)

rospy.loginfo("Ready to say anything !")
rospy.Service('/{}/say'.format(topic_name), Liana, service_handler)

try:
    rospy.spin()
except KeyboardInterrupt:
    rospy.logwarn("Shutting done ...")