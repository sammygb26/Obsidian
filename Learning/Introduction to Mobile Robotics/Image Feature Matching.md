# Image Feature Matching
We may have many images and want to *stitch* them together into one whole image.

![[Pasted image 20221003111004.png]]

The general process takes three steps **feature detection**, **feature description** and **feature matching**.

![[Pasted image 20221003111106.png]]

We use the same process as in *depth cameras* $O_R$ and $O_L$ to localize the object.

### Feature Detection
*Features* are points of interest. They need 5 things to be good features.

![[Pasted image 20221003111158.png]]

Repetitive *texture-less patches* are bad choices as they are hard to localize. Patches with large contrast changes (gradients) are easier to localize (**edges**).

![[Pasted image 20221003111513.png]]

##### Harris Corner Detection
This is an algorithm used to detect corners in an input image:

![[Pasted image 20221003111533.png]]

Given a pixel we examine its intensity change in all directions. We record this via *sobel operation*. We then find the **largest** and **second largest** magnitudes of pixel gradients. If they are both large enough this implies two edges in two directions are found hence two corners.

The **scale of the image matters** a small round corner will be classified as such but a larger scaled up corner doesn't.

![[Pasted image 20221003111924.png]]

##### Feature Detection Algorithms (improved versions)

![[Pasted image 20221003112009.png]]

### Feature Descriptors
A **feature** is a point of interest defined by its image pixel coordinates $[u,v]$. **Descriptor** is an *N-dimensional* vector that provides a *summary* of the local neighborhood of information around the feature. An effective feature should have the following characteristics:

1. *Repeatability* robust and invariance to translation, rotation, scale and illumination
![[Pasted image 20221003112245.png]]

2. *Distinctiveness* should allow to destinguish between two **close-by** features
![[Pasted image 20221003112330.png]]

3. *Compactness & Efficiency*: reasonably computation and time efficiency

##### Designing Invariant Descriptors: SIFT
This is the *Scale* *Invariant Feature Transform*. There are four steps:

![[Pasted image 20221003112529.png]]

The encoding moves around the orientations and along as if you were reading the descriptor. **SIFT** is a *human engineered* descriptor based on pixel gradients and is used in many state of the art systems. The process is computed on *rotated and scaled versions* giving multiple versions for a single point. This gives **robustness** so we try to match many versions at once. With neural networks we can do joint description and detection that reduces computation need.

### Feature Matching
**Given** a feature and its *descriptor* in image 1 and image 2 we want to find the *best match*.

![[Pasted image 20221003113026.png]]

A **good match** is defined as a distance function $d(f_i, f_j)$ that compares the two *D-dimensional descriptors* for every feature $f_i$ in image 1. We then compute *all* feature $f_j$ in image 2 and we find the *closest* having minimum distance. We can use many different distances.

![[Pasted image 20221003113232.png]]

![[Pasted image 20221003113254.png]]

We can find many *distances* are large so we specify a **threshold** to remove bad points. This gives the three steps

![[Pasted image 20221003113404.png]]

### Outlier Rejection
**Localization Problem** is we want to find a *translation* $T=[t_u,t_v]$ in image coordinate system between image 1 and image 2. That is we **localize** an object of image 1 to image 2.

![[Pasted image 20221003113546.png]]

We may find good matches:

![[Pasted image 20221003113605.png]]

But there will be **outliers** like the left most point. We formulate the problem as we have $N$ matches feature in image 1 and 2:

![[Pasted image 20221003113709.png]]

Then we have a translation model such that is we fund $t_u$ and $t_v$ such that

![[Pasted image 20221003113747.png]]

##### Solution Least Squares
We can solve this by finding $t_u$ and $t_v$ than minimizes $SSD$.

![[Pasted image 20221003113827.png]]

![[Pasted image 20221003113944.png]]

So if we pick and *outlier* we will have very few *inliers* and so a low $C$. With a good *inlier* we will find many points as inliers. Then we stop and compute translation parameters.

### Visual Odometry
Here given two consecutive images $I_{k-1}$ and $I_k$ we **extract and match** features. Then we use this to *estimate* motion between frames to get $T_k$:

![[Pasted image 20221003114438.png]]

[[]]