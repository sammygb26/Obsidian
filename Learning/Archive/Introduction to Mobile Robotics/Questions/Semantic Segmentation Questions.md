What is semantic segmentation? #flashcard #MOB #SemanticSegmentation
	This is a task where we take an input image and then convert it to a new image where each pixel represents the class of the object that pixel was part of in the original image.

---
What is our model trying to learn in semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	Our model is trying to learn a function taking an image to and image that groups classes of objects together.

---
What are some things that make semantic segmentation hard? #flashcard #MOB #SemanticSegmentation 
	**Semantic Segmentation** is made hard by occlusion, truncation, scale and illumination changes and smooth boundaries.

---
Why are smooth boundaries hard in semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	These are hard due to ambiguity and resolution limitations.

---
What type of network is usually used to perform semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	**ConvNets** are usually used for this as they work well with image data.

---
What are true positives, false positives and false negatives for a given class in semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	**True positives** are correctly classified pixels, **false positives** are wrongly classified our class and **false negatives** are in our class but classified wrongly.

---
How is IoU defined for a class in semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	This is described as the true positives $TP$ over the true positives plus the false positives $FP$ and the false negatives $FN$. This is $$\text{IOU}_{\text{class}}=\frac{TP}{TP+FP+FN}$$ So its the total number of correctly identified pixels divided by the total number of pixels either identified as the class or actually in the class.

---
What 3 steps are needed for a basic semantic segmentation model? #flashcard #MOB #SemanticSegmentation 
	We need a **feature extractor** to understand the scene **output layers** to understand where classes should be and **subsampling** to get an output of the same size as the original image.

---
Why does basic up sampling not work? #flashcard #MOB #SemanticSegmentation 
	Basic upsampling just caused pixilation and low amounts of data spread over more and more pixels this causes thin and far away objects to be lost in the output.

---
What solution is commonly used for the up sampling problem in semantic segmentation? #flashcard #MOB #SemanticSegmentation
	A decoder is used where convolutions take place in-between upsampling layers. This is similar to an autoencoder and results in a image where much of the detail in maintained.

---
How is loss for semantic segmentation calculated? #flashcard #MOB #SemanticSegmentation 
	The output from the network will be probabilities for each class for each pixel we can take a **cross-entropy-loss** therefore.

---
When upsampling what is a better technique that simple multiplier upsampling? #flashcard #MOB #SemanticSegmentation 
 We can instead perform 0 padding with max indices. We use the **max-indices** generated during max pooling to perform the reverse just for every pixel we are missing an index replace with a 0. This is better as it gives the network more fine grained information.

---
How is scene estimation performed after semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	Here we can take different segments and use them to generate the **drivable surface** aswell as estimate object positions like people and lamp-posts.

---
How can RANSAC be used to find surfaces in scene estimation following semantic segmentation? #flashcard #MOB #SemanticSegmentation 
	We can select three non-collinear points then compute the plane parameters by solving for 4vector plane normal. Then we can check the inlier number is over a given amount. If it is we have found our plane and if not we continue.

---
What is semantic lane segmentation? #flashcard #MOB #SemanticSegmentation 
	Here we also estimate the position of lane area within an image to further specify where our car can drive.

---
What is instance segmentation? #flashcard #MOB #SemanticSegmentation 
	Here we don't just label object classes but instead also individual object instances. Say 'person1' and 'person2'.

---
