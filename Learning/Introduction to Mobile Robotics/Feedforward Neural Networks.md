# Feedforward Neural Networks
A *Feedforward Neural Network* defines a mapping from some *input x* to *output y* as: $$y=f(x;\theta)$$Where $\theta$ is the weights. An $N$ layers FNN is represented as the function composition of these simple parts:

![[Pasted image 20221006111428.png]]

We can write this another way with nodes:

![[Pasted image 20221006111500.png]]

$x$ is called the *input layer* then the final function $f^{(N)}$ is called the *output layer*. The other function are the **hidden layers**. $\theta$ are the set of *learnable parameters* of all the layer functions.

### Functionality
**Object Classification** allows us to take an input say an *image* and return the *label*. **Object detection** is a task where we take a function taking in an image and the output is an object label and a location. 

![[Pasted image 20221006111814.png]]

**Depth** estimation can also be done from the single image with these networks.

![[Pasted image 20221006111800.png]]

We can also do **semantic segmentation** where we product a label for every pixel.

![[Pasted image 20221006111849.png]]

### Mode of Action of Neural Networks
We need to **train** the network to find some $\theta$ that best matches the output we want. This is done with *training data* where we have some $f^*(x)$ for given $x$ values. We train $\theta$ on these $x$ and how that it generalizes to unseen $x$ values. To do this we need good data form a variety of scenarios.

![[Pasted image 20221006112059.png]]

The way this system works we don't care about the *hidden layers* instead we only care about the output layers.

### Hidden units
The *hidden units* are the internal values passes between the network functions. We have some activation function $g$, $input $h_{n-1}$ weight matrix $W$ bias $b$ (these are a subset of the parameters $\theta$). With these in each layer we perform the function:

![[Pasted image 20221006112304.png]]

We can use many different **activation functions** but we need these as without them we can only create *linear functions*. The *ReLU* or Rectified Linear Unit can be written as $R(z)=\max(0,z)$ and looks like:

![[Pasted image 20221006112505.png]]

Although there are many alternatives.

### Training
There is a different between *inference* and *training*. Inference is performed when the network is already trained (whatever the task is). 

![[Pasted image 20221006112732.png]]

The *loss function* takes as an input the predicted output from the network and the true output $f^*$ and provides a **measure** of the difference between the two. We try to *minimize this measure*. By modifying the parameters $\theta$ this is called *optimization*. We want to make a loss function such that by reducing it the difference between the $f$ and $f^*$ values gets smaller. This optimization produces a change to $\theta$.

![[Pasted image 20221006112935.png]]

### Classification
Here we take some input $x$ and we want to map it to one of $K$ classes or categories. This can be image classification, semantic segmentation. Then **regression** is given an input $x$ we map it to a *real number*.  This can be *depth prediction* or bounding box estimation.

##### SoftMax Output Layers
When we have a loss function we need to work this into the output layer. The **SoftMax** is a output layer where we take a number of values as in a hidden unit layer and produce a *probability distribution* hence for however many input layers we have or $K$ classes. So we perform a linear transform producing a $K$-vector:

![[Pasted image 20221006113417.png]]

Then we pass this through the SoftMax function:

![[Pasted image 20221006113437.png]]

An example would be *cat classification* we will get as an output from the *linear transform* different real number values for each class. Then we apply SoftMax to get probabilities:

![[Pasted image 20221006113538.png]]

### Cross-Entropy Loss function
This is a commonly used Loss function. This treats its input as a probability distribution and we take:

![[Pasted image 20221006113643.png]]

Where $-z_i$ means that we maximize the class in the value we want (as it is -) and minimize in other classes as $-\times-=+$ hence we minimize loss so minimize this.

One problem with the *mean squared error* increases the randomness in the loss values as small differences after the linear transform get amplified by the *SoftMax*.

## Linear Output Layers
here we use *Mean Squared error* where our final layer is:

![[Pasted image 20221006114024.png]]

We then take the *mean squared error loss* as:

![[Pasted image 20221006114047.png]]

This indeed comes form assuming the error in the true values follows a *gaussian distribution* from out model. Then minimizing this gives the MSE loss.

### Training to Decrease Loss
We take a average of our losses and calculate the *gradients* we can then take of some fraction of this to get a better $\theta$

![[Pasted image 20221006114250.png]]

The *gradient* is a vector in the size of $\theta$. When we take some part off we reduce the loss by changing $\theta$. We take a step size $\epsilon$ who's size cannot be too large to ensure we don't miss the optimal values.  

![[Pasted image 20221006114443.png]]

##### Initialization and Stopping Conditions
![[Pasted image 20221006114723.png]]

## ConvNets
There are many neural networks but *ConvNets* are especially suited to "grid data" like images. But this can generalize to 1D time series data, 2D image and 3D videos. There are two major types of layers used *convolution layers* and *pooling layers*.

![[Pasted image 20221006114811.png]]

##### Dense vs Convolution layers
In a **dense layer** we allow every element to be affected by every other element:

![[Pasted image 20221006115023.png]]

But *convolution layers* are sparse and not every not affects every other for example:

![[Pasted image 20221006115057.png]]

We have less parameters and so we are less **flexible** however we are a lot more *efficient* in terms of memory. But this doesn't matter too much as image data is usually local and related more to closer pixels (which we focus on) instead of further away pixels.

### Operation
This way this works is we apply a *convolution* with a matrix just as in **edge detection**. We also have multiple layers and so we can apply different changes for different layers taking a *volume* and producing a *volume*.

![[Pasted image 20221006115346.png]]

We can use *zero-padding* to allow edge pixels to still be used. We can calculate the output size from the input size:

![[Pasted image 20221006115637.png]]

### Pooling : max pooling
The way this works is we split the network into different regions and then we take the max value for the outputs. Large values make more difference in these types of network hence ingnoring small values makes little difference. The *stride size* $S$ is the size of these regions:

![[Pasted image 20221006115741.png]]

We can calculate the output size as follows for some pool size $m\times m$ and stride $S$:

![[Pasted image 20221006115844.png]]

Max pooling is resistant to small shifts and so an be resistant to noise.
