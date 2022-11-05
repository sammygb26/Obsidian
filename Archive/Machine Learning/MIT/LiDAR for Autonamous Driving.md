# LiDAR for Autonomous Driving
LiDAR uses a laser that moves around using a scanning mechanism. The light that bounces back is recorded by a sensor. The time taken to come back depends on the distance of the object. Photons can also come from the sun and this bust be taking into account. This is all taken through a detector into a system signal and more noise comes here.

![[Pasted image 20220528112830.png]]

The noise overall can be improved by the above equation. The requirements will depend on the number speed and so requirement on speed and frame rate. The car needs to maximize *safety* and *comfort* (speed etc.). Hence we need prediction to be smooth in this way. We will need to classify what things are what far away. A higher resolution allows better prediction for further away objects. We need this resolution also to understand objects in the distance hence we need enough data to allow our system to decide. Range and frame rate isn't important if we cannot have enough resolution to see the object until it is close. Hence *vertical resolution* is important. 

We can determine collision relevance by comparing the distance of pixels above each other based on distance. This way a simple algorithm can make safety much more solid and so we can rely on it. This is important when our systems are safety critical. It may not be completely important to decide what an object is when we can simply detect objects and add bounding boxes to track movement.

### Deep Learning with Point clouds
We need to represent point clouds in data and so perform deep learning one them. The first key is that the data is unstructured so the order we represent is in shouldn't matter.  Another problem with point clouds is the data will be clustered around the car and will get far sparer far away. We can also represent the point clou as a *front view*. We make it into an image that perfectly encodes the distance and position of the image. We can also use *voxelization* where we take a volume we are working with and break this up into smaller volumes. This gives a structure to how close together points are.

![[Pasted image 20220528115806.png]]

We may also need to represent *occlusion maps* that take into account what objects are blocking which to give more information to our network.  We can combine deep learning and classical techniques to get a more white box approach taking everything into account. 
