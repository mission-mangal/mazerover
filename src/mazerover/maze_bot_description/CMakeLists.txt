cmake_minimum_required(VERSION 3.0.2)
project(maze_bot_description)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY
    launch
    models
    urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)