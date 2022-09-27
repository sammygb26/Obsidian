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
