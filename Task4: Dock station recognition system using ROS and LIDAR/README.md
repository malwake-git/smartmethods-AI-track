# Task4: Dock station recognition system using ROS and LIDAR

This task focuses on the process of writing a python script that publishes to /move_base_simple/goal topic. Furthermore, the task is an extension from the previous mission with the implementation of ROS power of connecting python scripts to Rviz & Gazebo (Nodes).

## First Introduction:-
 
 First, to complete the task, we used ROS Noetic version installed on Ubuntu 20.04. You may review tasks 1 2 & 3 for further instruction.
 
 The task consisted of creating a python script inside a newly created compiled package, in order to control and guide (Subscribe nodes) Turtlebot3 to a certain position (defined in move_base_simple.py).
 
 The following tools were needed to run and complete the task. Please make sure to install them beforehand:
 
 - Gazebo (http://gazebosim.org/tutorials?tut=ros_installing)
 - Rviz (http://wiki.ros.org/rviz)
 - Catkin (Added by default with ROS Noetic complete package)

## Script Run and Results:-

After launching Gazebo, Rviz, and Roscore from the previous saved map in task3.

```
# Gazebo
$ export TURTLEBOT3_MODEL=burger
$ roslaunch evarobot_simulation evarobot_gazebo_emptyworld.launch

# Rviz
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
```

- Now running the script while echoing the result in a different terminal:

```
$ python3 move_base_simple.py

$ rostopic echo move_base_simple/goal
```
The result on Rviz & terminal:

![Task4](https://user-images.githubusercontent.com/77699294/126635364-c2d6760c-f76b-4037-82cb-944a82d7a060.png)


![Task4-1](https://user-images.githubusercontent.com/77699294/126635371-2d26d12b-6ae3-4d8f-8dbe-7ebf7ea81a4a.png)


![task4-2](https://user-images.githubusercontent.com/77699294/126635375-34d372b1-4eba-43ea-8479-33f96b2705a4.png)

*Note: The code is time-based with a 1ms delay. The code was mainly inspired by ROS ANSWERS (https://answers.ros.org/question/306582/unable-to-publish-posestamped-message/).
