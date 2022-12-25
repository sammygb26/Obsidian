This is a classic algorithm which aligns two sets of three dimensional points. It uses a least squares based method where the weights for each term are scalars.

### Problem Setup
![[Pasted image 20221217170730.png]]

The problem is set up with a stationary reference frame and a moving reference frame attached to a vehicle. A collection of points $P_j$ is observed in both frames and the coal is to determine the relative pose of the moving frame with respect to the stationary one by aligning the two point clouds.

Formally we say there are two reference frames one **non-moving** ${\underset{\to}{\mathcal F}}_i$ and then one attached to a moving vehicle ${\underset{\to}{\mathcal F}}_{v_k}$. We have $M$ measurements $r_{vk}^{p_jv_k}$ where $j\in[M]$ of points from the vehicle expressed in the moving frame ${\underset{\to}{\mathcal F}}_{v_k}$ although these measurement could have been corrupted by **noise**. We assume we know $r_i^{p_ji}$ the position of each point $p_j$ located and expressed in the non-moving frame ${\underset{\to}{\mathcal F}}_i$. For example in **ICP** these are found by associating each point in the moving frame with the closest one in the non-moving frame. We want to find the translation and rotation that best align the two point clouds. We only care about alignment for a single time $k$.

##### Rotation Matrix Solution
We can first define $y_j=r_{v_K}^{p_jv_k}$, $p_j=r_i^{p_ji}$, $r=r_i^{v_ki}$, $C=C_{v_ki}$ for simplicity. Then we also define $$\mathbf y=\frac1w\sum_{j=1}^Nw_j\mathbf y_j\hspace{64pt}\mathbf p=\frac1w\sum_{j=1}^Mw_j\mathbf p_j\hspace{64pt}w=\sum_{j=1}^Mw_j$$where $w_j$ are scaler weights on each point. We define an error term for each point $$e_j=y_j-C(p_j-r)$$ our estimation is then to globally minimize the cost function: $$J(C,r)=\frac12\sum_{j=1}^Mw_je_j^Te_j=\frac12\sum_{j=1}^Mw_j(y_j-C(p_j-r))^T(y_j-C(p_j-r))$$subject to $C\in SO(3)$ meaning $CC^T=1$ and $\det C=1$. Before carrying out the optimization we will make a change of variables for the translation parameter. We define $$d=r+C^Ty-p$$which is easy to isolate for $r$ if all the other quantities are known. In this case we can rewrite our cost function as

![[Pasted image 20221217180633.png]]

which is the sum of two semi-positive definite terms the first depending only on $C$ and the second depending only on $d$. We can minimize the second trivially by taking $d=0$ which in turn implies that $$r=p-C^Ty$$this is simply the different of the centroids of the two point clouds expressed in the stationary frame. We then need to minimize the first term with respect to $C$> If we multiple out each smaller term within the first large term only one part depends on $C$.

![[Pasted image 20221217181632.png]]

So we can sum this term over all the weighted points giving

![[Pasted image 20221217181732.png]]

where $$W=\frac1w\sum_{j=1}^Mw_j(y_j-y)(p_j-p)^T$$this allows us to define a new cost function that we seek to minimize with respect to $C$ as $$J(C,\Lambda,\gamma)=-tr(CW^T)+\underbrace{tr(\Lambda(CC^T-1))+\gamma(\det C-1)}_{\text{Lagrange multiplier terms}}$$where $\Lambda$ and $\gamma$ are Lagrange multipliers associated with the two terms. This ensures $C\in SO(3)$. We can take the derivative of this $J(C,\Lambda,\gamma)$ with respect to $C$, $\lambda$ and $\gamma$ we get

![[Pasted image 20221217182740.png]]

Where $L$ is created by lumping the Lagrange multipliers together as $L+2\Lambda+\gamma1$. Hence setting this to 0 we get $$W=LC$$
##### Simple Solution
If we know that $\det W>0$ then we can post multiply the above equation by itself giving $$L\underbrace{CC^T}_{1}L^T=WW^T$$Since $L$ is symmetric we have $$L=(WW^T)^{\frac12}$$which involves the matrix square root. Substituting this back into the equation 2 above we get $$C=(WW^T)^{-\frac12}W$$ This works well with lots of non-coplanar points however for some applications like noisy RANSAC this doesn't work.

