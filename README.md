# Maze rover
### Installation

```
git clone https://github.com/mission-mangal/mazerover.git
cd mazerover
catkin init
catkin build
sudo apt install ros-noetic-leo-description ros-noetic-leo-gazebo-plugins
```



### Terminal 1
$ roslaunch maze_bot_control maze1.launch


### Terminal 2
$ rosbag record -a

### Terminal 3
$ roslaunch maze_bot_control teleoperation.launch



