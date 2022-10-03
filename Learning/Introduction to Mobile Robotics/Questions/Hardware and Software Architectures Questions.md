What are sensors? #flashcard #MOB #HardwareSoftwareArchitecture
	Sensors are devices that measure some property of the environment.

---
What are exteroceptive and interoceptive sensors? #flashcard #MOB #HardwareSoftwareArchitecture 
	Exteroceptive sensor are sensors which sense the outside environment (outside the robot) while interoceptive sensors sense the actual robot.

---
What are the 5 main exteroceptive sensors covered? #flashcard #MOB #HardwareSoftwareArchitecture 
	RGB Cameras, Stereo Cameras, LiDAR, mmWave Radar, ultrasonic sonar.

---
Why are RGB cameras used to widely? #flashcard #MOB #HardwareSoftwareArchitecture 
	RGB cameras are very useful as then can read a large amount of information about the scene, a lot is encoded in a single image.

---
What are the factors different RGB cameras are compared on? #flashcard #MOB #HardwareSoftwareArchitecture 
	FOV (field of view), Resolution (how many pixels) and dynamic range (difference between the brightest and dimmest colors the camera can distinguish between).

---
What is the current trend in RGB cameras? #flashcard #MOB #HardwareSoftwareArchitecture 
	They are trending towards being more HD and with a wider dynamic range.

---
Why is there a trade off for RGB cameras FOV? #flashcard #MOB #HardwareSoftwareArchitecture
	Low FOV can see less of the scene but in higher resolution where as high FOV can see more of the scene but the resolution is spread more thinly.

---
What are stereo cameras? #flashcard #MOB #HardwareSoftwareArchitecture 
	This is a setup where two or more cameras are used place some distance apart. This distance is used to get the same affect as binocular vision in humans where the depth of the scene can be estimated. This allows for a depth image of the scene.

---
What is LiDAR and how does it work? #flashcard #MOB #HardwareSoftwareArchitecture 
	LiDAR used pulses of light to eliminate the scene. Then by measuring the pulses it can accurately measure the depth at different points.

---
What type of light does LiDAR use? #flashcard #MOB #HardwareSoftwareArchitecture 
	It uses close IR light that humans cannot see.

---
What is a Lidar sensor and example of? #flashcard #MOB #HardwareSoftwareArchitecture 
	It is an example of a transceiver as it send out a signal then measure the response.

---
What is mmWave radar? #flashcard #MOB #HardwareSoftwareArchitecture 
	This a sensor that measures in a way similar to LiDAR sending out pulses of an even lower wavelength EM. This allows for the position, speed and acceleration of objects to be measured by exploiting the Doppler Effect.

---
What is ultrasonic sonar? #flashcard #MOB #HardwareSoftwareArchitecture 
	This is a sensor that sends out pulses of ultrasonic sound and listens to the response.

---
What are the downsides of ultrasonic sonar and where is it used? #flashcard #MOB #HardwareSoftwareArchitecture 
	The downsides are it is low range (~5m) and takes longer to get an image as compared to LiDAR and mm Radar as it uses sound waves. Hence it is generally only used for service robots.

---
What are the three main types of proprioceptive sensors in mobile robots? #flashcard #MOB #HardwareSoftwareArchitecture 
	GNSS (Global Navigation Satellite System), IMU and Wheel Odometry.

---
What does GNSS stand for and give a robot in terms of a measurement? #flashcard #MOB #HardwareSoftwareArchitecture
	GNSS (Global Navigation Satellite System) used give a position of the robot in the world aswell as its speed and heading. 
	
---
What does IMU give a robot in terms of measurements? #flashcard #MOB #HardwareSoftwareArchitecture
	IMU used to measure the rotation, acceleration (angular acceleration too) and speed of the robot.

---
What does wheel odometry give a robot in terms of measurements? #flashcard #MOB #HardwareSoftwareArchitecture 
	It measure the speed and direction of the wheels providing overall speed and orientation of the robot.

---
What are the three types of parallel accelerators used for processing sensor data? #flashcard #MOB #HardwareSoftwareArchitecture 
	Graphics Cards, FPGAs and ASICs

---
What does FPGA stand for?  #flashcard #MOB #HardwareSoftwareArchitecture 
	Field Programmable Gate Arrays

---
What does ASIC stand for?  #flashcard #MOB #HardwareSoftwareArchitecture 
	Application Specific Integrated Circuit

---
What is the trade off between Graphics Cards, FPGAs and ASICs?  #flashcard #MOB #HardwareSoftwareArchitecture 
	Moving away from graphics cards we get greater and faster performance but on a narrower more fixed set of problems. Graphics Cards are versatile be slower while ASICs are the faster but can only do what they were designed to do.

