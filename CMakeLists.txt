cmake_minimum_required(VERSION 2.8.3)
project(liana_tts)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_service_files(
  FILES
  Liana.srv
)

generate_messages()

catkin_package()