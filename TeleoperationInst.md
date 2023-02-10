# Follow these instructions for operating the rover in the teleoperation mode

## In this mode of operation the operator has to move the rover using the following keyboard keys:
```md
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
anything else : stop

CTRL-C to quit

```

## To launch the teleoperation simulation, please run the below command in the  mazerover_ws workspace after sourcing the workspace(If you need help in this, please refer to [InstallationInstructions](InstallationInstructions.md) for setting up and souring(Step 5) the workspace).

```bash
roslaunch maze_bot_control  teleoperation.launch
```

## For more information about the package please refer the link [Teleop Twist Keyboard](http://wiki.ros.org/teleop_twist_keyboard)
