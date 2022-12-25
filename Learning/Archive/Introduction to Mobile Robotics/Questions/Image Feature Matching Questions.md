How overall is image feature matching performed?  #flashcard #MOB #ImageFeatureMatching
	We first find *features* in both images. We then match these features to allow us to move one image over the other.

---
What are the five keys things a good features needs? #flashcard #MOB #ImageFeatureMatching 
	A good feature needs to be **Salient**, **Repeatable**, **Local**, **Efficient** and a **Quantity** of features is needed.

---
What does saliency mean when it comes to features?  #flashcard #MOB #ImageFeatureMatching 
	A **salient** feature is a distinctive, identifiable and different from its neighborhood.

---
What does repeatability mean when it comes to features?  #flashcard #MOB #ImageFeatureMatching 
	A **repeatable** feature can be found even under some distortion (movement, time passing)

---
What does **locality** mean when it comes to features?  #flashcard #MOB #ImageFeatureMatching 
	A **local** feature is one that occupies only a relatively small subset of image space.

---
What does it mean for a feature to be **efficient**?  #flashcard #MOB #ImageFeatureMatching 
	A feature is **efficient** if it is easy to compute in terms of time and resources needed.

---
Broadly what makes good features?  #flashcard #MOB #ImageFeatureMatching 
	**Texture less patches** are a bad choice while **edges** and **corners** are good as their not easily mistaken for patches around them.

---
How does Harris Corner Detection work?  #flashcard #MOB #ImageFeatureMatching 
	In Harris Corner detection we sweep around some area and map intensity. If we find two competing directions with large changes then we have found two edges and so a corner.

---
What is a problem with Harris corner detection?  #flashcard #MOB #ImageFeatureMatching 
	Harris corner detection isn't **scale invariant** that is at a small scale it can detect an edge but not at a large scale and if we zoom in on a corner.

---
What are feature descriptors?  #flashcard #MOB #ImageFeatureMatching 
	Feature descriptors are summaries of the look of some local feature. The idea is that they sum up the information of a feature in a way that allows us to allows them to be compared to other descriptors.

---
What are the three required properties of a good descriptor?  #flashcard #MOB #ImageFeatureMatching 
	A good descriptor is **repeatable**, **distinctive** and **compact & efficient**.

---
What does it mean for a descriptor to be repeatable?  #flashcard #MOB #ImageFeatureMatching 
	A descriptor is **repeatable** when it is robust and invariant to rotation, scale and illumination.

---
what does it mean for a descriptor to be distinctive?  #flashcard #MOB #ImageFeatureMatching 
	This means a descriptor should be easily distinguished form close-by features.

---
What does it mean for a descriptor to be compact and efficient?  #flashcard #MOB #ImageFeatureMatching 
	A descriptor is compact and efficient if it doesn't take a lot of computational resources to find, store and compare.

---
What does SIFT stand for?  #flashcard #MOB #ImageFeatureMatching 
 **Scale Invariant Feature Transform**

---
What are the 4 steps to make a sift descriptor?  #flashcard #MOB #ImageFeatureMatching 
	To make a sift descriptor we first **find a 16x16 window around the feature**. Then we separate the neighborhood into **16 cells** so each cell is 4x4. The for each cell we find the most prominent gradient change direction. With this we create an **8-bin histogram** to describe the cell. We then **concatenate** all bins from all sections into a 128-dimension vector reading the cells like a book.

---
What is the aim of feature matching?  #flashcard #MOB #ImageFeatureMatching 
	In feature matching we are given a list of feature descriptors. The job is to match the descriptors to the most similar descriptors. Hence we match points in the image space of two images.

---
How can compare descriptors?  #flashcard #MOB #ImageFeatureMatching 
	We need some distance function to compare descriptors. For this we can use distance function like Sum of Squared Differences or Sum of Absolute Differences of Hamming Distance.

---
How would a brute force method for matching descriptors work?  #flashcard #MOB #ImageFeatureMatching 
	We would define some distance function $d$ and **threshold** $\delta$ then for every feature $f_i$ in image 1 we compare it to all $f_j$ in image 2. Then we find the *closest match* in image2 from image 1. Then we remove all matches not over the threshold if perhaps the feature isn't in the second image.

---
What is the localization problem in image feature matching?  #flashcard #MOB #ImageFeatureMatching 
	Here we try to find some translation $T=[t_u,t_v]$ in the image coordinate system that move image1 over image2 to produce a match. We **localize** image 1 to image 2.

---
Given a collection of matched feature how can we localize via minimizing SSD?  #flashcard #MOB #ImageFeatureMatching 
	If we minimize SSD we will find values for $t_u$ and $t_v$ to be $$t_u=\frac1N\sqrt{\sum_i^N\left(u_i^{(1)}-u_i^{(2)}\right)}\hspace{16pt}t_v=\frac1N\sqrt{\sum_i^N\left(v_i^{(1)}-v_i^{(2)}\right)}$$

---
What is the goal of random sample consensus?   #flashcard #MOB #ImageFeatureMatching 
	In *random sample consensus* we are trying to remove the effect of outliers.

---
How does random sample consensus work?   #flashcard #MOB #ImageFeatureMatching 
	We pick $M$ matched features and calculate $T$ translation from img1 to img2 using these. We then compare how many samples from the rest of the data still fit the model. If this number is over some inlier ratio then we return this inlier set else we pick a new $M$ points.

---
What is an inlier?   #flashcard #MOB #ImageFeatureMatching 
	An inlier in terms of random consensus is a point that fits in with some other set. That is for some translation $T$ the error between matched features is small.

---
How is visual odometry performed?   #flashcard #MOB #ImageFeatureMatching 
	In visual odometry we use matched feature to estimate translation and so motion and rotation between different frames.

---

