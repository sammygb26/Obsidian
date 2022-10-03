# Camera Calibration
In the *pinhole* camera model we are projecting light form the outside world only an *image plane*. This is behind the camera and so gives an inversed flipped image. For simplicity in the math we therefore have a **virtual image** that is Infront of the *camera center*.

![[Pasted image 20220929192536.png]]

We can look at this model in 2D to get a better idea of the dynamics. We see that the $y$ position of some world point is on a line that also passes through the *image plane*. We want the point on the image plane. If we take $f$ to be the distance form $C$ to the image plane and $z$ to be the distance from $C$ to the object. Then the $x$ value will be scaled down by $z$ and scaled up by $f$. Hence in matrix form we have$$x_i=\frac fzx\hspace{32pt}y_i=\frac fzy$$![[Pasted image 20220929192855.png]]

We also add on a $u_0$ and $v_0$ term as UV virtual image coordinates are measured from the bottom left corner. $$x_i=\frac fzx+u_0\hspace{32pt}y_i=\frac fzy+v_0$$![[Pasted image 20220929193226.png]]
Now we have equations that explain the projection from world space to image space. Hence now we can write in in matrix form. We add a *scale-factor* $w$ which is $z$ in the following case as we are just projecting realistic image coordinates. This gives

![[Pasted image 20220929193645.png]]

This matrix above is called the **projection matrix** we can decompose it further into three matrices that break up the different components of the camera. $K$ is the *intrinsic parameters* so the actual camera properties. Then $[R|t]$ are the *extrinsic parameters*. $R$ is the rotation matric and $t$ is the translation matrix.


![[Pasted image 20220929141851.png]]

### Calibration
*Calibration* takes 4 steps. We need to identify *key points* for fixed world coordinates. We use this to generate 3D-2D matching pairs. We then use these pairs to solve for the matrix $\textbf P$. We then decompose this matric to find $\textbf K[\textbf R|\textbf t]$ from $\textbf P$.

- **Detecting key points** -> The checkerboard pattern can be used allowing us to detect many different points that are fixed in the world. This can be done by a computer vision program and is particularly easy with the chessboard pattern bellow.

![[Pasted image 20220929194753.png]]

- **Generate pairs** -> We can treat the checkerboard as the origin this way each order we are detecting we already know the position of. Hence we have the image position form the image and the world position.

![[Pasted image 20220929194919.png]]

- **Solve for matrix P** -> We have the basic equation $\textbf x_i\times\textbf P\textbf X_i=0$ that is the $\textbf x_i$ and $\textbf P\textbf X_i$ matrices point in the same direction.  ![[Pasted image 20220929195356.png]]The knowns here are  $x$, $y$, $z$, $u$ and $v$. Through matrix multiplication we get that $$w=\textbf p_3\textbf X$$Then we can also say for $u$ and $v$ that $$wu=\textbf p_1\textbf X\hspace{32pt}wv=\textbf p_2\textbf X$$We can replace $w$ with the form above and get the following. $$u(\textbf p_3\textbf X)-\textbf p_1\textbf X=0\hspace{32pt}v(\textbf p_3\textbf X)-\textbf p_2\textbf X=0$$This therefore gives 2 equations for every pair of UV -> worlds pace coordinates. Hence we are solving a system of equations for the $p_{ij}$ values of the *projections matrix*. So we build a matrix $\textbf A$ out of these equations. Have 12 values we need to solve to find $p$ hence we need $N$ points where $2N>11$. We make a column vector $\mathcal P=[p_{11}\hspace{4pt}p_{12}.\hspace{2pt}..\hspace{2pt}p_{34}]^T$ and solve $\textbf A\mathcal P=0$

- **Decompose K, R, t from P** now we have$\textbf P$ we know $\textbf P=\textbf K[\textbf R|\textbf t]$ we can start by solving for $\textbf K$. We do this by noting that by distributing $\textbf K$ we get $\textbf P=\textbf K[\textbf R|\textbf t]=[\textbf{KR}|\textbf{Kt}]$. Now we have the left portion of $\textbf P$ and we can times it by itself. Hence $\textbf {KR}(\textbf {KR})^T=\textbf{KRR}^T\textbf K^T=\textbf{KK}^T$ now this equals the first 3x3 section of $\textbf P$ timed by it's transpose. Now we know the form of $\textbf K$ so we can find the form of $\textbf {KK}^T$. This means that if $\textbf{KK}^T=[k_{ij}]$ then we get the following equations: $$u_0=k_{13}\hspace{16pt}v_o=k_{23}\hspace{16pt}f_y=\sqrt{k_{22}-v_0^2}\hspace{16pt}s=\frac{k_{12}-u_0v_0}{f_y}\hspace{16pt}f_x=\sqrt{k_{11}-u_0^2-s^2}$$The reason $\textbf{RR}^T=\textbf I$ is that $\textbf R$ is a rotation matrix hence it's transpose is its inverse. Now that we know $\textbf K$ we can solve for $\textbf K^{-1}$ and so find $\textbf t$ from $\textbf{Kt}$ and $\textbf R$ from $\textbf{KR}$.  

[[Camera Calibration Questions]]
