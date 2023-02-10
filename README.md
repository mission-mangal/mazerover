# Maze rover
### Installation

```
sudo apt install python3-rosdep python3-catkin-tools xterm
git clone https://github.com/mission-mangal/mazerover.git
cd mazerover
catkin init
catkin build
sudo apt install ros-noetic-leo-description ros-noetic-leo-gazebo-plugins
```



### Terminal 1
$ roslaunch maze_bot_control maze1.launch


### Terminal 2
$ rosbag record -o rosbag /cmd_vel /collision  /joint_states /ground_truth /tf /tf_static /rosout

### Terminal 3
$ roslaunch maze_bot_control teleoperation.launch


# For Docker users


