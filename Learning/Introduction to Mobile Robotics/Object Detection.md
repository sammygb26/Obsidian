We need for formulate the problem as a neural network problem. 

![[Pasted image 20221010111328.png]]

We need to find the location of the objects bounding boxes and what is in the box. This is a **hard problem** as there are many problems such as *occlusion* (background object covered by foreground objects) and *truncations* where part of the object is cut of by out partial view. **Scale distraction** where objects change is size as the move about. **Illumination** there an be too little or too much light.

##### Formal definition
We want to locate the presence of objects with a *bounding box* and *classes*. The **input** is an *image* with one or more objects. The **output** is one or more *bounding boxes* defined by a point and a witch and a height and a *class label* for each bounding box.

**ConvNets are used for this**
![[Pasted image 20221010111805.png]]

##### Evaluation Metrics
We need to define a metric to give the network to optimize over. For this **IoU** is commonly used.

![[Pasted image 20221010111856.png]]

![[Pasted image 20221010111915.png]]

This can give values from 0 to 1. We use this *IoU* metric to define some more metrics.

**True Positive** - Object class score > score(threshold) and IoU > IoU (threshold)
**False Positive** - Object class score > score(threshold) and IoU < IoU(threshold)
**False Negative** - Number of ground truth objects not detected/returned by algorithm.

Then we define *precision* $TP/(TP+FP)$ and *recall* $TP/(TP+FN)$. 

We use this to define a *precision recall curve* (PR-curve) where we use multiple threshold values to compute precision and recall.

![[Pasted image 20221010112332.png]]

*Average Precision (AP)*: Area under curve (PR-AUC) for a single class (can be approximated with ~11 recall points between $[0,1]$)

*Mean AP (mAP):* the average AP over all object classes.

![[Pasted image 20221010112620.png]]

![[Pasted image 20221010112732.png]]

We can work with different values for the thresholds and get different precision and recall values. This then gives us out own char.

![[Pasted image 20221010112859.png]]

### CNN for Object Detection
We will use a special architecture for this task. We first have a *feature extractor* which is layers of convolution layers. We can then combine this with *prior boxes* used in training then we have some dense layers processing this information together and an *NMS* to reject boxes.

![[Pasted image 20221010112948.png]]

##### Feature Extractor
This is the **most computationally expensive** component of the 2D object detector. The output feature usually have much lower height and width but very large depth.

![[Pasted image 20221010113237.png]]

##### VGG'16
This is an architecture for convolution networks. The idea is we have **alternating** convolution and pooling layers. All *convolution layers* are of size 3x3xK, with stride 1 and 1  zero-padding. All *pooling* layers use the max function and are of size 2x2 with stride 2 and no padding.

![[Pasted image 20221010113431.png]]

![[Pasted image 20221010113557.png]]

![[Pasted image 20221010113546.png]]

![[Pasted image 20221010113626.png]]

##### Prior anchor Bounding Boxes
Instead of finding bounding boxes from scratch we assume we do have a prior about *where* they are and **how large they are**. These *manually* defined boxes are called prior or anchor boxes.

The *boxes* are moved as close a possible to the ground truth bounding box. The we also match the box dimensions.

![[Pasted image 20221010114131.png]]

![[Pasted image 20221010114158.png]]

![[Pasted image 20221010114217.png]]

We take the $1\times1\times D^*$ and feed it through a classifier and regression layers to get the class and to fit the box.

##### Output handling (NMS)
*Non-max-suppression* - There are many different boxes for different candidates but we need to pick which to use.

![[Pasted image 20221010114440.png]]

We sort the list of boxes by their classification scores $\bar B$ and we initialize some $D$ to be empty. Then we take the $b_{max}$ with the highest classification value. We add $b_{max}$ to $D$ and remove it from $\bar B$. Then for everything else in $\bar B$ we remove every box if it overlaps too much with our picked $b_{max}$ we discard it. If it doesn't overlap then it may be picked as our next $b_{max}$.

![[Pasted image 20221010114504.png]]

### Training
We don't train **NMS** as it is just an algorithm and we get more feedback into our network when we don't perform NMS.

![[Pasted image 20221010115033.png]]

##### Minibatch
We take batches of example to train the network as not to overload the GPU. We use this batch to calculate the loss and gradients. But we also filter out outputs and remove *mid-scoring values* to ensure the network isn't confused.

![[Pasted image 20221010115320.png]]

There will be many boxes where there is nothing in the network. These are called **negative anchors**.

![[Pasted image 20221010115435.png]]

*Control training bias* - Here we take some batch with a 3:1 ration of negative to positive anchors to ensure the network isn't biased towards negative examples.

*Hard Negative Anchor Mining* - Chose negative with high classification loss to be included in minibatch (hard examples).

![[Pasted image 20221010115656.png]]

[[Object Detection Questions]]
