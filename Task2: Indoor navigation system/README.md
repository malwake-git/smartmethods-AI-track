# Task1: Indoor navigation system for mobile robot design and implementation

This task focuses on the process of running SLAM (Simultaneous Localization and Mapping) using emulated robotics machine in ROS.

## First Introduction:-
 
 First, to complete the task, we used ROS Noetic version installed on Ubuntu 20.04. You may review task 1 for further instruction.
 
 The task consisted of two parts:
 
 1- Using Turtlebot3 with the SLAM approach to create and save a map.
 2- Using Evarobot with the SLAM approach to create and save a map.
 
 The following tools were needed to run and complete the task. Please make sure to install them beforehand:
 
 - Gazebo (http://gazebosim.org/tutorials?tut=ros_installing)
 - Rviz (http://wiki.ros.org/rviz)
 - Catkin (Added by default with ROS Noetic complete package

## Second Using Turtlebot3 with the SLAM approach to create and save a map:-

The steps for this task were simple. The following website provides, in detail, all the necessary steps to complete the task. Please review section 3 & 6:
https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/#overview

Furthermore, I will illustrate some of the necessary steps in the following:

- After making sure that ROS Noetic is installed, try to install all the dependant ROS packages:

```
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```
- Now install TurtleBot3 ROS packages:
```
$ sudo apt install ros-noetic-dynamixel-sdk
$ sudo apt install ros-noetic-turtlebot3-msgs
$ sudo apt install ros-noetic-turtlebot3
```
- Then, all you need to do is to install TurtleBot3 Simulation Packages and compile them as the following:
```
$ cd ~/catkin_ws/src/
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make
```
You can run the Gazeboo, Rviz, and slam launch files for testing:
```
# Gazeboo
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

#SLAM
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```
Now, you may encounter similar to screens:

![week2(1)](https://user-images.githubusercontent.com/77699294/123518375-42e6af00-d6ae-11eb-9045-a09530f74557.png)

![week2](https://user-images.githubusercontent.com/77699294/123518392-598d0600-d6ae-11eb-9a1b-73e202f3b5e5.png)

Now you can communicate and move the turtlebot3 through the teleportation node:
```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
![week2(2)](https://user-images.githubusercontent.com/77699294/123518376-48dc9000-d6ae-11eb-988a-189d99117f00.png)

Also, you can save the initiated map through the command:
```
rosrun map_server map_saver -f ~/map
```
![map](https://user-images.githubusercontent.com/77699294/123518441-9ce77480-d6ae-11eb-80d9-630d242e0f76.jpg)

## Third Using Evarobot with the SLAM approach to create and save a map:-

The following website provides all the necessary steps to complete the task. Please review the following links:
- http://wiki.ros.org/Robots/evarobot
- https://github.com/inomuh/evarobot


Moreover, we will go through the steps in here to clarify some hidden concepts and ideas about this task.

First, let's go on and install some needed packages for the task
```
sudo apt update

sudo apt install ros-noetic-joint-state-publisher-gui

sudo apt install ros-neotic-robot-state-publisher
```
In order for the "joint_state_controller" to work, "joint_state_controller_gui" package must be downloaded
```
sudo apt install ros-noetic-ros-controllers
```
Download "driver_base package
```
cd ~/catkin_ws/src

git clone https://github.com/ros-drivers/driver_common -b indigo-devel

```
Download "interactive marker twist server" package
```
cd ~/catkin_ws/src

git clone https://github.com/ros-visualization/interactive_marker_twist_server -b kinetic-devel
```
Download "slam_gmapping" package
```
cd ~/catkin_ws/src

git clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel

sudo apt-get install ros-noetic-openslam-gmapping

sudo apt-get install ros-noetic-slam-gmapping
```
In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded. If the command didn't work please reveiw the following links: http://wiki.ros.org/gazebo_ros_pkgs
```
sudo apt-get install ros-noetic-gazebo-ros-pkgs
```
In order for the navigation tools to work properly, "ros-navigation" must be downloaded
```
sudo apt-get install ros-noetic-ros-navigation
```
Now, download evarobot packages:
```

```





