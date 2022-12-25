What needs to be performed in the task of object detection? #flashcard #MOB #ObjectDetection
	In object detection we need to find the bounding boxes and classes for different objects in the scene.

---
What kinds of things make the task of objects detection hard? #flashcard #MOB #ObjectDetection 
	Object detection is made hard by a variety of things such as 1) Occlusion, 2)Truncations, 3)Scale distraction, 3) Illumination changes

---
What is truncation in image perception? #flashcard #MOB #ObjectDetection 
 An object is **truncated** if part of it is cut of by the edge of the sensor.

---
what is scale distraction in image perception? #flashcard #MOB #ObjectDetection 
	**Scale Distraction** is where objects change size as they move about.

---
What type of network is used to perform object detection in general? #flashcard #MOB #ObjectDetection 
	**ConvNets** are usually used for this task.

---
What does IoU stand for? #flashcard #MOB #ObjectDetection 
	IoU stands for **Intersection** over **Union**.

---
How is IoU calculated? #flashcard #MOB #ObjectDetection 
	IoU is calculated by find the area of intersection between the two boxes and the area of union. We then take the intersectional area over the union area $$\text{IoU}=\frac{\text{Area of Overlap}}{\text{Area of Union}}$$

---
What is IoU used for? #flashcard #MOB #ObjectDetection 
	IoU is a metric used to establish the similarity between two bounding boxes. It is 1 when the boxes are the same and 0 when there is no similarity.

---
When given and IoU score and an object class score how can a true positive be defined? #flashcard #MOB #ObjectDetection 
	Here we have identified the object ($\text{IoU}>\text{threshold}$) and we are confident it is the true class ($c_i>\text{threshold}$).

---
When given an IoU score and object class score how can a false positive be defined? #flashcard #MOB #ObjectDetection 
	Here we have not identified the object ($\text{IoU}<\text{threshold}$) have identified the correct class ($c_i>\text{threshold}$).

---
When can a false negative be defined given a list of detected objects with bounding boxes? #flashcard #MOB #ObjectDetection 
	This is the number of objects that haven't been detected.

---
How is the precision of a model defined with respect to the number of true positives and false positives? #flashcard #MOB #ObjectDetection 
	The **precision** is defined for $TP$ true positives and $FP$ false positives as: $$\text{precision}=\frac{TP}{TP+FP}$$ So is the fraction of identified objects that are correct.

---
How is recall of a model defined with respect to the number of true positives and false negatives? #flashcard #MOB #ObjectDetection 
	The **recall** is defined for $TP$ true positives and $FN$ false negatives as: $$\text{precision}=\frac{TP}{TP+FN}$$ That is the percentage of objects correctly identified.

---
What curve is defined by varying the threshold used to calculate precision and recall? #flashcard #MOB #ObjectDetection 
	This is the PR-curve where each threshold value will define an $x$ and a $y$ value of precision and recall for a given threshold.

---
What is AP with respect to a PR-curve? #flashcard #MOB #ObjectDetection
	AP is average precision and is defined as the area under the PR-curve.

---
What parts are needed for a basic object detector model? #flashcard #MOB #ObjectDetection 
	This will need a **feature extractor**, possibly some concept of **prior boxes**, **output layers** and **NMS.

---
What is a feature extractor in a object detection model? #flashcard #MOB #ObjectDetection 
	A **feature extractor** is a network designed to take our input image and extract useful features we can use to deduce where objects are.

---
What are prior boxes used for in object detection models? #flashcard #MOB #ObjectDetection 
	Our model needs some idea of where things could be in the scene one way to imbed this is to give the model some **prior boxes** which it will then fit to the image and modify slightly.

---
What do the output layers in an object detection model produce? #flashcard #MOB #ObjectDetection 
	These layers produce the actual boxes and confidence values for each class for them.

---
What does NMS stand for? #flashcard #MOB #ObjectDetection 
	This stands for **non-max-suppression** and is where we filter the many boxes given by the network to ensure only one box is used per object.

---
What is VGG'16? #flashcard #MOB #ObjectDetection 
	**VGG'16** is an architecture for convolutional networks that takes two **convolution layers** with 0 padding and 1 stride (hence don't reduce tensor width and height). Followed by **convolution layers** which half the size of the matrix with 2 stride. The **depth** of the network is increased as we get deeper into the network.
	
---
How are prior boxes fit to an image after a convolutional feature extractor? #flashcard #MOB #ObjectDetection 
	Deep in the network at this point there will be a small size of image. We take a 3x3 convolution for each pixel to give a vector which we can perform regression on to give box positions deviations and class confidences.

---
How is NMS performed? #flashcard #MOB #ObjectDetection 
	NMS is performed by taking boxes in order of confidence. Then every box that has a high enough IoU with this box we remove. We repeat this for all remaining boxes.

---
How is NMS treated at training time usually? #flashcard #MOB #ObjectDetection 
	NMS is usually ignored during training to get more error feedback into the network per computation.

---
What is Minibatch selection when it comes to object detection? #flashcard #MOB #ObjectDetection 
	Minibatch selection is where we filter our loss function to only take example that are clearly wrong or right this is to ensure the network doesn't become confused.

---
What are negative anchors when it comes to having prior boxes in our network? #flashcard #MOB #ObjectDetection
	Negative anchors are spots in our image where boxes are generated but there are no objects to detect. Hence our network never could have generated a correct box.

---
What is control training bias? #flashcard #MOB #ObjectDetection
	Here we use a batch with a 3:1 ratio of negative to positive anchors to ensure the network isn't biased to detecting empty boxes.

---
What is hard negative anchor mining? #flashcard #MOB #ObjectDetection 
	Here we add extra examples to our batch of background with high classification loss to ensure the network learns to identify background elements well.

---
