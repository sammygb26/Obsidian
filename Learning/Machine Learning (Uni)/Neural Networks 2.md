# Neural Networks 2
We will try to use optimization to find the parameters our network will use for inference. A simple neural network with a sigmoid function can be summed up as:

![[Pasted image 20221014152450.png]]

With a two class approximation the output of our node can be seen to have the same form as calculating posterior probabilities:

![[Pasted image 20221014152653.png]]

### Training Neural Networks
We need to define our *training set* and **error function**. For example we could use mean squared error function:

![[Pasted image 20221014152750.png]]

We want  to minimize this MSE that is we want to find $\underset{w}\min E_{MSE}(w)$. There is no analytical solution and so need to employ an iterative method. Like for example gradient descent (seen below in vector and scalar forms):

![[Pasted image 20221014152911.png]]

Usually **Online/stochastic gradient descent** is used where we sample the dataset to speed up training. So we update parameters with a subset to reduce the number of samples needed to perform a given update. Sometimes our algorithm can get stuck in a *local minimum*.

![[Pasted image 20221014153308.png]]

And we can try using different starting values to change this.

### Finding Gradient
We start with the basic MSE error:

![[Pasted image 20221014153415.png]]

Now we can apply the **chain rule** giving the gradient since $\hat y_n$ is a function on $a_n$ and $a_n$ is a function of $w_i$:

![[Pasted image 20221014153524.png]]

Overall this allows us to calculate how much our weight should change in a compact form:

![[Pasted image 20221014153711.png]]

### A problem
We find that we have to pass the activations through the derivative of our activation function:

![[Pasted image 20221014153810.png]]

The problem with this is for extreme values of $a$ the gradient will be very small. To remedy this we can use **cross-entropy loss** which cancels our $g'$ when $g$ is a sigmoid function.

![[Pasted image 20221014154045.png]]

### Other Activation functions
![[Pasted image 20221014154110.png]]

LReLU is normally used instead as its derivative cannot be 0 and so doesn't give the same problem where nodes will stop changing if their activation becomes negative $g'=0$.

### Multiple Output Nodes
With multiple output nodes we get a model as follows:

![[Pasted image 20221014154439.png]]

We apply a similar error function:

![[Pasted image 20221014154523.png]]

This can be **trained** in much the same way finding the gradient and applying gradient descent:

![[Pasted image 20221014154554.png]]

### Training Multiple Layers
We use a superscript $(i)$ to mean something in the $i$th layer. We can apply the same formulas as before but this only gives values for the last layer. The key idea is we can use the activations from the forward propagation as if they were the inputs to the last layers. This gives derivatives for the first layer. But the values from the first layer goes to many different nodes in the last layer. Hence a summation is needed:

![[Pasted image 20221014155445.png]]

#### Computation Graph
Vectors and Matrices are commonly used to allow computation to be more efficiently performed by GPUs. So we can write the calculation of our first layer calculations as:$$\textbf z=g(\textbf x)=\sigma(W_1\textbf x+w_{10})$$then the second layer is: $$\hat {\textbf y}=\text{softmax}(W_2\textbf z+w_{20})$$
and finally the loss is:

![[Pasted image 20221014155843.png]]

![[Pasted image 20221014155549.png]]

Basically we can think of applying many nested functions and therefore we can apply the chain rule to any depth we want to find derivatives for arbitrary weights.

