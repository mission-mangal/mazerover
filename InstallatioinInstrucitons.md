# Follow these instructions to setup the workspace for maze rover

1. First make sure you have cloned the repository from github, if not clone the repositiry using the below command in the termianl. (if you have downloaded the workspace in .zip format, please extract it, to follow the next series of steps)

```bash
sudo apt install python3-rosdep python3-catkin-tools
git clone https://github.com/mission-mangal/mazerover.git
```

2.  Once you have successfully cloned the repository, go inside the main folder of the workspace using the below command
```bash
cd mazerover_ws
```

3.  Run the below commands in the terminal to install all the dependencies and build the workspace

```bash
rosdep install -y --from-path src --ignore-src --rosdistro noetic
catkin build
```

4.  Once you have executed all the above commands successfully, please go to the next step, if there is any issue please try repeating the instructions from step 1 in a different location. But still if the problem persist, contact the coordinator near you for troubleshooting.

5.  This step is to source the workspace for all the executions, so using the below command to source the workspace.
```bash
source devel/setup.sh
```

6. Now this step will be to ensure that whether all the packages are configured properly, here this command will launch the simulation with the maze and a rover for the movement.

```bash
roslaunch maze_bot_gazebo maze_bot.launch
```