##### Detailed Explanation
Fist we can take the SVD of the square matrix $W$ so that $W=UDV^T$ where $U$ and $V$ are square orthogonal matrices and $D=diag(d_1,d_2,d_3)$ is a diagonal matrix of singular values $d_1\ge d_2\ge d_3\ge 0$. We can use $W=LC$ to and the above to give us

![[Pasted image 20221217184221.png]]

Taking the matrix square root gives us $$L=UMU^T$$ where $M$ is the symmetric matrix square root of $D^2$ meaning $M^2=D^2$. It can be show that every real symmetric $M$ satisfying this condition can be written as $$M=YDSY^T$$ where $S=diag(s_1,s_2,s_3)$ with $s_i=\pm 1$ and $Y$ an orthogonal matrix ($Y^TY=YY^T=1$). An example of how this could be true is $s_i=\pm1$ then $Y=1$ and then any values of $d_i$. But this isn't the only case. For example if $d_1=d_2$ then we can get

![[Pasted image 20221217193347.png]]

for any value of the parameter $\theta$. The *important point here* is that the structure of $Y$ can become more complex in correspondence with repeated singular values. We also have that $D=YDY^T$ due to eh structure of $Y$ and the multiplicity of the singular values in $D$. Now we manipulate the objective function we want to minimize as follows:

![[Pasted image 20221217195528.png]]

This gives several cases to consider.

1. $\det W\neq0$ 
	Here we have that all of the singular values are positive. Then from $W=LC$ and $L=UMU^T$ we get ![[Pasted image 20221217195939.png]] 
	Since the singular values are positive we have that $\det D>0$ or that the signs of the dominants of $S$ and $W$ must be the same which implies that ![[Pasted image 20221217200201.png]] 
	Note we have $\det U=\pm 1$ (since $(\det U)^2=\det(U^TU)=\det1=1$) and the same for $V$. There are four subcases.
		1. $\det W>0$, Since $\det W\ge 0$ by assumption we must also have $\det S=1$ and therefore to uniquely minimize $J$ we must pick $s_1=s_2=s_3=1$ since all $d_i$ are positive and therefore we must have $Y$ diagonal. Thus with $S=diag(1,1,1)$ we get the following which is equivalent to our simplified solution.  ![[Pasted image 20221217203422.png]]
		2. $\det W<0$ $d_1\ge d_2>d_3>0$. In this case since $\det W<0$ we have $\det S=-1$ which means exactly one of the $s_i$ is negative. In this case we can uniquely minimize $J$ since the minimum singular value $d_3$ is distinct we can pick $s_1=s_2=1$ and $s_3=-1$. We must have $Y$ diagonal so by the same logic as the above case we have $$C=USV^T$$ with $S=diag(1,1,-1)$
		3. $\det W<0$, $d_1>d_2=d_3>0$ as before we have $\det S=-1$ which means one $s_i$ is negative. Since $d_2=d_3$ we can pick s_2=-1$ or $s_3=-1$ and end up with the same value for $J$. With these values for the $s_i$ we can pick any of the following for $Y$: ![[Pasted image 20221217204958.png]] where $\theta$ is a free parameter. We can plug any of these $Y$ in to find minimizing solutions for $C$ using $W=LC$ this gives: $$C=UYSY^TV^T$$with $S=diag(1,1-1)$ or $S=diag(1,-1,1)$. Since $\theta$ can be anything there are an infinite number of solutions minimizing the objective function.
		4. $\det W<0$, $d_1=d_2=d_3>0$ as previously we have $\det S=-1$ which means exactly one of the $s_i$ must be negative. Since $d_1=d_2=d_3$ we can pick $s_1=-1$ or $s_2=-1$ or $s_3=-1$ and end up with the same value for $J$ this implies there is an infinite number of minimizing solutions
