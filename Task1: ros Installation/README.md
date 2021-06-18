# Task1: Robot operating system installation and configuration

This task focuses on the process of installing the ROS (Robot Operating System) software and its packages on a 64-bit computer system.

## First Introduction:-
 
 This installation and configuration process used VMware virtual machine (VMware® Workstation 16 Pro) integrated with ROS Noetic Ninjemys, which primarily targets Ubuntu 20.04 (Focal) release.

   *Virtual machine (VMware® Workstation 16 Pro) minimum system requirements:*

   A compatible 64-bit x86/AMD64 CPU launched in 2011 or later *
   1.3GHz or faster core speed.
   2GB RAM minimum/ 4GB RAM or more recommended.
   General Host OS Requirements.
   VMware Workstation Pro and Player run on most 64-bit Windows or Linux host operating systems: Windows 10. Windows Server 2019.

   *Ubuntue (Version 20.04) minimum system requirements:*
   2 GHz dual core processor.
   4 GiB RAM (system memory)
   25 GB of hard drive space (or USB stick, memory card or external drive but see LiveCD for an alternative approach)


## Second Download Softwares:-

After fulfilling system requirements, the second task to install ROS noetic is to download & install a virtual machine software and to select an OS for ROS. Here, I'll provide the links to download and install VMware® Workstation 16 Pro & Ubuntu 20.04.

Download Ubuntu Desktop: https://ubuntu.com/download/desktop

Download VMware Workstation Pro: https://www.vmware.com/mena/products/workstation-pro/workstation-pro-evaluation.html


## Third Download & Configure ROS Noetic:-

After installing your Ubuntu software, open the terminal, and download Python3 using the command for any version you wish, I choose 3.8:
```
sudo apt install python3.8
```

Set up your computer to accept software from packages.ros.org Through the following command:
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Now Set up your keys:
```
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
Then, update your Ubuntu/Linux built-in packages and select to install your ROS version:
```
sudo apt update
```
*Desktop-Full Install: (Recommended): Everything in Desktop plus 2D/3D simulators and 2D/3D perception packages*
```
sudo apt install ros-noetic-desktop-full
```
*or Desktop Install: Everything in ROS-Base plus tools like rqt and rviz*
```
sudo apt install ros-noetic-desktop
```
*or ROS-Base: (Bare Bones) ROS packaging, build, and communication libraries. No GUI tools.*
```
sudo apt install ros-noetic-ros-base
```
Now You must source this script in every bash terminal you use ROS in
```
source /opt/ros/noetic/setup.bash

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
Finally, To install this tool and other dependencies for building ROS packages, run:
```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```
Also, if you have not yet installed rosdep, do so as follows.
```
sudo apt install python3-rosdep
```

Congragulation, you have installed ROS noetic successfully. You may check the following commands to interact with ROS:

```
roscore: Starts the ROS master process
roslaunch: Launches nodes described in a launch script
rosnode list: Shows a list of running nodes.
rostopic list: Shows a list of published topics
rostopic echo /topic: Echos the topic given
rostopic pub /topic type data: Publishes data, example: rostopic pub /hello std_msgs/String “Hello”
rosparam list: Lists parameters
rosparam set parameter_name value: Sets parameters
rosparam get parameter_name: Gets a parameter value
rosversion -d: Lists version of ROS
roslaunch ros_pkg_name launch_file_name: Calls a launch script, ex: roslaunch roscpp_tutorials talker_listener.launch
rosrun ros_pkg_name node_name: Starts a ros node.
*Source: Prof. J Gobbert AAE 490 IAR: Spring 2020*
```
Now, there are a few packages and tools to add on ROS to be able to complete this track.

Therefore, let's download and run the catkin tool. Open the terminal and run the following commands:
```
cd ~/catkin_ws/src
rosdep install --from-paths src --ignore-src -r -y
 sudo apt-get install ros-noetic-moveit
 sudo apt-get install ros-noetic-joint-state-publisher ros-noetic-joint-state-publisher-gui
 sudo apt-get install ros-noetic-gazebo-ros-control joint-state-publisher
 sudo apt-get install ros-noetic-ros-controllers ros-noetic-ros-control
```
Install catkin python tools:
```
 sudo apt install python3-osrf-pycommon
 sudo apt install python3-catkin-tools
```
Make sure that ROS is running on another terminal and then go back to the folder, initiate, and compile the tool:
```
cd ~/catkin_ws

catkin init

catkin_make
```

We are almost done. Clone the robot arm and launch it (roscore must be running at this point), as follows:
```
git clone https://github.com/smart-methods/arduino_robot_arm 

source /home/user/catkin_ws/devel/setup.bash

roslaunch robot_arm_pkg check_motors.launch

```

Install git to clone the arm folder, if didn't, using the command:
```
sudo apt install git

```

Congratulations, We are done. Your final screen should look like this:

![image](https://user-images.githubusercontent.com/77699294/122617269-9b0d2800-d094-11eb-9ee7-f1b137302889.png)
