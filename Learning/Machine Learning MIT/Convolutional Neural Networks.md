# Convolutional Neural Networks
Vision can be very important to humans so it is also important for our machines to understand. This has been a very important use of machine learning and has helped diagnose disease, drive cars and help visually impaired people.

## Images are Numbers
We can encode a pixel as grayscale, the light level would then be the value for that pixel. The whole thing can be made out of a matrix that is the same scale as the image. If we want to have multiple colors we can then add more channels.

## Tasks for Compute Vision
Two common task we will do with this are recognition or *classification* and *regression* (quantitative analysis). With *regression* our output is a continuous value and with *classification* we can produce a probability of belonging to a given class. 

#### Classification
We might wounder how this is done by the computer however. *Feature detection* is where we identify key features in each category we are looking to decide between. To build this we would need to apply some *domain knowledge* to *define features* at the end of this we *detect the features* in order to classify. But we would need to tell the computer all this as it is very hard to define these types of features ad there are many variations that features may take that will be very hard to detect.

With the neural network we extract and find features automatically instead of hand engineering them. They are generated to be resilient to changes through the data set having examples of these features in different variations. But how do we make a neural network that can extract these features.

## The Convolution
We can crush our whole 2D image into one long string and feed it into a fully connected neural network. This will have many parameters however since it is densely connected and we have destroyed all locality between pixels in our image. We want to preserve our spatial structure when we send images.

![[Pasted image 20220516153828.png]]

The other option in stead is to connect close pixels together feeding into our next layer. This reduces the number of weights we need as our neuron doesn't depend on the whole next layer. Then it also preserves locality as only local regions of pixels are considered.

![[Pasted image 20220516154047.png]]

We pass the same box all across the image. With the *same weights* as to extract any feature for the whole image. The feature extraction for the region is made via the weights on the patch. This sliding operation is called a *convolution*. For example with a $4\times4$ patch we have $16$ weights which we apply over our whole image. A each placement of the box we get a single pixels in the next layer.

A feature itself will be a sort of mini image that will detect a different piece of the image. Then the relation between the positions of these low level features are detected in the next layer. The local features preserve locality as the boxes are small.

The *convolution operation* works by summing the element wise multiplication of our convolution matrix with the corresponding portion of our larger matrix. The output of the convolution will be a feature map.

![[Pasted image 20220516154851.png]]

We continue for every possible location of the convolution matrix. A large amount of overlap will get a large value (feature detected) and a small overlap will get a small value.

![[Pasted image 20220516155150.png]]

Different values will extract different features.

## Make of a Convolutional Neural Network
To make a convolutional neural network itself we need three main elements. We want to learn features and then combine these to detect properties of the image to finally inform a classification (for a classification example). 

![[Pasted image 20220516155905.png]]

We need *convolutional* layers that take a number of filters (convolution matrices) that are learned by our network in order to detect features. We need to apply a *non-linearity* (often ReLU). We will also use *pooling* where we will further sample the feature maps in order to detect larger more abstract features.

#### Convolution Layers
Within a convolution layer we will have a single feature produce a new layer that is the *convolution* of the previous layer and the feature matrix. For a neural network version of this we will also apply a bias and pass through a non-linear activation function. Within each layer we have have multiple filters this will have a list of feature matrices for the next layer.

![[Pasted image 20220516160323.png]]


The *stride* is the filter step size in order to cover the image being processed. The *receptive field* will be the locations in the image a node is connected to. 

These extracted features will then have a *non-linearity* added to it. This basically performs a cutoff for the values that extracts only certain features. 

![[Pasted image 20220516160923.png]]

*Pooling is then applied* we use this to reduce the dimensionality of our feature maps aswell as preserving locality. For example above we take a max pool for many pools over the matrix to produce a new matrix preserving some of the key information of the first.

Overall this allows features to build up over layers.

![[Pasted image 20220516161118.png]]

## Overall
We can now take features and chain together convolution and pooling to get a small and smaller feature volume.

![[Pasted image 20220516161249.png]]

Finally we can expand this out to a fully connected layer to make a decision with our overall information about the image.

![[Pasted image 20220516161337.png]]

The first part extracts features and the second part makes s decision on them. Overall we can combine this in code to get our overall network.

## Versatility
The above discussion relates to image detection/classification however just by changing the second part of the network we can do far more that just classification. We can swap it out to do far more tasks. Like for example we can perform regression, object detection, segmentation or probabilistic control.

## Object Detection
So classification can detect if there is or isn't a taxi.

![[Pasted image 20220516161853.png]]

But a harder problem is to find the bounding box of the taxi.

![[Pasted image 20220516161926.png]]

But this may need to detect many objects if there are multiple objects in the scene.

![[Pasted image 20220516162038.png]]

One simple way we could do this is to place a random box in our image, pass that through a CNN and ask its class

![[Pasted image 20220516162209.png]]

We can then continue this for many different boxes. The problem is there are far too many boxes and images this makes the problem intractable. We could use a simple heuristic to detect where possible good boxes are. We then warp this down and pass it through a CNN.

![[Pasted image 20220516162338.png]]

But this is still *slow* as we have to solve every image separately. We can also be quite *brittle* as our region detection is separate from the rest of our network. One that works well is *faster R-CNN* which learn region proposals.

![[Pasted image 20220516162703.png]]

As this is all done in tandem it can be far more efficient.

## Semantic Segmentation
This is another task where we for each pixel detect what is the class of the pixel. With this we have a feature extraction which we will then use to learn to upscale using *transverse convolutions*.

![[Pasted image 20220516163024.png]]

This is also applied to biomedical analysis where we detect parts of say a brain that are affected by a disease.

## Continuous Control
This is another problem that would be involved in a car driving. Here we want to decide what the best say steering wheel angle is to take. For our car. We will be outputting a *continuous distribution* over our possible steering commands saying which ones are desirable.

![[Pasted image 20220516163313.png]]

We can train this end to end by first passing all cameras through their own feature detection matrices. We then pass all these through into a concatenated layer. We then predict our control parameters from this.

![[Pasted image 20220516163643.png]]

