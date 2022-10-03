What is the pinhole camera model? #flashcard #MOB #Camera 
	The pinhole camera model is a simple view of how a camera works. It comes as a basic way to project an image of a world onto an **image plane**. We have a hold in a wall this way each point on the image plane corresponds to its own line in the world hence the image isn't blurred.

---
What is a virtual image plane? #flashcard #MOB #Camera 
	The virtual image plane is a simplification of the image plane in a **pinhole camera** model. This way the image is Infront of the *camera center* and therefore the image isn't inverted.

---
What is the focal length? #flashcard #MOB #Camera 
	The focal length of a camera $f$ is the distance form the image center to the image plane.

---
How can we describe the projection performed in a pinhole camera model? #flashcard #MOB #Camera 
	We start by using a *virtual image*. There is a line that passes from the camera center through the virtual image to any point in out image. So for any point we just need to trace out this line. If the point has the position $\textbf x$ then the gradient will be ${\textbf x}/{z}$ and with focal length $f$ the point in out virtual image will be $f\textbf x/z$.a

---
How are UV coordinates created from world positions in terms of equations given the difference in their origin? #flashcard #MOB #Camera 
	For some point $(x, y,z)$ we have our virtual image coordinates as $x'=x/z$ and $y'=y/z$ but UV coordinates have their center in the bottom left corner hence we add on $u_0$ and $v_0$ giving $x'=x/z+u_0$ and $y'=y/z+v_0$.

---
How is the projection to UV coordinates written in matrix form? #flashcard #MOB #Camera 
	The first row is $[f_x\hspace{3pt}s\hspace{3pt}u_0\hspace{3pt}0]$ where $f_x$ is the $x$ focal distance this just means some amount we scale $x$ values by. Then $s$ is the skewness which in modern cameras is very small. $u_0$ is in the third column so it is multiplied by $z$. This just counteracts the scale factor $w=z$ which is applied to the UV vector. Then the second column is much the same with the form $[0\hspace{3pt}f_y\hspace{3pt}v_0\hspace{3pt}0]$ just missing the skew factor however this doesn't matter as it is already accounted for in the first column. Just as above this will resolve to $wv$ and since $w=z$ the scaling factor will be maintained despite being the in the third column. The final column is just $[0\hspace{3pt}0\hspace{3pt}1\hspace{3pt}0]$ and resolves to $w$ hence means $w=z$.

---
What are intrinsic and extrinsic parameters in camera projection? #flashcard #MOB #Camera 
	The **intrinsic parameters** describe the properties of the camera like the focal distance, skewness and UV offset. The **extrinsic parameters** describe the position of the camera in the world. We have a rotation matrix describing how any projected object's coordinates should be rotated to be in the correct orientation with respect to the camera and we have a positional vector that describe how to move the object so that is position is relative to the camera.

---
How can the projection matrix P be described by Intrinsic and extrinsic parameters? #flashcard #MOB #Camera 
	We can break $\textbf P$ into $\textbf K[\textbf R|\textbf t]$. Where $\textbf K$ is the **intrinsic parameter** describing the position of the camera. Then $\textbf R$ is the rotation matrix and $\textbf t$ is the translation vector, rotating and offsetting points such that their position is relative to the camera.

---
What are the 4 steps to calibrate a camera finding K, R and t? #flashcard #MOB #Camera 
	We first need to **detect key points** which we will track. Then we **generate pairs** of worlds pace and UV coordinates. Then we use this information to generate a system of simultaneous equations which we can **solve** to get $\textbf P$. Then we **decompose K, R and t from P** by using the properties of $\textbf R$ and form of $\textbf K$ we can solve for $\textbf K$ and use this to find $\textbf R$ and $\textbf t$.

---
In the camera calibration task of a checkerboard inverted box what makes the task easier? #flashcard #MOB #Camera 
	The box gives convenient points whose offset from the far corner we know if the size of the box is known. This way we can assume the corner is the origin and since the points offset is known we can get their world space position. This provides the UV world space pairs we need to solve for the $\textbf P$ projection matrix in calibration.

---
How can we solve the matrix P from pairs of UV worlds pace coordinates? #flashcard #MOB #Camera 
	The projection matrix describes a set of three equations $uw=\textbf p_1\textbf x$, $vw=\textbf p_2\textbf x$  and $w=\textbf p_3\textbf x$ this way we can get two equations by working $w$ into the first two equations. This gives $$\textbf p_1\textbf x-u\textbf p_3\textbf x=0\hspace{16pt}\textbf p_2\textbf x-v\textbf p_3\textbf x=0$$which are two equations with the unknown variables being the $p_{ij}$ values. So if $\textbf p=[p_{11}\hspace{3pt}p_{12}\hspace{3pt}...\hspace{3pt}p_{34}]$ we can form a system of linear equations $\textbf{Ap}=0$ where the rows of $\textbf A$ are made out of the equations from the pairs of points.

---
How can we decompose P into K, R and t? #flashcard #MOB #Camera 
	These terms are equal in that $\textbf P=\textbf K[\textbf R|\textbf t]=[\textbf{KR}|\textbf{Kt}]$ now we can perform $\textbf{KR}(\textbf{KR})^T$ which we can find as the first 3x3 columns of $\textbf P$ multiplied by its transpose. But $\textbf {KR}(\textbf {KR})^T=\textbf{KRR}^T\textbf K^T=\textbf{KK}^T$ as $\textbf R$ is a rotation matrix so its transpose is its inverse. Now since the form of $\textbf K$ is known we can find the form of $\textbf {KK}^T$ and this allows us to solve for the values of $\textbf K$. Then once we have $\textbf K$ we can solve for $\textbf K^{-1}$ and use this to find $[\textbf R|\textbf t]$ from $\textbf P=\textbf K[\textbf R|\textbf t]$.

---
How can basic image filtering be applied? #flashcard #MOB #Camera 
	We can use a basic cross-correlation filter. We replace each pixel with some matric some over the surrounding pixels.

---
What is a gross correlation filer? #flashcard #MOB #Camera 
	A cross correlation filter is a a general case where we apply a filter by sliding some matrix (a function) over our image which is another matrix.

---
How does gaussian cross-correlation filter differ form a mean filter? #flashcard #MOB #Camera 
	A cross correlation filter in the mean case is just a matrix filled with 1s. For some kernel size $k$ it will be a $2k+1\times2k+1$ matrix of 1s. However a gaussian filter will have a 4 at the center then on all the axes 2s and then 1s in the corners (at least in the case of $k=1$).

---
What do we need to use stereo cameras to find the depth of some object? #flashcard #MOB #Camera 
	We need the positions of the points in the image plane that is the UV of the object form each camera.

---
What assumption do we need to make to find the depth of an object form two cameras? #flashcard #MOB #Camera 
	We need to assume that $Z_R\approx Z_L\approx Z$ hence we assume the distance between the cameras $b$ is negligible in terms of $Z$.

---
What is the formula for $Z$ given $x_L$ and $x_R$ (stereo cameras)? #flashcard #MOB #Camera 
	We get that $Z=\frac{fb}{(x_L-x_R)}=\frac{fb}d$ where $d=x_L-x_R$ is the divergence. This makes since as with low divergence the point is far away which makes sense as far away object move slower as you shift form side to side.

---

