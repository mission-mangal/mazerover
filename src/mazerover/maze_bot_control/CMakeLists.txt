cmake_minimum_required(VERSION 3.0.2)
project(maze_bot_control)

find_package(catkin REQUIRED
  COMPONENTS
  roscpp
  nav_msgs
  geometry_msgs
  tf
)
file(GLOB_RECURSE sources scripts/*.py)

set(THIS_PACKAGE_INCLUDE_DIRS
  include
)

catkin_package(LIBRARIES
  INCLUDE_DIRS
  CATKIN_DEPENDS
  roscpp
  nav_msgs
  geometry_msgs
  tf
)

include_directories(${THIS_PACKAGE_INCLUDE_DIRS})
include_directories(SYSTEM ${catkin_INCLUDE_DIRS})

add_executable(mazerover_cpp src/mazerover.cpp)
target_link_libraries(mazerover_cpp ${catkin_LIBRARIES})


## Example programs
add_executable(example_get_position_cpp examples/get_position.cpp)
target_link_libraries(example_get_position_cpp ${catkin_LIBRARIES})

add_executable(example_velocity_control_cpp examples/velocity_control.cpp)
target_link_libraries(example_velocity_control_cpp ${catkin_LIBRARIES})

#add_executable(example_velocity_control_cpp examples/velocity_control.cpp)
#target_link_libraries(example_velocity_control_cpp ${catkin_LIBRARIES})


catkin_python_setup()

catkin_install_python(
  PROGRAMS ${sources} src/mazerover_py examples/example_get_position_py examples/example_velocity_control_py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
