# Cameras and Images
Cameras are one of the major solutions to perceptions and can do most of the heavy lifting.

### Human/Robot Vision
30-50% of the human brain focuses on image perception. Hence vision is the most important sensing system in humans. Just like this cameras are used as the primary sensor in our robots. The dream is to work at the same level as the human brain.  We can see similarities in how the human brain works just as humans break down sensory information computers break down matrices of numbers produced by computers.

![[Pasted image 20220929111635.png]]

### Physics of Cameras
To measure a scene we need a light source who's light bounces of objects in the scene. This bounced light is sensed to understand the scene. The sensory senses the amount of photons hitting it. This is then relayed to the computer and interpreted into binary numbers.

![[Pasted image 20220929111815.png]]

There are two types of images *greyscale* and *colored*. Greyscale images only have a brightness of each pixel while RGB images have three for Red Green and blue.

![[Pasted image 20220929112042.png]]


![[Pasted image 20220929112052.png]]

### Image Formation
With just one point we can sense objects directly on the sensor. But with more than one we get blurring. Instead we can use a *pinhole camera*. Hence all the light comes form this little point and so each point on the sensor only corresponds to what can be seen out from the point from its POV.

![[Pasted image 20220929112220.png]]

The position of the *pinhole* is called the **optical center** $C$. Where as the distance from $C$ to the image place is called the *optical length* $f$.

![[Pasted image 20220929112422.png]]

We can take the gradient of a point given some $z$ (distance from $C$ value).

![[Pasted image 20220929112531.png]]

This develops the following rule for the $y'$ and $x'$ values on the image plane.

![[Pasted image 20220929112609.png]]

We take a projection instead to a furth forward plane to develop a virtual image that isn't flipped.

![[Pasted image 20220929112726.png]]

Hence we are translating World Coordinates to Image Coordinates.

### Stereo Cameras
Distance measurement can be made by LiDAR however **stereo cameras** can also be used. We compare the differences in images from two close cameras to get *estimated depth*. We assume two *identical* cameras and *parallel* optical axes.

![[Pasted image 20220929113117.png]]

We know $O_L$ and $O_R$ and we want to solve for $Z$ (distance) and $X$ (position). To do this we need to detect the same $O$ objects in both images.

![[Pasted image 20220929113304.png]]

We can compare the two triangles between $C_L$, $Z_L$ and $O$ and $C_R$, $Z_L$ and $O$.  We already have the equations describing $x_L$ and $x_R$ in terms of $f$, $Z$ and $X$. We need to note that the $X$ values is calculated relative to $C_L$ so the true $X$ values for $C_R$ is $X-b$. Where $b$ is the distance between $C_R$ and $C_L$. This allows us to derive:

![[Pasted image 20221001184255.png]]

Where $d$ is *disparity* it the difference in the $x_L$ and $x_R$ values in the image plane.

![[Pasted image 20220929113641.png]]

This all works out as we assume $Z_L=Z_R$ as this is almost true for cameras that are close together and objects that are far from them relative to their distance $b$. That is $Z$ is much greater than $b$.

### Image Filtering
The task here is to take a noisy image and *denoise* it to make it more useable. An example would be replacing outlier pixels with the average of their neighbors. This happens for all pixels not just the outliers (although this can be done).

![[Pasted image 20220929113959.png]]

We can write the formally as follows.

![[Pasted image 20220929114047.png]]

The filter size will be $2k+1$ and $(u,v)$ is the center of the pixel we are filtering.

##### Cross-correlation
A mean filter is a special case of a foamily of *cross-correlation filters*. For example a **gaussian filter** is another.

![[Pasted image 20220929114242.png]]

We can see that the mean filter is blurring the image more while also denoising it.

![[Pasted image 20220929114259.png]]

Cross-correlation or the kernel concept can be used for *image gradient computation* aswell.

![[Pasted image 20220929114419.png]]

[[]]

[[Camera Questions]]