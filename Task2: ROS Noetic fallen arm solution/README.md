# Task1: ROS Noetic fallen arm solution

This task focuses on the process of fixing the fallen arm issue of ROS Noetic version.

## First Problem:-
 
 You may faced the following issue while running 
 ```
 roslaunch robot_arm_pkg check_motors.launch
 ```
 => "ERROR: cannot launch node of type [robot_state_publisher/state_publisher]: Cannot locate node of type [state_publisher] in package [robot_state_publisher]. Make sure file exists in package path and permission is set to executable (chmod +x)"
 
with the following screen


 
 Where in the new Noetic version, state_publisher was a deprecated alias for the node named robot_state_publisher. It was removed in https://github.com/ros/robot_state_publisher/pull/87 which is included in the ROS Noetic release of that package.


## Second Solution:-

Therefore, the solution is to change the type of the publishing package from type="state_publisher" to type="robot_state_publisher". To do that follow the following commands.

1- Nevigate to the check_motors.launch file inside your cloned arduino_robot_arm file

```
cd ~/catkin_ws/src/arduino_robot_arm/robot_arm_pkg/launch

```

2- Open the check_motors.launch file with any file editor tool, and change type="state_publisher" to type="robot_state_publisher".


3- run again

 ```
 roslaunch robot_arm_pkg check_motors.launch
 ```

Congragulations, your final screen should be like this:



