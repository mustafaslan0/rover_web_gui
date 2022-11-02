#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import os
import subprocess
  
def callback(data):
      
    # print the actual message in its raw format
    rospy.loginfo("Here's what was subscribed: %s", data.data)
    if(data.data == "autonomy"):
        subprocess.call(['Terminator-terminal', '-x', '~/Desktop/redgiant_ws/src/rover_gui/scripts/autonomy.sh'])
    elif(data.data == "artag"):
        os.system("gnome-terminal -- '~/Desktop/redgiant_ws/src/rover_gui/scripts/tag.sh'")
        # subprocess.call(['gnome-terminal', '-x', '~/Desktop/redgiant_ws/src/rover_gui/scripts/tag.sh'])


  
  
def main():
      
    # initialize a node by the name 'listener'.
    # you may choose to name it however you like,
    # since you don't have to use it ahead
    rospy.init_node('command', anonymous=True)
    rospy.Subscriber("/command_gui", String, callback)
      
    # spin() simply keeps python from
    # exiting until this node is stopped
    rospy.spin()
  
if __name__ == '__main__':
      
    # you could name this function
    try:
        main()
    except rospy.ROSInterruptException:
        pass