# Introduction
We think about *Artificial Intelligence* as the ability of a compute to mimic intelligent behavior. Then *Machine Learning* is a machine's ability to do this without being completely programmed. Finally *Deep Learning* is where we can extract patterns that aren't programmed from data using **neural networks**

The difference between just feature detection and deep learning is the composition of features over multiple levels to allow for deeper in the network concepts to be represented rather than just fixed patterns. This is the difference between original neural networks as now we can do this with new computer hardware that is more powerful.

## Perceptron
This is the basic building block of neural networks. It is called a *perceptron* and is a simplified representation based on a neuron in the brain. Information propagates through a *perceptron*. We take a weighted sum of all the values that can change going into a neuron as well a a fixed bias term. The resulting values is then passed through a non-linear activation function to give our output.

![[Pasted image 20220302221113.png]]

The *bias* allows you to shift the level at which the activation function will have certain values. We can also represent the $x_i$s and $w_i$s. This way we can take the dot product of two vectors $W$ and $X$ this will give us $\hat y=g(w_0+X^TW)$ where $w_0$ is the bias.

We use a nonlinear function but we can choose whatever we like. Some common ones are given bellow along with how to use them in **TensorFlow** which is a library to use neural networks.

![[Pasted image 20220302221431.png]]

The **sigmoid function** is very useful as it always gives an output between 0 and 1, so it suits probability quite well. **ReLU** is also quite popular due to its simplicity.

## Why Activation Functions?
We may ask why we need activation functions. We do this to add non-linearity to our neural function on the data otherwise we couldn't split the data in a non-linear way. The layers aren't different without an activation function for example we could just compose all the matrices that can represent going from one layer to another and so we have accomplished no more than just one layer.

![[Pasted image 20220302222035.png]]

This way we can *approximate* arbitrarily complex functions. Any weighted combination of values will create a field in the dimension of the input vector. We can think of boundary in this as some critical value for our activation function. It will always be a hyper plane. The ideas is when we apply similar distortions again and again in deep neural networks that we get meaningful patterns.

## Neural Networks
If we take a single *perceptron* or *neuron* we can look at it in a more simplified way where every line going in has a weight $w_i$ applies to a value $x_i$ its value $z$ is the weighted sum with the bias. Then $g$ is applied going forward.

![[Pasted image 20220302223243.png]]$$
z=w_o+\sum_{j=1}^mx_jw_j
$$
We can add more output by just adding more *neurons*. This gives us the following.

![[Pasted image 20220302223407.png]]$$
z_i=w_{0,i}+\sum_{j=1}^mx_jw_{j,i}
$$ We add $i$ to indicate which $z$ we are referring to. We still take the dot product of the input values and weights for each $z$ plus a bias. When we have every input connected to every perceptron we call this a *dense layer* or *fully connected layers*.

#### Single Layer Neural Network
Here we add another layer after the first to be out final output layer. We now have two layers of weights.

![[Pasted image 20220302223955.png]]$$
z_i=w_{0,i}^{(1)}\sum_{j=1}^mx_jw_{i,j}^{(1)}\hspace{16pt}\hat y_i=w_{0,i}^{(2)}\sum_{j=1}^mx_jw_{i,j}^{(2)}
$$
The middle layer is called a *hidden layer*.  We has a superscript to the weights $W^{(1)}$ and $W^{(2)}$ to specify which matrix we take the values from. If we just look at one neuron in the hidden layer like $z_2$ it is the same perceptron as before. If we want the $z$ values for the whole row we take a matrix multiplication of the input values to get the output vector. So we get $$Z=W^{1}\bar x+\bar w_0$$We can look at a single neuron and see it is the same as before.

![[Pasted image 20220302224632.png]]

To create a deep neural network we just keep stacking layers like this.

