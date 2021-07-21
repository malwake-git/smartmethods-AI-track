# Task3: Robotic Radar using Simulated Navigation and Laser Network

This task focuses on the process of Nevigating Turtlebot3 using SLAM (Simultaneous Localization and Mapping) in ROS.

## First Introduction:-
 
 First, to complete the task, we used ROS Noetic version installed on Ubuntu 20.04, along with Turtlebot3. You may review task 1 and 2 for further details.
 
 The task consiste of:
 
 Using Turtlebot3 with the SLAM approach to create and nevigate the Turtlebot3 robot through the saved .yml map.
 
 
 The following tools were needed to run and complete the task. Please make sure to install them beforehand:
 
 - Gazebo (http://gazebosim.org/tutorials?tut=ros_installing)
 - Rviz (http://wiki.ros.org/rviz)
 - Catkin (Added by default with ROS Noetic complete package)
 - Turtlebo3 file cloned and packages.

## Second Using Turtlebot3 with the SLAM approach to create and nevigate the Turtlebot3 robot through the map:-

The steps for this task were simple. The following website provides, in detail, all the necessary steps to complete the task. Please review section 6.3:
https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/

Furthermore, I will illustrate some of the necessary steps in the following:

- After making sure that ROS Noetic & Turtlebot3 are installed and working, Run the Rviz from the previously saved map:

```
// You may choose any Turtlebot3 model installed

// Gazebo
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch

// Rviz
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```
- Estimate Initial Pose from the steps:
1- Click the 2D Pose Estimate button in the RViz menu.
2- Click on the map where the actual robot is located and drag the large green arrow toward the direction where the robot is facing.
3- Repeat step 1 and 2 until the LDS sensor data is overlayed on the saved map.

You may also, Launch keyboard teleoperation node to precisely locate the robot on the map.
```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
4- Move the robot back and forth a bit to collect the surrounding environment information and narrow down the estimated location of the TurtleBot3 on the map which is displayed with tiny green arrows.


Set Navigation Goal Steps:

1- Click the 2D Nav Goal button in the RViz menu.
2- Click on the map to set the destination of the robot and drag the green arrow toward the direction where the robot will be facing.

Some helpful tips:
- This green arrow is a marker that can specify the destination of the robot.
- The root of the arrow is x, y coordinate of the destination, and the angle θ is determined by the orientation of the arrow.
- As soon as x, y, θ are set, TurtleBot3 will start moving to the destination immediately.


Finally, you can download the map again with the following commands:
```
rosrun map_server map_saver -f $(rospack find evarobot_navigation)/map/ma

# Ex. rosrun map_server map_saver -f ~/map
```
![map (1)2](https://user-images.githubusercontent.com/77699294/123520089-af19e080-d6b7-11eb-8dc5-1c3716f39129.jpg)

