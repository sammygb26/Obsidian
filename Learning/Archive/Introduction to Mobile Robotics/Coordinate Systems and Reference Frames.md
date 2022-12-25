There are multiple **coordinate systems** we need to know the relationship between them to achieve *sensor fusion*. On a basic level we may have a two systems **world coordinates** and **ego-vehicle** (relative to vehicle).

![[Pasted image 20221024111518.png]]

### Rigid Body
Rigid body is a solid body in which deformation is zero or so small it can be neglected. This matters as it implies the movements of the sensor is the same as the movement of the whole platform. This isn't the case with **soft body**.

### Coordinate System (Right hand only)
When dealing with motion we start with a *cartesian coordinate system*. We only use right handed frames in robotics.

![[Pasted image 20221024111801.png]]

With this **rigid body motion** can be describes by a rotation and then a translation (or the other way around).

![[Pasted image 20221024111835.png]]

### Degree of Freedom of a Rigid Body
Rigid-body robots have 6 degrees of freedom in 3D space. We have x, y, z then raw, pitch and yaw. There are three for translation and three for rotation.

![[Pasted image 20221024111944.png]]

We express these vector in **vectors** but these factors can be represented differently in different frames. We have have two different vectors in different coordinate systems. We need a coordinate rotation that transforms frame $a$ into frame $b$. $$r_b=C_{ba}r_a$$
### Coordinate Transformation
We use vector addition to making sure to express all the coordinates in the **same** frame. We use the superscript to indicate the **start and end point** of a 3D vector (right to left).

![[Pasted image 20221024112359.png]]

### Rotation Representation
**Direct Cosine Matrix** - DCM uses a 3x3 matric to represent the linear transform mapping from one coordinate frame to another.

![[Pasted image 20221024112526.png]]

**Euler Angles** - here we decompose our rotation into three steps for three different axis. Each angle represents a rotation for a different axis.

![[Pasted image 20221024112638.png]]

Euler angles are more *parameter efficient* as we only need three angles where as *DCM* has 9. Another problem is **Gimbal Lock** where there is a loss of one degree of freedom in a three-dimensional space. Also called a **singularity**. This is caused by the composition of rotations. This means the later axis are rotated by the first rotation. Hence if two axis become overlapped two axis will give the same rotation. This is a problem as we need the rotation to be defined but this gives **ambiguity**.

**Unit Quaternions** - A quaternion $\textbf q\in \mathbb M$ is an extended number system for complex numbers. It may be represented as a vector.

![[Pasted image 20221024113540.png]]

Rotation order **matters** as rotation in 3D are **non-commutative**.

# Reference Frames
**Earth Centered Fixed Frame** - ECEF coordinate frame rotates with the earth. The earth if fixed we measure the distance from the center of the earth. This is used by GNSS

![[Pasted image 20221024114033.png]]

**Navigation** - for autonomous driving we want to have a frame that is **fixed to the ground** for the ease of analysis and use. Usually we attach the origin of NED to a known starting point. Here $x$ is true north $y$ is true east and $z$ s down along gravity.

In the real world, the first step to build up multi sensor localization systems we need **extrinsic calibration** between sensors to capture the transformation between different coordinate systems.

![[Pasted image 20221024114354.png]]

### GNSS and Korean Air Flight 007
Here a plane was shot down by the soviets after flying over the air space. This was due to the initial setup of the navigation system. This lead to GPS being opened to the public.

### GNSS
![[Pasted image 20221024114554.png]]
There are many different satellites systems for different countries. 

With **GPS** we have 31 satellites in 6 orbital planes. The altitude is ~12,000 miles with a 12hr orbital period. Each satellite broadcasts on two frequencies L1 and L2 (military use only). Each **GPS** satellite transmits a signal which encodes: 

1. Its **position** in ECEFF coordinates via accurate ephemeris information (orbit info)
2. The **time of signal transmission** via onboard atomic clock.

To compute a GPS position we fix in ECEF, the receiver uses the **speed of light** to compute the distances to the different satellites (which we know the position of). For each satellite we measure the **pseudo range** as follows:

![[Pasted image 20221024115055.png]]

where

![[Pasted image 20221024115211.png]]

This defines a sphere and the intersection of 4 spheres will gives us a good position for the coordinate.

### GPS Error Sources
**Ephemeris & clock errors**: As GPS heavily uses speed of light for distance computation a clock error of 1x10^-6s gives 300m positional error. Or if we don't know the satellites position we will get erroneous readings.
**Multipath effect** here sometimes signals can come in from buildings and this causes extra time to be added to the time offset.
**Ionosphere delay** here charged ions in the atmosphere can affect signal propagation. This cause sit to not work well in in rainy weather.

These error cause the requirement to perform lo

[[Coordinate Systems and Reference Frames Questions]]