## Applying Neural Networks
We have a feature space which is the dimension of the size of the input vector into the network. This can be populated with collected data. We want to build neural networks that are capable to taking this input vector to our output that is useful in some way. But if we just give our network some value it just gives some random answer. This is since out network hasn't *learned* anything it is the equivalent of a baby. We need some way of telling it when it is wrong or right. We say *loss* of a network measures the cost incurred from incorrect predictions.
$$
\mathcal{L}(f(x^{(i)};\textbf{W},y^{(i)})
$$
Loss is $\mathcal{L}$ where $f$ is the function our network is applying we predict $\hat y$ which is the result form $f$ and we compare this to $y^{(1)}$ which is our final result. So we compare the predicted output and the ground truth output. We want to minimize the *loss*. If we have lots of data we can compute an **empirical loss**. We want to make a network the minimizes the empirical loss of a network. It is defined as $$J(\textbf W)=\frac{1}{n}\sum_{i=1}^n\mathcal L\left(f(x^{(i)};\textbf W), y^{(i)}\right)$$If we are predicting probabilities we can use *cross entropy loss*. This measures how far apart two distributions are that is success vs failure. It is given as $$J(\textbf W)=-\frac{1}{n}\sum_{i=1}^ny^{(i)}log\left(f(x^{(i)};\textbf W)\right)+(1-y^{(i)})log\left(1-f(x^{(i)};\textbf W)\right)$$Another error loss we can use when we are outputting a value rather than a probability is *mean squared loss*. This is a sum of the differences of the values from the actual results. We would the use $$J(\textbf W)=\frac{1}{n}\sum_{i=1}^n\left(y^{(i)}-f(x^{(i)};\textbf W)\right)^2$$
## Training Neural Networks
We have our *loss function* now we need to optimize it. We want the lowest loss for given values of $\textbf W$ we are optimizing $\textbf W$ to minimize our loss which is defined by the dataset.$$
W^*=\mathop{argmin}_{\textbf W}\frac{1}{n}\sum_{i=1}^n\mathcal L\left(f(x^{(i)};\textbf W), y^{(i)}\right)$$$$
W^*=\mathop{argmin}_{\textbf W}J(\textbf W)$$We can think of $\textbf W$ as a high dimensional array of values that describe some point in this high dimensional space. We can then plot our loss in this space. It will give a landscape in a space one dimension higher. With two weights this can fit into 3D.

![[Pasted image 20220302234509.png]]

We pick some point then we compute the gradient at some point that is $\frac{\partial J(W)}{\partial W}$. This tells us which direction would move us up so instead we turn the other way and reduce the values by this amount. We do this over and over again to get towards the lowest point. We will converge to a local minimum (though perhaps not a global minimum).

![[Pasted image 20220302234552.png]]

This algorithm is called *gradient descent* and can be summarized in the following algorithm.

![[Pasted image 20220302234647.png]]

We take a small step in the direction we want this is done by multiplying by the factor $\eta$. This is called the *learning rate*. The gradients themselves $\frac{\partial J(W)}{\partial W}$ need to be calculated and this is done through *backpropagation*.

#### Backpropogation
This can be seen clearly with a very simple neural network. We want to compute the gradient for $w_1$ and $w_2$ in order to find the loss for the weights as a whole.

![[Pasted image 20220302235538.png]]

We can have a derivative for how much a change in $\hat y$ changes $J(W)$. But if we want to calculate the change in $J(W)$ with respect to $w_2$ we can use that chain rule so that we find how much a change in $\hat y$ is affected by a change in $w_2$ then this can be combined with how much we know some small change will change $J(W)$ this will give us
$$\frac{\partial J(W)}{\partial w_2}=\frac{\partial J(W)}{\partial\hat y}\cdot\frac{\partial\hat y}{\partial w_2}
$$ But now that we have the derivative given by a small change in $w_2$ we can use this to calculate for $w_1$! This will give us
$$\frac{\partial J(W)}{\partial w_1}=\frac{\partial J(W)}{\partial\hat y}\cdot\frac{\partial\hat y}{\partial w_1}
$$Which is reclusively expanded to the following as we don't know how much $\partial\hat y$ will be change by $\partial w_1$.  Where the function $z_1$ contains within it the value of $w_2$
$$\frac{\partial J(W)}{\partial w_1}=\frac{\partial J(W)}{\partial\hat y}\cdot\frac{\partial\hat y}{\partial z_1}\cdot\frac{\partial z_1}{\partial w_1}
$$
The recursion coming from the layer of differentiable functions is what leads to the name *backpropagation*. This gets harder to calculate for more and more weights in a network like for example thousands or millions.

## In Practice
It is much harder than the simple description above. In reality is is extremely hard to train network. For example the loss function when plotted for a real network will have a very non-convex (lots of local minimum). Hence our final state will depend greatly on out starting condition. Hence it depends a lot on our initial conditions (*hyperparameters*). We can node the step function from before.
$$
W\leftarrow W-\eta\frac{\partial J(W)}{\partial W}
$$
We can change the $\eta$ value to jump out of local minima or skip over them. But choosing this value is hard as small values will converge to the slightest local minima while too large a value will diverge. We can build an *adaptive* learning rate that changes with how large the gradient is or many other options like weight sizes, time from start how quickly learning is improving.

## Batching
The gradient can be very hard to compute especially if it is over the whole data set. Instead of calculating over the whole dataset we just calculate for a single data point this is called *stochastic gradient decent*. The better option is instead of using this single gradient we estimate it better using a *batch*. Then we estimate the gradient as an average over a batch of size $B$. This is more *accurate* that *SGD* and is far cheaper than full *GD*. This is called *minibatching*. This also allows us to parallelize to different CPUs or  GPUs hence we can train on large systems much faster.

## Overfitting
The problem comes from our network training too much to the point where we predict the training data well at the cost of generalization. We don't care about the training data we care about the test or real data. If we don't have enough capacity we are *underfitting* and when we have too much we are *overfitting*.

![[Pasted image 20220303003437.png]]

We have to fit out model to the data getting an *idea fit*. But neural networks have so many parameter how can they not overfit? For this we need *regularization*. This is a system we can use to improve generalization and there are many different way of implementing it.

**Dropout** -> Here we randomly set some activations to 0. This means some of our *neurons* are simply deactivated. This reduced the capacity in our network hence our network has to learn to be resilient to loss in functionality. Hence it reduces the capacity to memorize reliably. It also speeds up training as with a dropout probability of 0.5 for example we only have to train half the network at a time.  We drop different neurons each time so a network has to make sure to not overfit to one path and rely on the whole network.

**Early Stopping** -> Here we keep some test data at the side we can then compare how the network does on both sets. In the beginning both lines decrease. But eventually the *testing* loss will increase even though *training* must decrease due to gradient descent if our network still has capacity to memorize the training data. Hence we can stop at the minimum of how well our test set does.

![[Pasted image 20220303004600.png]]
