What are coordinate systems?  #flashcard #MOB #CoordinateSystemReferenceFrames
	Coordinate systems are different ways of labeling space around earth. They are useful for different applications and so used in different situations.

---
What are the two most basic coordinate systems? #flashcard #MOB #CoordinateSystemReferenceFrames 
	These would be the ego-vehicle coordinate system and the world coordinate (global) coordinate system. One is relative to the car one is global.

---
What is a rigid body and how does this help with localizing measurements? #flashcard #MOB #CoordinateSystemReferenceFrames 
	A rigid body is a in which deformation is zero or so small it's negligent. This simplifies calculations of reference frames since we can assume sensors have a constant position relative to the car.

---
What type of frame is used in robotic when it comes to cartesian coordinates? #flashcard #MOB #CoordinateSystemReferenceFrames 
	We use a right hand frames only. That is with our right hand pointing index into the air thumb along x and middle finger along z.

---
What do we need to describe rigid body movement? #flashcard #MOB #CoordinateSystemReferenceFrames 
	We only need rotations and translations. For each frame we take a rotation then a translation or the other way around.

---
What are the 6DofF for a rigid body in 3D space? #flashcard #MOB #CoordinateSystemReferenceFrames 
	These are the three positional constraints x, y, and z. Then the three rotational constraints roll (around z axis), pitch (around x axis) and yaw (around y axis).

---
How can a vector be rotated between reference frames and what is this called? #flashcard #MOB #CoordinateSystemReferenceFrames 
	We need a matrix that describes the rotation of a vector form one frame $a$ to another $b$. We use a subscript to describe this. This way $$r_b=C_{ba}r_a$$

---
How can the transformation from one reference frame to another be captured? #flashcard #MOB #CoordinateSystemReferenceFrames 
	This is described with a transformation vector. It is labeled with a superscript the firs lifter from the second to. So if we have vectors about $a$ but we have moved to $b$ we need $r^{ab}$. This way $$r^{pb}=r^{ab}+r^{pa}$$

---
How is rotation and translation combined to transform coordinates between systems? #flashcard #MOB #CoordinateSystemReferenceFrames 
	We get $$\vec{r}^{pa}_b=\vec r^{ab}_b+C_{ab}r_a^{pa}$$

---
How is the direct cosine matrix created? #flashcard #MOB #CoordinateSystemReferenceFrames 
	We are given three axis vectors in the two coordinate system $a$ and $b$. That is $A=[\vec a_1,\vec a_2,\vec a_3]$ and $B=[\vec b_1,\vec b_2,\vec b_3]$ the inner product is then taken. $$C_{ab}=B^TA$$ which gives a cosine matrix where $c{ij}=\cos(\theta_{\text{axis}_i, \text{axis}_j})$. Where $\text{axis}_1=x$ and $\text{axis}_2=y$ etc.

---
What is the DCM direct cosine matrix? #flashcard #MOB #CoordinateSystemReferenceFrames 
	This is just a matrix describing the rotating between two coordinate systems.

---
What are Euler Angles? #flashcard #MOB #CoordinateSystemReferenceFrames 
	Euler angles is a way of describing rotation where we have three rotation matrices one for each axis. Then our final rotation is $$C(\theta_3, \theta_2, \theta_1)=C_3(\theta_3)C_2(\theta_2)C_1(\theta_1)$$ Here $C_1,C_2,C_3$ describe rotation around the 3rd 2nd and 1st axis respectively.

---
What is a problem with Euler angles? #flashcard #MOB #CoordinateSystemReferenceFrames
	The problem is a phenomena called Gimbal Lock where two rotation axis can become aligned by the first such that all rotation now only takes place in two axis. That is multiple angles give the same effect.

---
What are unit quaternions? #flashcard #MOB #CoordinateSystemReferenceFrames 
	A quaternion $\mathbf q\in\mathbb M$ is an extended number system of complex number. Which may be represented as a vector and can describe rotations.

