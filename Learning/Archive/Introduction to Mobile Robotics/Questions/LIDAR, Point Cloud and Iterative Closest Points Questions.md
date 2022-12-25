What three things do you need to make LIDAR work? #flashcard #MOB #LIDARPointCloudICP
	1) A system that outputs light in a direction 2) A way to sense the light again 3) A very accurate clock

---
How does lidar measure the distance to an object (formula)? #flashcard #MOB #LIDARPointCloudICP 
	LIDAR measure distance to an object by measuring the time it takes for some light to bounce back form that object this is $t$. The light will travel at the speed of light $c$ hence the distance $r$ is defined as $$r=\frac12c\cdot t$$

---
How can we get a simple LIDAR system in do with a laser and mirror? #flashcard #MOB #LIDARPointCloudICP 
	The laser can shoot pulses which we can measure the response of before another pulse is sent out. We can use a mirror to change the angle of the laser and so take a 2D slice of a space.

---
What is the inverse and forward sensor models in LiDAR? #flashcard #MOB #LIDARPointCloudICP 
	The inverse goes from angles and range to x, y, z while the forward goes the other way around. It makes sense that it is this way around as the sensor model takes in some state (x, y, z) and not some sensor data (r, a, e).

---
What are the three components that make up the 3D polar coordinates? #flashcard #MOB #LIDARPointCloudICP 
	These are the azimuth, elevation and range ($\alpha$, $\epsilon$, $r$). Azimuth is the angle along the ground and elevation is the angle vertically.

---
How is LiDAR data stored? #flashcard #MOB #LIDARPointCloudICP 
	LiDAR data is commonly stored as a massive matrix of point arrays.

---
How can we translate our LiDAR points?  #flashcard #MOB #LIDARPointCloudICP 
	The LiDAR points are stored as a matrix with a row or column for each point. All we need to do to translate is to add a matrix where each row or column is the same translation vector and so we can shift all the points.

---
How can we rotate our LiDAR points?  #flashcard #MOB #LIDARPointCloudICP 
	We can perform this with a rotation matrix left multiplying by it on each point individually or the dataset as a whole.

---
How can the different axis of our LiDAR space be scaled?  #flashcard #MOB #LIDARPointCloudICP 
	We can do this by having a scaling matrix where each diagonal is the scaling coefficient for an individual axis.

---
What we bring scaling, translation and rotation together for a LiDAR point cloud what order are they performed in?  #flashcard #MOB #LIDARPointCloudICP 
	1) Translation 2) Rotation 3) Scaling

---
What is the state estimation problem in LiDAR?  #flashcard #MOB #LIDARPointCloudICP 
	In this problem we are given the pint found in two frames and we must calculate the state change between the two frames for our ego.

---
What are the symbols used for our points in LiDAR?  #flashcard #MOB #LIDARPointCloudICP 
	This would just be $p_i$ for a point and $P$ for our matrix of points.

---
What symbol is used for scaling rotation and translation in LiDAR?  #flashcard #MOB #LIDARPointCloudICP 
	This would be $S$ for scaling $C$ for rotation $r$ for translation with points and $R$ for translation with the whole matrix.

---
What is the state estimation problem in LiDAR mathematically?  #flashcard #MOB #LIDARPointCloudICP 
	In this problem we are given two sets of points $P_S$ and $P_{S'}$ we want to find $\hat C_{s's}$ and $\hat r_{s's}$ in order to estimate the change between the two frames. 

---
What problem does the iterative closest points algorithm solve?  #flashcard #MOB #LIDARPointCloudICP 
	It solve the problem of estimating the state change given two points clouds.

---
What is the idea that makes ICP algorithm work?  #flashcard #MOB #LIDARPointCloudICP 
	The key idea is that we are trying to minimize the difference in distance between points that are close in the real world.

---
What are the steps of the ICP algorithm?  #flashcard #MOB #LIDARPointCloudICP 
	1) We get an initial guess for the transformation $\{C,R\}$ 2) Associate each point in $P_{S'}$ with nearest point in $P_S$. 3) Solve for the optimal transform $\{\hat C_{S,S'},\hat r_S^{S,S'}\}$. 4) Repeat using the new transform replacing our initial guess until we converge to a solution.

---
What are the steps to find C and r in each step of the ICP algorithm?  #flashcard #MOB #LIDARPointCloudICP 
	We calculate the **centroid** for the two point clouds (means). Then we compute a **spread matrix** $$W_{s's}=\frac1n\sum_{j=1}^n(p_s^{(j)}-\mu_s)(p_{s'}^{(j)}-\mu_{s'})^T$$Then we take the SGV decomposition of $W_{S'S}=USV^T$ and we can finally we find $\hat C_{S'S}=UYV^T$ where $Y$ is an identify matrix with the bottom right corner replaced with $\det U\det V$. Finally we can calculate $r$ $$r_S^{S'S}=\mu_S-\hat C_{S'S}^T\mu_{S'}$$

---
What problem can outliers lead to with ICP algorithm?  #flashcard #MOB #LIDARPointCloudICP 
	Some points wont have matches in both point clouds. Therefore they will always lead to high error and with least squares quadratically high error. To get around this we can use different error functions. Such as the Absolute, Cauchy and Huber losses. These discount errors that are larger.

---
How is the Squared error function defined?  #flashcard #MOB #LIDARPointCloudICP 
	This is L2 $$p(e)=\frac12 ||e||_2^2=\frac12e^Te$$

---
How is absolute error defined?  #flashcard #MOB #LIDARPointCloudICP 
	This is L1 defined as $$p(e)=||e||_1=\sum_i|e_i|$$

---
How is Cauchy loss defined?  #flashcard #MOB #LIDARPointCloudICP 
	This is defined as $$p(e)=\frac{k^2}2\log\left(1+\frac1{k^2}||e||_2^2\right)$$

---
How can ground plane estimation be done with LiDAR? #flashcard #MOB #LIDARPointCloudICP 
	We can use semantic segmentation to understand which points form what angles belong to this class.

---
How can dynamic objects be removed? #flashcard #MOB #LIDARPointCloudICP 
	Once dynamic objects have been detected we can use their bounding boxes to remove them.

---
