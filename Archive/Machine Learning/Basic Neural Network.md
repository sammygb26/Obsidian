# Basic Neural Network
As seen in [[Machine Learning/Binary Classification and Logistic Regression]] machine learning can take place within a simple logistic regression domain. We take in *activations* of our feature vector multiple by weights and pass that through an activation.

![[Pasted image 20220709125511.png]]

A **neural network** works in this same way we can however stack more *layers*.

![[Pasted image 20220709125616.png]]

Each nodes takes in a z-like calculation and a a-like calculation. Each stack of nodes is called a *layer* and we say $W^{[1]}$ is the weights for the first layer then $W^{[2]}$ is the weights for the second layer and so on. In the same way $b^{[i]}$ is the *bias* for the $i$th layer.

![[Pasted image 20220709130003.png]]

The **input layer** is made out of the input features $x_1, x_2, x_3$ the **hidden layer** will be the second layer or any layer that isn't the first or last layer. The final layer is called the **output layer** and produces our output $\hat y$. The *hidden layer* is named such as these values are hidden in the training data. We say $a^{[0]}=x$ where $a$ is the activations so $a^{[0]}$ is the activations of the first layer. The hidden layer in this case will also generate *activations* $a^{[1]}$. The input layer isn't counted so this network is called a 2-layer neural network. 

### Computing Neural Network Output
This is similar to just [[Logistic Regression]] but repeated many times.

![[Pasted image 20220709131223.png]]

We compute $z$ and then use that to compute the activation $a$. Each node acts like this calculating $z$ and then $a$. So the top note we will calculate $z_1^{[1]}$ as $z^{[1]}_1=w_1^{[1]T}x+b_1^{[1]}$ where subscript $1$ just means first node. So $a^{[\mathcal l]}_i$ is the $\mathcal l$th layer and the $i$th node. This is the overall calculation for layer 1.

![[Pasted image 20220709131645.png]]

This can be **vectorized** ([[Vectorization]]) we stack the weights to get a $4\times3$ matric $W$ which is a stack of the transposes of the weight vectors. This way $W^{[1]}x=[w^{[1]T}x, w^{[2]T}x, w^{[3]T}x,w^{[4]T}x]$ we can then add on a similar vector for the biases. To get $Z^{[1]}=[w^{[1]T}x+b^{[1]}_1, w^{[2]T}x+b^{[1]}_2, w^{[3]T}x+b^{[1]}_3,w^{[4]T}x+b^{[1]}_4]$. This will be a *column vector*. We define an activation vector $a^{[1]}=[a^{[1]}_1,a^{[1]}_2,a^{[1]}_3,a^{[1]}_4]=\sigma(Z^{[1]})$. Then the $z$s and $a$s for the network can be worked out similarly.

![[Pasted image 20220709135131.png]]

### Vectorizing Across Multiple Examples
From the equations above we can calculate $\hat y$ for a single training example. We must repeat this for all training examples from $1\to m$. We are taking in $x^{(1)},x^{(2)}...x^{(m)}$ and to generate $a^{[2](1)},a^{[2](2)}...,a^{[2](m)}$ where here $a^{[2](i)}$ is the activation for the  $i$th training example. This could be done with the following for loop.

![[Pasted image 20220709135617.png]]

We can replace $x^{(i)}$ with the matrix $X$ and instead get $Z^{[1]}$, $A^{[1]}$, $Z^{[2]}$ and $A^{[2]}$ where each one has the different examples' vectors placed horizontally apart. As each input is a vector and to push a matric through a matrix multiplication you just repeat for each column giving a number of $m$ columns as an output replacing $x$ with $X$.

### Alternative Activations Functions
Previously we have used the sigmoid activation function but often other choices can work much better. A common one is tanh. This has the following graph going form -1 to 1 instead of 0 to 1 as in sigmoid.

![[Pasted image 20220709142350.png]]

This is actually a shifted version of $\sigma$ where $tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$. This creates an output form layers than is more centered as the mean of the possible activations is 0. *Sigmoid* is however useful for the output layer of our network say when outputting in *binary classification*. In general we say some $a=g(z)$ where g is out activation function and more generally for some layer $i$ we say $a^{[i]}=g^{[i]}(z^{[i]})$ where $g^{[i]}$ is the activation function for the $i$th layer. A problem with *sigmoid* and *tanh* is that for large values the gradients are very small which can cause gradient descent to take far longer than needed. The alternative is the *Rectified Linear Unit* or **ReLU** where $g(z)=max(0,x)$ hence has the graph:

![[Pasted image 20220709143536.png]]

This function isn't differentiable but we can just treat the output as if its 0 or 1. There is also the **LReLU** or leaky ReLU which has $g(z)=max(cz, z)$ hence the graph:

![[Pasted image 20220709144058.png]]

### Why do we need a non-linear activation function?
Phrased another way why don't we just have $a=z$? If we do this $\hat y$ is just a linear function of $a^{[0]}$/$x$. That is all becomes $w'x+b'$ where $w'$ and $b'$ are a simple matrix and real number. Then it will be no more expressive than a simple logistic regression with no hidden layers. This kind of activation is also called a **linear** activation. This can be useful if our output is a real number.

### Gradient Descent for Neural Networks
We can get the derivatives $g'$ for our $g$ activation function and then we can perform back propagation within the neural network. We want to *optimize* our **parameters** these will be $w^{[1]}$, $b^{[1]}$, $w^{[2]}$ and $b^{[2]}$. We also define a **cost function** as $$J(w^{[1]},b^{[1]},w^{[2]},b^{[2]})=\frac1m\sum_{i=1}^m\mathcal L(\hat y,y)$$
We want to initialize the parameter to random *non-zero* values. We then compute the prediction $\hat y$ for all examples. Then the all the derivatives for our parameter. We then update our parameters by their gradient times the learning rate. This will be one integration until we get convergence or a good enough cost.

### Random Initialization
When we have our model we need to initial state for the parameters we are optimizing. However they cannot be initialized all to 0. At least for the weights (not the biases). The problem is this will cause our nodes to be *symmetric*. This means the derivative for the weights will be the same so no matter how long you train the network the hidden units will train the same function and so this limits the expressivity of the network. The solution is to initialize the weights to be random variables to a range close to 0.

[[Basic Neural Network Questions]]