---
What is hardware synchronization?  #flashcard #MOB #HardwareSoftwareArchitecture 
	This is the idea that all our sensor bus be calibrated to not give conflicting readings. If we are getting two scenes from two cameras but they are misaligned this can give erroneous readings.

---
What is the basic top down path for the software architecture in a mobile robot?  #flashcard #MOB #HardwareSoftwareArchitecture 
	**Senor Data** comes in and is used for *Environment Mapping* and *Environment  Perception* (both of which help each other). Out map/perception of the world is then used in *Motion Planning* to generate an idea of what to do next. Finally this requirement is fed to our *controllers* which translate this plan into actions performed by the **Actuators** truly moving the robot.

---
What inputs are used to find position and 6DoF in environment perception phase, what is this called?  #flashcard #MOB #HardwareSoftwareArchitecture 
	We can use the GPS system alongside wheel Odometry, IMU. 

---
What is localization in the context of environment perception?  #flashcard #MOB #HardwareSoftwareArchitecture 
	Localization is where we find the robots position and 6DoF.

---
What path is used to perceive dynamic objects in environment perception?  #flashcard #MOB #HardwareSoftwareArchitecture 
	First we **detect** the objects then **tracking** takes place to see how these objects move over time. This can then be used in **prediction** to see where they objects will be in the future.

---
What inputs are used for **dynamic objects detection**?  #flashcard #MOB #HardwareSoftwareArchitecture 
	For dynamics object detection LiDAR, Cameras and Radar may be used (other are possible).

---
What inputs are used for detecting *static objects*?  #flashcard #MOB #HardwareSoftwareArchitecture 
	For static objects LiDAR, Cameras and Radar may but used however a HD road map may also be used which has fixed information about the road and can help the robot decide what is what.

---
What is an occupancy grid map?  #flashcard #MOB #HardwareSoftwareArchitecture 
	An occupancy grid map describes what is where in the environment; describes in space where things are.

---
What inputs are used to create an occupancy grid map?  #flashcard #MOB #HardwareSoftwareArchitecture 
	Object tracks for dynamics objects aswell as Static objects may be used. This can be combined with the raw **LiDAR/ Depth Cameras/ Cameras/ Radar** data.

---
What is a localization map?  #flashcard #MOB #HardwareSoftwareArchitecture 
	Mapping builds up a picture of a world where as localization describes how the robot fits into it hence. A localization map is a map of how the robot fits into the world.

---
What are the three layers used to make up motion planning?  #flashcard #MOB #HardwareSoftwareArchitecture 
	These layers are the **mission planner**, **behavior planner** and the **local planner**.

---
What does the mission planner do in motion planning?  #flashcard #MOB #HardwareSoftwareArchitecture 
	This mission planner takes in the overall mission and produces a *mission path* that describes the plan of how the robot will accomplish its goal.

---
What does the behavior planner do in motion planning?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The mission plan describes what we are do do in the world as if it were static. The behavior planner brings in dynamic components and makes sure to follow any rules set out. Basically constrains the plan to reality.

---
What does the local planner do in motion planning?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The local planner takes in the behavior constraint from the behavior planner and works through how the robot actually moves this produces a planned trajectory.

---
What inputs are needed by the mission planners?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The mission planner needs a concept of what the current goal is. Then it needs a way to decide what do do based on this. Hence it will need a HD road map in the case of an auto and it will need its own position (state).

---
What inputs are needed by the behaviors planner?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The behaviors planner needs to work in how dynamic objects not mapped out affect the plan and work around this. It also needs the overall plan given by the mission planner.

---
What inputs does the local planner need?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The local planner will need the behavior generated by the behavior planner aswell as an occupancy map and any other dynamic objects the produced planned trajectory must avoid.

---
What does the controller do in the mobile robot software stack?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The controller takes in the planned trajectory and compares it to the true position of the robot. It can then calculate how to vary the different actuators of the robot to match this trajectory.

---
What is the system supervisors role in a mobile robot?  #flashcard #MOB #HardwareSoftwareArchitecture 
	The system supervisor's job is to take a top down view of the different steps and ensure nothing is out of place or mismatches suggesting some problem in the other steps. 

---
What are the two types of system supervisors?  #flashcard #MOB #HardwareSoftwareArchitecture 
	these are the **software supervisor** and the **hardware supervisor**.

---
What does IMU stand for? #flashcard #MOB #HardwareSoftwareArchitecture 
	Inertial Measurement Unit

---