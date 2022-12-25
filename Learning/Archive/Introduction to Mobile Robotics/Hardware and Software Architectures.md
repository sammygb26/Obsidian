# Hardware and Software Architectures
This will cover the robots get inputs from the outside world (**sensors**), a basic overview of what is needed to process this (**computing hardware**) and a basic software outline of how this is accomplished (**software architecture, decomposition**).

### Sensors
*Sensors* are devices that measure some property of the environment or some change to the environment. There are two types *exteroceptive* (external) and *proprioception* (internal).

![[Pasted image 20220926133208.png]]

### Exteroceptive

**RGB Cameras** - This is an essential for robot percepts as it has very *rich semantics* (a lot of data and context can be gleamed from this). These are compared on their *resolution*, *FOV* and *dynamic range* (difference between blackest black and brightest white). There is a trade for FOV, low FOV can see things far away much better while wide FOV pixels get spread further. 

Trend: HD, Wide dynamic range

**Stereo Cameras** - Here we have two cameras space apart. This mimics how binocular vision works in humans and allow the robot to generate a depth map of the surroundings.

**LiDAR** - This uses pulses of light clow or IR to detect how far away objects are. It generate a 3D point cloud for many different ancles from the car. This type of device is called a *transceiver* as it puts out and takes in some signal.

Trend: HD, low-cost and solid state

**mmWave Radar** - this uses lower frequency radiation to detect objects around the car. Furthermore the Doppler effect can be used to detect the speed of an object. 

Trend: single-chip, 4D imaging radar

**Ultrasonic/Sonar** - Measure the distance to objects using sound waves. This is short range but all lighting conditions work. Not generally used for self-driving cars as its not quick enough but used a lot for service robots.

### Proprioceptive

**GNSS & IMU** - *GNSS* or (Global Navigation Satellite Service) allows a car to tell where it is at a large scale in the world. This can provide position, velocity and heading. *IMU* - measure the angular and acceleration of itself and can be used to tell the angular rotation rate, acceleration and heading of out robot.

**Wheel Odometry** - This tracks the velocity and orientation with a rotary encoder and can be used to calculate overall speed and orientation of the car.

### Computing Hardware
All the information goes the the **Central Computer** which must use this to process and plan out what to do next. This takes a lot of hardware. *Service Robots* with simple environments can use basic computing hardware like RPi3/4 but autonomous cars need much more. 

Parallel specialized computers are used for heavy loads for example **GPUs** which are the most flexible, **FPGAs** (field programmable gate arrays) which are faster but less flexible needing the problem to be build in. Finally **ASICs** or Application Specific Integrate Chips which have the least flexibility but allow for the fastest speeds. This basically involves building how the problem is to be solved into the chip.

*Synchronized Hardware* - It is also important to make sure all the sensors and their readings and synchronized. Without this perfectly valid readings could be combined in a way that creates invalid readings. This is hard enough on one robot but many autonomous cars hope to link together. For this the internet and GPS are used using NTP time as a reference clock.

### Software Architecture
![[Pasted image 20220926135522.png]]
This is the basic architecture used. *Sensors* are used to perceive what is going on in the environment and so create a map of what we can see. What is have perceived is then used to modify out plan and ensure we follow rules. After this out plan is broken down into what changes we need to make the the actuator to actual change how the robot is moving to fit with the plan. Over this a *system supervisor* is used to ensure no erroneous or conflicting readings have been made.

##### Environment Pereption

![[Pasted image 20220926140128.png]]

In *environment perception* We take in the raw readings either from data we already have (HD road map) or exteroceptive sensors (LiDAR/Cameras/Radar) or out interoceptive sensors (GPS/IMU/Wheel Odometry) to perform the following.

1. **Localization** - where we are in the scene -> gives *Robot Position and 6DoF*
2. **Dynamic Object Detection** where moving objects are -> **Dynamic Object Tracking** how the move -> **Object Motion Prediction** how the objects will move -> gives *dynamic objects*
3. **Static Object Detection** things we know wont move giving a scene of *static objects*

##### Environment Mapping

![[Pasted image 20220926140901.png]]

*Object Tracks* and *LiDAR/Depth Cameras/Radar* are used to give a **occupancy grid map** which can either be 2D or 3D and describes what is where and what is empty in the environment. These are also used to generate a **Localization Map** of where we are relative to features placing us in some scene/context. Finally any *prior HD map* out position and any *static objects* are used to provide a **HD Road Map** which we can then perform planning with.

![[Pasted image 20220926142021.png]]

##### Motion Planning
This can often be broken down into three layers. The **Mission Planner**, then **Behavior Planner** and the **Local Planner**.

![[Pasted image 20220926142203.png]]

The *mission planner* may break down how the overall goal is to be achieved. This path is then used by the *behavior planner* to decide what is to be done next that is the action that will be taken. For example stop or turn left. This is then used by the *Local Planner* to give a **planned trajectory** of what the car is to do say for the next few seconds.

##### Controller
The planned trajectory and the actual position of the car are fed into controllers to decide how much to change the throttle, brake percentage ad steering angle actually affecting how the car moves.

![[Pasted image 20220926142655.png]]

##### System Supervisor
This overviews the system and ensures all the readings and plans don't have glaring failures in them. We can also have a *hardware supervisor* that monitors the sensors for failure conditions.

![[Pasted image 20220926142818.png]]

[[Hardware and Software Architectures Questions]]