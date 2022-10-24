Why is it a bad idea to try to use conceptions from low dimensional space in high dimensional space? #flashcard #MachineLearningUni #HighDimensionalStatistics
	High dimensional space behaves very differently than what we expect with lower dimensional space. Therefore we should be careful not to use our conceptions as this can lead to strange problems...

---
Why is the volume of a circle coventrated around the crust in high dimensions? #flashcard #MachineLearningUni #HighDimensionalStatistics
	The volume of a sphere is in any dimension proportional to $cr^d$ for some dimensional constant $c>0$. This means that decreasing the radius by some small fraction $\epsilon$ will leave the internal reduced volume exponentially smaller in the size of $\epsilon$ and $d$. $$\frac{V((1-\epsilon)r)}{V(r)}=\frac{(1-\epsilon)^dV(r)}{V(r)}=(1-\epsilon)^d\le e^{-\epsilon d}$$

---
How does the volume of a unit ball change in different dimensions? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	The higher the dimension the small the ball and this happens vanishingly quickly where after ~10 dimensions the volume is almost nothing.

---
What is the distance to a d-dimensional unit cube's corner from its center? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	The distance to the edge from the center is always $\frac12$. Then the distance to the corner is a sum of the squared distances in all the d dimensions to it. That is $\sqrt{\sum_{i=1}^d\left(\frac12\right)^2}=\sqrt{\frac d4}=\frac{\sqrt d}4$. Hence as $d$ grows so does the distance to the corner despite the volume of the cube not increasing.

---
Why does a unit cube in high dimensions poke out of a sphere with radius that would encapsulate it in lower dimensions? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	This comes from the fact that the distance to the corners grows with the root  of the dimensions. But the distance to the spheres edges always stays the same hence in high enough dimensions any cube will poke out of any arbitrarily sized sphere.

---
How do we know the mass of a high dimensional cube is concentrated in its corners? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	We know the volume of a fixed radius sphere shrinks to nothing with the dimensions. Hence a cube of fixed side length will have a sphere fit inside it. But as the dimensions grow we know the volume of this sphere shrinks. The cube is the same volume therefore it's volume must be in the corners.

---
Why would we say a sphere is high dimension has all its mass about its equator? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	The volume in a hemisphere $\epsilon$ above the equator shrinks exponentially with the number of dimensions and the root. Therefore it approaches 0 for some number of dimensions meaning all the volume left over must be in the sliver $\epsilon$ above and below the equator.

---
What is the average distance between two vectors in high dimensions? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	This would approach $\sqrt 2$ as the number of dimensions increases. Meaning in  high dimensions a sample of points is likely to be equally spaced apart

---
Why are gaussian distribution in high dimensional space like soap bubbles? #flashcard #MachineLearningUni #HighDimensionalStatistics 
	In high dimensional space the probability some vector in a gaussian distribution has a length larger than $\sqrt d$ is exponentially small hence since the volume in the center also goes to 0 gaussians are like soap bubbles.

---