2. $\det W=0$. This time there are three subcases to consider depending on how many singular values are zero.
	1. $\text{rank}W=2$ In this case we have $d_1\ge d_2>d_3=0$. We can uniquely minimize $J$ by picking $s_1=s_2=1$. Since $d_3=0$ the value of $s_3$ does not affect $j$ and thus it is a free parameter. From $W=LC$ we get $$(UYDSY^TU^T)C=UDV^T$$Multiplying by $U^T$ from the left and $V$ from the right we get $$D\underbrace{U^TCV}_Q=D$$ since $DS=D$ due to $d_3=0$ and then $YDY^T=D$. That matrix $Q$ will be orthogonal since $U$, $C$ and $V$ are all orthogonal. Since $DQ=D$, $D=diag(d_1,d_2,0)$, and $QQ^T=1$ we know that $Q=diag(1,1,q_3)$ with $q_3=\pm1$ We also have that $$q_3=\det Q=\det U\underbrace{\det C}_1\det V=\det U\det V=\pm1$$Therefore we can rearrange and rename $Q$ and $S$ we have $$S=diag(1,1,\det U\det V$$
	2. $\text{rank }W=1$ In this case we have $d_1>d_2=d_3=0$. We let $s_1=1$ to minimize $J$ and now $s_23 and $s_3$ do not affect $J$ and are free parameters. Similarly to previously case we can end up with $$DQ=D$$ which along with $D=diag(d_1,0,0)$ and $QQ^T=1$, implies that $Q$ will ![[Pasted image 20221218115331.png]] with $\theta\in\mathbb R$ a free parameter. This means there are infinitely many minimizing solutions. Since $$\det Q=\det U\underbrace{\det C}_1\det V=\det U\det V=\pm1$$ renaming $Q$ and $S$ we get $$C=USV^T$$with ![[Pasted image 20221218115541.png]] This can corresponds to the points being collinear so that rotating about the axis they are colinear in does not alter the objective function $J$
	3. $\text{rank} W=0$ This corresponds to there being no points or all points coincident and so any $C\in SO(3)$ will produce the same value for $J$.

Looking at all these solutions we can see that depending on $W$ there can be 1 or infinitely many solutions. If there is a unique global solution it is always of the form $$C=USV^T$$ with $S=\text{diag}(1,1\det U\det V)$ and $W=UDV^T$ is a singular-value decomposition of $W$. The necessary and sufficient conditions for this unique global solution to exist are:

1. $\det W>0$, or
2. $\det W<0$ and minimum singular value distinct $d_1\ge d_2>d_3>0$ or 
3. $\text{rank}W=2$

If none of these conditions are true there will be infinite solutions for $C$> However, these cases are fairly pathological and do no occur frequently in practical situations.

Once we have found the optimal rotation matrix, we take $\hat C_{v_ki}=C$ as our estimated rotation. We build the estimated translation as $$\hat r_i^{v_ki}=p-\hat C^T_{v_ki}y$$and if desired combine the translation and rotation into an estimated transformation matrix $$\hat T_{v_ki}=\begin{bmatrix}\hat C_{v_ki}&-\hat C_{v_ki}\hat r_i^{v_ki}\\0^T&1\end{bmatrix}$$that provides the optimal alignment of the two point-clouds in a single quantity. We can also recover $\hat T_{iv_k}$ as follows.$$\hat T_{iv_k}=\hat T_{v_ki}^{-1}=\begin{bmatrix}\hat C_{iv_k}&\hat r_i^{v_ki}\\0^T&1\end{bmatrix}$$Both forms are useful depending on the required solution.

### Example
This is a case for 1:2 where $\det W<0$, $d_1\ge d_2>d_3>0$. So the solution is $C=USV^T$ with $S=\text{diag}(1,1,-1)$. We start of with the $p$ and $y$ points as follows

![[Pasted image 20221218131859.png]]

Where $1_i$ is the $i$th column of $I_3$. The point in the first point cloud are the centers of the faces of a rectangular prism. On the second point cloud the faces are associated with the opposite face. This gives us

![[Pasted image 20221218132615.png]]

This means the centroids are already on top of one another so we only need to rotate to align the point-clouds. With the 'simplified approach' we have

![[Pasted image 20221218132702.png]]

But $\det C=-1$ so $C\not\in SO(3)$, so we need to use the more rigorous approach. We perform SVD on $W$ to give 

![[Pasted image 20221218132813.png]]

Then $\det W=-4/3>0$ and there is a unique minimum singular value. So we need to use the solution from case 1:2. This gives $S=\text{diag}(1,1-1)$ and so since $C=UDV^T$ we have $$C=\text{daig}(-1,-1,1)$$so now $\det C=1$. This is a rotation about the axis $1_3 by the angle $\pi$. Here the minimum $J=4$ is reached.