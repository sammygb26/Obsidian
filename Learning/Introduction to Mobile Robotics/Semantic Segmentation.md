# Semantic Segmentation
Semantic segmentation is the task of generating a map of what is in an image. We give a label to every pixel of what it is part of.

![[Pasted image 20221013111129.png]]

### Semantic Segmentation Problem
![[Pasted image 20221013111310.png]]

We are trying to groups parts of the image together. The idea being that they *belong together*. We break this down to *pixel level predictions*. For we we need a **function estimator** for each pixel.

![[Pasted image 20221013111457.png]]

![[Pasted image 20221013111533.png]]

There are many issues that makes this task harder for example *occlusion*, *truncation* and *scale and illumination changes*. It is also hard to make **smooth boundaries** due to ambiguity and resolution limitations.

![[Pasted image 20221013111724.png]]

##### Formulation
![[Pasted image 20221013111831.png]]



These metric are defined for a given class. Just as in object detection we will have *true positives* (correctly classified pixels for a given class), *false positives* (pixels wrongly classified for a given class), *False Negatives* (missed correct classifications for a given class).

![[Pasted image 20221013112133.png]]

![[Pasted image 20221013112237.png]]

![[Pasted image 20221013112256.png]]

### ConvNets for Semantic Segmentation
![[Pasted image 20221013112456.png]]

We need a **feature extractor** to identify patterns and object information in the image.

![[Pasted image 20221013112558.png]]

A good one to use is VGG'16 we stop earlier in this case and reach a larger output feature volume (4 convolutions $2^4=16$ times smaller.

![[Pasted image 20221013112700.png]]

We only have a 16 times smaller version but we need to map it back to the normal size. If we just just apply a SoftMax classification layer at the end we will get a low resolution segmentation. We will be using *nearest neighbor* we get 

![[Pasted image 20221013112922.png]]

![[Pasted image 20221013112948.png]]

Small and thin object will disappear with this naïve method. We can instead add a **feature decoder into the network** which will perform a smarter upscaling. Feature extractor is also called a *feature decoder*.

![[Pasted image 20221013113156.png]]

![[Pasted image 20221013113224.png]]

So rather than directly applying SoftMax on our feature volume after extraction we then perform the same upscaling on these features before performing SoftMax over the top.

![[Pasted image 20221013113424.png]]

![[Pasted image 20221013113524.png]]

We get a *SoftMax* output for each pixel and we can compare it to **ground truth** *one-hot-encoded* vector.  We then take a cross entropy loss for each pixel.

![[Pasted image 20221013113628.png]]

![[Pasted image 20221013113701.png]]

**Max-Pooling indices** can be used where we store the indices which were taken when pooling original. We can then use these indices to place the values from the downscaled version and replaced the rest with 0s.

![[Pasted image 20221013114104.png]]

It is then the convolution layers job to fill in these 0s.

### Scene Estimation
1. Generate semantic segmentation output
2. We can associate 3D point coordinates from lidar with 2D image pixels.
3. Choose 3D points (*blue* on the right feature) belong to the **drivable surface** trajectory.
4. estimate 3D drivable surface model with the chose points

![[Pasted image 20221013114428.png]]

We then take a set of points for a surface and solve for the normal of the surface. We have three parameters so we need three colinear points.

##### Outliers
We can use **RANSAC** to find outliers just as before.

![[Pasted image 20221013114608.png]]

When we stop the *inliers* are used to estimating the surface.

### Semantic Lane Segmentation
We can estimate the **lane** areas where the car can drive on the driven surface. We want to estimate the **boundaries** of the lane:

![[Pasted image 20221013114752.png]]

### Instance Segmentation
We we want to find not just object but also what instance they belong to. We want individual object identification.

![[Pasted image 20221013114841.png]]

This is a more complicated task:

![[Pasted image 20221013114959.png]]

Mask R-CNN gets around prior boxes and proposes regions itself. We have three output heads for this network *Mask*, *Classification* and *boundary boxes*.