---
What are the pros and cons of DCM, Unit quaternions and Euler angles? #flashcard #MOB #CoordinateSystemReferenceFrames 
	DCM uses 9 parameters and so is space inefficient. Euler angles only uses 3 parameters instead of 9 for DMC but has singularities (Gimbal lock).

---
What is important about the order or rotations in 3D? #flashcard #MOB #CoordinateSystemReferenceFrames 
	In 3D rotations aren't commutative so different orders of rotations will give different results.

---
What are reference frames in robotics? #flashcard #MOB #CoordinateSystemReferenceFrames 
	Reference frames in robotics are systems of coordinates that can be used to describe space.

---
What is the ECF reference frame and what do we need to measure it? #flashcard #MOB #CoordinateSystemReferenceFrames 
	This is the Earth Centered Fixed Frame. Here we measure a position with and **latitude** (rotation above or bellow equator) and **longitude** (rotation left or right of GMT).  We also need the semi-major axis describing the shape of earth. The ECF position cab then be given as $x,y,z$ away from the center of the earth.

---
What is the navigation reference frame? #flashcard #MOB #CoordinateSystemReferenceFrames 
	This is a reference frame fixed to the ground and it used for simplicity when an autonomous car is  moving. This usually has an origin of our starting point then $x$ is north, $y$ is east and $z$ is down along gravity.

---
What is extrinsic calibration? #flashcard #MOB #CoordinateSystemReferenceFrames 
	All the sensor we have have their own reference frame. We need to know these so we can combine them all together without misalignment.

---
What is the GNSS? #flashcard #MOB #CoordinateSystemReferenceFrames 
	This is the Global Navigation Satellite System and is made of of many difference satellite from different countries.

---
What is GPS? #flashcard #MOB #CoordinateSystemReferenceFrames 
	This is the American part of GNSS made our of 31 satellites in 6 orbital planes.

---
What is encoded in a transmission from a GPS satellite? #flashcard #MOB #CoordinateSystemReferenceFrames 
	**Position** encoded in ECEFF coordinates given by ephemeris information (orbit info) and **time of signal transmission** given by atomic clock.

---	
How does GPS work? #flashcard #MOB #CoordinateSystemReferenceFrames 
	GPS has 31 satellites in many known positions. They broadcast a signal which encodes giving a position of a satellite and the time of transmission. We then know our position is within $c\Delta t$ of this satellites position and we can cross-reference with 4 other satellites to get our position.

---
What equation describes the relation between a receiver position and a satellite position in GPS? #flashcard #MOB #CoordinateSystemReferenceFrames
	This is $$p^{(i)}=c(t_r-t_s)=\sqrt{(p^{(i)}-r)^T(p^{(i)}-r)}+c\Delta t_r+c\Delta t_a^{(i)}+\eta^{(i)}$$ Where $r$ is the receiver 3D position, $p^{(i)}$ is the position of satellite $i$, $\Delta t_r$ is the receiver clock error, $\Delta t_a^{(i)}$ atmospheric propagation delay, $\eta$ measurement noise, $c$ speed of light $t_s$ and $t_r$ are time send and received.

---
What are the three sources of GPS error? #flashcard #MOB #CoordinateSystemReferenceFrames 
	These are **ephemeris & clock errors**, **multipath effect** and **ionosphere delay**.

---
Why are ephemeris and clock errors in GPS a problem? #flashcard #MOB #CoordinateSystemReferenceFrames 
	GPS calculation uses speed of light so small errors in time calculation give large differences in position while wrong satellite positions will give erroneous results.

---
Why is the multipath effect a problem in GPS? #flashcard #MOB #CoordinateSystemReferenceFrames 
	Here we get signals reflected of buildings so we cannot be sure the signal too the shortest path hence we can overestimate our distance to the satellite.

---
Why is ionosphere delay a problem is GPS? #flashcard #MOB #CoordinateSystemReferenceFrames
	Here charged ions can slow down the signal and so the weather can effect the accuracy of GPS (rain).

---