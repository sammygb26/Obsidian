Lidar is a light laser based ranging device. It was developed for study the atmosphere and then Apollo 15 used lidar to map the surface of the moon.

You need three things to make lidar work. A system that outputs the light (can be spinning to get many angles). A way to sense the data again. Then a very accurate close to allow the time difference to measure the distance.

![[Pasted image 20221031104248.png]]

### 2D LIDAR
In 2D we can use a laser and pulse it while rotating a mirror this gives a view of the world. But this can be problematic with certain surfaces like glass.

![[Pasted image 20221031104432.png]]

In **3D** we can sense higher angles and get a better view of the world.

### Measurement models
The two angles the elevation and azimuth allows us to find the vector to the point hence get its $x,y,z$. But this is **non-linear** if we convert from the polar coordinates to $x,y,z$. This is called the **Inverse Sensor model** but we also get then we have the **forward sensor model** going form $x,y,z$ to polar coordinates.

![[Pasted image 20221031104854.png]]

### LIDAR point clouds
We get many points as the beam scans and this will be sorted in a massive matrix.

![[Pasted image 20221031105030.png]]

### Translation
We can move our points all together by batching them together.

![[Pasted image 20221031105142.png]]

### Rotation
We can also perform rotation we can rotate all the data together and because of the format we store the data in it can all be done my one matrix multiplication.

![[Pasted image 20221031105252.png]]

### Scaling
We can make a scaling matrix for each axis.

![[Pasted image 20221031105446.png]]

### All together 
![[Pasted image 20221031105549.png]]

### State Estimation via Point Set Registration

![[Pasted image 20221031105627.png]]

Here we want to find a transformation from one timestep to the next and hence estimate how far the car has moved. We want to find the **optimal translation** and **optimal rotation** between the two sensor reference frames minimizing the distance between the two point clouds.

![[Pasted image 20221031105804.png]]

The **Iterative Closes Point** Algorithm is inspired by the idea that corresponding points will be closer to a partner than to any other points.

1. Get an **initial** guess for the transformation $\{\check C_{s,s'},\check r_s^{s,s'}\}$
2. Associate each point in $P_{S'}$ with the nearest point in $P_S$.
3. Solve for the optimal transformation $\{\hat C_{s,s'},\hat r_s^{s,s'}\}$
4. We can repeat using the new transformation replacing out initial guess then we will get a better solution

### Solving for Rotation and Transformation
We need to find $\{\check C_{s,s'},\check r_s^{s,s'}\}$ each iteration. We can use least squares to do this being careful with with the rotation matrices.

![[Pasted image 20221031110349.png]]

![[Pasted image 20221031110438.png]]

![[Pasted image 20221031110512.png]]

### Outliers
Sometimes not all points are paired up correctly. Even the prefect transform will give erros.

![[Pasted image 20221031110651.png]]

This will cause a huger error in the loss. One way to get around this is to use different error terms.

![[Pasted image 20221031110744.png]]

This discounts errors that are too far away making them make less difference to the overall result.