Don't try to use any of your intuitions in high dimensional space. Different object can be represented as a high dimensional objects. For example a $28\times 28$ image is just $28^2$-vector. Or an English word would for one-hot would be a 20000-vector for 20000-word vocabulary. We tent to extrapolate intuitions from two and three dimensions to higher dimensions. But many intuitions fail to hold at higher dimensions.

### Volume Concentrations
The volume of a ball with radius $r$ is:

![[Pasted image 20221020151843.png]]

If we shrink the radius by a small amount $\epsilon$ the volume shrinks:

![[Pasted image 20221020151914.png]]

The last inequality uses $1-x\le e^{-x}$. This means as $d$ increases the rations goes to 0 as $d$ grows. This means at high dimensions the volume of the inner ball compared to the outer is **arbitrarily small** at higher dimensions. The volume is **concentrated at the crust** at higher dimensions.

![[Pasted image 20221020152234.png]]

At higher dimensions most of the ball is at the crust (green). We can look at a graph of how much of the volume exists at the crust:

![[Pasted image 20221020152324.png]]

##### Unit ball
If we take the equation again and set $r=1$ we get:

![[Pasted image 20221020152432.png]]

Then $\Gamma(x+1)~\sqrt{2\pi x}(\frac x e)^x$ meaning it grows with $x^x$ and so gets large very fast. The volume of the ball can be graphed as:

![[Pasted image 20221020152548.png]]

### Corners of the Unit Cube
We can take a unit cube centered at 0 with a side length of 1. The length to the corner is $2{\sqrt{{\frac12}^2}}$.

![[Pasted image 20221020152632.png]]

This can be generalized to $d$ dimensions the distance becomes

![[Pasted image 20221020152837.png]]

 The distance come from the fact that in $d$ dimensions the distance is $$V=\sqrt{\sum_{i=1}^d\left(\frac12\right)^2}=\sqrt{\frac d4}=\frac{\sqrt d}4$$Hence the distance to the corner grows. Then if we put this in a unit ball for 2D we get:

![[Pasted image 20221020152918.png]]

As $d$ increases the corners point out the side

![[Pasted image 20221020152946.png]]

The volume goes to 0 inside the ball but its volume is still 1 hence all the mass is in the corners.

![[Pasted image 20221020153032.png]]

### Volume near the Equator
If we pick a north direction we can compute the volume around the equator. At high dimensions all the mass get concentrated at this direction. We pick some $\epsilon>0$ the width of the slab. The volume above is about: $$\frac2{\epsilon\sqrt d}e^{-d\epsilon^2/2}$$Hence as $d$ grows this all goes to 0. So the green area below in high dimensions approaches 0.

![[Pasted image 20221020153510.png]]

Because of this if we pick a random vector inside the ball it is likely to be on the equator. Hence if we pick two random vector their dot product is likely to be very close to 0. 

### Distances of two random vectors
Any two random vector $u$ and $v$ are likely orthogonal meaning $u^Tv$ is likely to be small. The volume is concentrated at the crust so $||u||$ and $||v||$ are likely to be close to 1. The distance of any two random vector is likely to be about $\sqrt2$. We can look at a histogram of this at high dimensions. Then most points will have the same distance.

![[Pasted image 20221020154148.png]]

This makes this hard when we have say KNN then everything will be an equal distance apart. Hence we are almost picking a random point as they are all a similar distance apart.

### Norm of random Gaussian Vectors
For any $x\sim\mathcal N(0,1)$

![[Pasted image 20221020154424.png]]

That is the probability the norm squared of our gaussian vector -1 is above epsilon. Is always smaller than $\exp{\frac{-d\epsilon^2}x}$. That is the norm squared divided by $d$ is very close to 1.

![[Pasted image 20221020154740.png]]

This means gaussians in high dimensions are like soap bubbles.

[[High Dimensional Statistics Questions]]