# Neural Networks 1
The neural network's parts are the *perceptrons*.  Their basic design is based around how *neurons* work.

![[Pasted image 20221010151507.png]]

The perceptron takes in some vector $x$ and uses a weight vector $w$ and weight $b$ give an output value. If perceptron output is positive  we say its active and 0 if not. This all came from **Frank Rosenblatt's** perceptron. Which was designed to classify letters.

![[Pasted image 20221010151812.png]]

### Decision Boundary of Linear Discriminant
We can think about this network as fitting a hyperplane where $w$ is the normal.

![[Pasted image 20221010152005.png]]

The *decision boundary* is defined where $\textbf w^T\textbf x + \textbf w_0=0$. In 3D we have a plane decision boundary. With higher dimensions we have a **hyperplane** with $y(x)=\sum_{i=0}^Dw_ix_i$

![[Pasted image 20221010152210.png]]

### Training of Perceptron
We want to reduce the decision boundary such that there is less misclassification. We need a perceptron correction algorithm for this.

![[Pasted image 20221010152348.png]]

For simplicity we define $\dot x=[1, x^T]^T$. Then we define $g$ to be the step function or *activation function* (also transfer function $g(a)=H(a)$). We also want a set of paired values for our training set:

![[Pasted image 20221010152618.png]]

We then initialize $w$ and if we run some $x_i$ and it is misclassified. We set $w^{\text{(new)}}=w+\eta(y_i-y(x_i))x_i$.

If $y_i$ and $y(x_i)$ are the same we get

![[Pasted image 20221010152928.png]]

If they are different we add a small error to move $w$ towards a value that will further minimize the error.

![[Pasted image 20221010153157.png]]

There are two versions of this algorithm *Incremental (online)* where we update for each sample seen. Then there is *Batch* where we go over the whole dataset and take the average of the change. But this takes a long time as we have to go over the whole dataset for each update.

This algorithm converges when the training samples are *linearly separable*.

![[Pasted image 20221010153605.png]]

### Structures and Decision Boundaries
As we change $w$ we change the slope of our decision boundary. Given the decision boundary we can calculate our weight vector. With the example below of $x_2>x_1-1$ we get $a(x)=1-x_1+x_2=w_0+w_1x_1+w_2x_2$. Hence we have found $w_0$, $w_1$ and $w_2=1$. We have found a solution. But the relative size is what matters we could scale any of these values and get the same decision boundary.

Since we are dealing with a binary output 0,1 we can create logical functions with these perceptrons. The $x_1$ is in the $x$ axis and the $x_2$ is in the $y$ axis.

![[Pasted image 20221010154147.png]]

Note: XOR has two decision boundaries so cannot be defined by our *perceptron*. We need two nodes to create two boundaries then a third to combine them.

![[Pasted image 20221010154444.png]]

We can draw two different perceptron combinations as follow:

![[Pasted image 20221010154811.png]]

The intermediate layers nodes (not output or input) are called **hidden nodes**.

![[Pasted image 20221010154900.png]]

When the numbers of hidden layers is increased we can get more complex output shapes:

![[Pasted image 20221010155026.png]]

We can **generalize** the perceptron to have multiple outputs. We instead have a matrix $\textbf W$ Hence we have $\hat y=g(\textbf W\dot{\textbf x})$.

![[Pasted image 20221010155235.png]]

![[Pasted image 20221010155246.png]]

### Limitations of Perceptron
The *training* algorithm used only works when we have a linearly separable dataset. It was proven in 1969 that it was only a linear classifier. Another problem with the *training* is that no training happens when the network is correct. We could try to resolve this by using MSE but then how can we update $w$. We cannot find derivatives as $g$ (as a step function) isn't differentiable.

If we replace $g$ with linear which would be differentiable we would really only have a single layer network as it all collapses.

We instead replace $g$ with a different function for example a *sigmoid* function. Which is differentiable

![[Pasted image 20221010155845.png]]

![[Pasted image 20221010155955.png]]

### Universal Approximation Theorem
This says that with one hidden layer we can approximate and continuous function of $n$ real variables. This doesn't say how to train or how many nodes we need.

[[Neural Networks 1 Questions]]