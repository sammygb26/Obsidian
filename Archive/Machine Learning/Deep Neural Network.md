# Deep Neural Network
What makes a neural network **deep**? It is simply the number of layers. The shallowest might have 1 or so layers. Where as a proper deep neural network will have many more. The number of hidden layers allows the NN to model more complex functions.

### Notation
![[Pasted image 20220711154101.png]]

This is a 4 layers NN. The *notation* used we would say $L=4$ to denote the number of layers. We then have $n^{[l]}$ as the number of units in layer $l$. The closest layer to the input is the first layer. Hence $n^{[1]}=5$, $n^{[2]}=5$, $n^{[3]}=3$, $n^{[4]}=n^{[L]}=1$ then we can also say $n^{[0]}=n_x=3$. For each layer $l$ we also say $a^{[l]}$ as the activations of layer $l$. Then $a^{[l]}=g^{[l]}(z^{[l]})$ then we have the weights of layer $l$ as $w^{[l]}$. We would also say $a^{[0]}=x$ and $a^{[L]}=\hat y$.

### Forward Propagation in a Deep NN
This is when we want to get the output value for a given input into the network. Given the activations for some layer $l$ we would calculate the activations for that layer as $$z^{[l]}=W^{[l]}a^{[l-1]}+b^{[l]}$$and $$a^{[l]}=g^{[l]}(z^{[l]})$$Then this very simply will allow values to propagate through our training examples. These equations will work similarly for horizontally stacked output vectors.

### Getting Matrix Dimensions Right
This can help debugging implementations of a NN. It can help to look at the vectors going in and out of a layer. If a layer takes in $n^{[l-1]}$ inputs and has $n^{[l]}$ outputs. We know that $z^{[l]}$ will have the same dimension as the output. Hence the matrix $W^{[l]}$ will must have such a shape as to make this happen. The number of rows of a matrix is the number of rows of its output in vector form. Hence $W^{[l]}$ is $n^{[l]}$ rows high. It must have the number of columns as the rows of the matrix it is multiplied into. This will be the number of rows of the input vector hence $n^{[l-1]}$. Hence $W^{[l]}$ must be a $n^{[l]}\times n^{[l-1]}$ matrix. So the size can be through of as $($next$,$first$)$. The *dimension* of be will be the same as the output for the same layer. Hence $b$ in layer $l$ is size $(n^{[l]}\times1)$. The only difference when taking multiple examples is for some layer $l$ we will have $z^{[l]}$ being $(n^{[l]},m)$ matrix then $a^{[l]}$ will also be the same size. $b^{[l]}$ is still $(n^{[l]},1)$ but will be *broadcast* to become $(n^{[l]},m)$.

### Why Deep Networks Work Well
It has been observed that not just number of nodes and parameters matters. How deep the network is also plays a key role in its power. The idea is that the fist layers make up simpler layers then deeper in the network composes the functions together to pick out more complicated patterns. The network must be *deep* to allow this sort of composition. Another example is from *circuit* theory. Basically the idea is that small deep layered function can compute more complicated function that exponentially larger shallow networks.

### Building Blocks of Deep Neural Networks
When performing *forward propagation* we will compute the simple steps as above. We also cache $z^{[l]}$ allowing us solve back propagation later. When performing *back propagation* on a neural network we need to for each layer take as an input $da^{[l]}$ and output $da^{[l=1]}$. We cached $z^{[l]}$ to help compute this and we also compute $dw^{[l]}$ and $db^{[l]}$.

### Implementing Forward and Backward Propagation
In order to implement *forward* and *backward* propagation we will have two functional steps for each layer. The **forward step** taking in the activations for the last layer $a^{[l-1]}$ then computing the following using $W^{[l]}$ and $b^{[l]}$:

$$z^{[l]}=W^{[l]}a^{[l-1]}+b^{[l]}\hspace{64pt}a^{[l]}=g^{[l]}(z^{[l]})$$

We will also *cache* $z^{[l]}$ as we will need it later for backward propagation (optional can cache $W$ and $b$ depending on implementation).

In the **backward step** we take in $da^{[l]}$ and we output $da^{[l-1]}$ aswell as $dW^{[l]}$ and $db^{[l]}$. We make use of the cached $z^{[l]}$ value to do this. These steps are done with the following equations.

$$dz^{[l]}=da^{[l]}*g^{[l]}{'}(z^{[l]})\hspace{64pt}dW^{[l]}=dz^{[l]}a^{[l-1]T}$$
$$db^{[l]}=dz^{[l]}\hspace{64pt}da^{[l-1]}=W^{[l]T}dz^{[l]}$$

The same can be *vectorized* to deal with examples simply as in many cases above.

### Parameters and Hyperparameters
The *parameters* are $W$ and $b$ but there are also other things we need to store. These are called **hyperparameters** such as the learning rate $\alpha$ the number of iterations. The number of hidden layers $L$, the activation functions choices and the number of nodes in the hidden layers. These are parameters that control the parameters hence the name.

### Setting Up Machine Learning Applications
Applying ML is a highly iterative process where there are many hyperparameters that need to be explored. You will start with an idea, code it up then experiment to see how it works. This may then inform further ideas and experimentation until you're happy with the network. There are many areas ML has had success in but intuitions from one area may not move on to other areas. Not only this but also the hardware you're running on. This makes it hard to guess hyperparameters hence the testing and *iteration*. Going around the development cycle fast is therefore important for finding a good solution. To do this well **Train/Dev/test sets** must be set up well.

Data is usually split into a *training set* which is used to train the model on. Then the *holdout/cross validation/dev* set is used to test this against to find good **hyperparameters** finally a test set is used to evaluate overall performance. For this different splits are used. Such as *70/30* train test, or *60/20/20* train/dev/test. But with *big data* less percentage is needed for dev and test to get significant results. Hence these fractions have gotten skewed further towards larger training sets. So with 1,000,000 examples we may only need 10,000 for train and test. we may then have a *98/1/1* split. You can also have mismatched train/test sets where your training data can come form one source and test from another. In this case it may be ok as you can Taylor your training by having dev in the same as test.  Not having a test set may be ok if you don't need an unbiased measure of how well you're doing.

### Bias and Variance
We can define **bias** in terms of underfitting and overfitting. We can see this simply with two dimensions but require metrics for higher dimensions.

![[Pasted image 20220712222344.png]]

The key variables to look at are **train set error** and **dev set error**. An example would be a training set error of 1% and a dev set error of 11%. Here we would say we are overfitting and so we are not *generalizing* well. Here we would say we have **high variance**. Another example could be training set error of 15% and dev set error of 16% here (with humans doing far better) we can see the algorithm isn't even fitting the training set. So we say it is **biased**. If both train and dev are high say 15% train error and 30% dev error we might say **high bias and variance**. If we have very low in both cases 0.5% train error and 1% test error we may say **low bias and variance**. We predicate this on the assumption that human performance is 0%. But with an optimal error some of the other error may be considered differently. Another term for this ideal error is the *Bayes Error*.

### Basic Recipe for Machine Learning
When training you're network the first think to look at is does it have **high bias**. Then we can try by getting a *bigger network*, *train longer* or use *another architecture*. If we can fit within the *bayes error*. We can then look to see if there is **high variance**, can we generalize? If we cannot we can use *more data*, *use [[Machine Learning/MIT/Regularization]]* another *architecture* can also help with this. With love *bias* and *variance* we are done.

Originally in *machine learning* there was a lot of talk of "bias variance tradeoff" as many things that could be done would increase bias and reduce variance. But today along as we can train a bigger network with more data we can reduce bias from a bigger network and more data will reduce variance.

# Setting Up Optimization Problem

### Normalizing Inputs
One way of improving training is by **normalizing** out inputs. As an example we have some training set of feature of the form $x=[x_1,x_2]$. We can first reduce the mean of each input to 0. Where $\mu=\frac1m\sum_{i=1}^mx^{(i)}$ we set $x:=x-\mu$. Then we normalize variance where $\sigma^2=\frac1m\sum_{i=1}^m\left(x^{(i)}\right)^2$ we set $x:=x/\sigma$. 

![[Pasted image 20220713111507.png]]

Hence we reduce $x$ to have mean $(0,0)$ and variance $(1,1)$ as it is a vector. We we use some $\mu$ and $\sigma$ in training we must use the same in testing otherwise we could skew out test data in a strange way.

##### Why Normalize
This can help with the landscape we are optimizing over. With *unnormalized inputs* the different feature can take very different values with oblong contours. With normalization we get a more symmetric function and hence it is easier to optimize over.

![[Pasted image 20220713111935.png]]

The more distorted shape will require a lower learning rate to stabilize where as the other can learn quicker and so get a better result faster. In practice $w$ is a high dimensional vector hence this intuition doesn't quite make sense.

### Vanishing/exploding gradients
One of the problems with very deep neural networks is vanishing and exploding gradients. Here gradients can get very large or very small. We will have *weights* $w^{[1]},...w^{[L]}$. We can also say we are using for simplicity a linear activation function $z=g(z)$. Hence out activations will be $\hat y=w^{[1]}*...*w^{[L]}$. In an example $w^{[l]}=[1.5\hspace{3pt}0, 0\hspace{3pt}1.5]$ then $\hat y$ will grow at $1.5^L$. Conversely with $w^{[l]}=[0.5\hspace{3pt}0, 0\hspace{3pt}0.5]$ $\hat y=0.5^L$ and we get a very small value.

![[Pasted image 20220713112439.png]]

Similarly the gradients may be exponential small or large. This makes training difficult as small gradients means very small changes to weights and large gradients may cause our algorithm to be unable to converge. This can be solved partially with **smart weight initialization**.

### Weight Initialization for Deep Networks
We can look at a simple example with one neuron. Here we have $z=w_1x_1+w_2x_2+...+w_nx_n$ (ignoring $b$ for now). To ensure $z$ doesn't blow up or become small if we have a large $n$ we want smaller $w_i$. So we can set the variance of $w_i$ to be $\frac1n$. So we can say $$W^{[l]}=\text{np.random.randn($shape$)}*\text{np.sqrt$\left(\frac1{n^{[l-1]}}\right)$}$$(note with ReLU $\frac2n$ works a bit better). With $tanh$ we can use $\sqrt{\frac1{n^{[l-1]}}}$ this is called a *Xavier Initialization* another variant is $\sqrt{\frac2{n^{[l-1]}*n^{[l]}}}$. But the most common is the ReLU version. But this can also be tuned with **hyper parameters**.

### Numerical Approximation of Gradients
This is a numerical approximation than can help ensure any implementation of back prop works well. We can approximate gradients by adding a small number onto our value and off. We take two points for some $\theta$, $f(\theta-\epsilon)$ and $f(\theta+\epsilon)$. We then compute the gradient from the first value to the second. The heights will be $f(\theta+\epsilon)-f(\theta-\epsilon)$ then the width will be $2\epsilon$. Hence the gradients approximation is $$\frac{f(\theta+\epsilon)-f(\theta-\epsilon)}{2\epsilon}\approx g'(\theta)$$
### Gradient Checking
The way this works is we take all out weights and biases and concatenate them into a giant vector $\theta$. Hence we have $$\mathcal J(W^{[1]},b^{[1]}+...+W^{[L]},b^{[L]})=\mathcal J(\theta)$$
We also reshape $dW^{[1]},db^{[1]},...,dW^{[L]},db^{[L]}$ into a giant vector $d\theta$ of the same dimension as $\theta$. To implement grad check for each dimension of $\theta$. We nudge $\theta_i$ up by $\epsilon$ and down by the same amount. To get an approximation of $d\theta_i$ we use the final $J$ values from this with the above formula. We can check the approximation and a value form gradient descent one. After we go through all dimensions we can get a full $d\theta_{approx}$ and compare it to $d\theta$ to see if they're approximately equal. To do this we can compute the Euclidean distance that is $||d\theta_{\approx}-d\theta||_2$ we then and normalize by the length of the two vectors $||d\theta_{\approx}||_2+||d\theta||_2$. With epsilon of $10^{-7}$ we can check if our ratio is roughly equal. With larger values we may want to check our implementation.

### Implementing Gradient Checking
The first thing to note is grad check should only be run debugging and not while training. This is as the approximation calculations take a long time. You can also look specifically at which values are far of. For example the biases might be off but the weights might be fine hence the bias terms may be where the bug is. We also need to remember regularization may change the loss value and hence we should be careful this isn't what's causing differences in gradients. *Gradient checking* also doesn't work with *dropout*.

### Hyperparameter Tuning
When we train neural nets we need to set many **hyperparameters**. Perhaps the most important is the learning rate $\alpha$ but after that the momentum term $\beta$ aswell as the number of hidden units in each layer and the mini-batch size are important. After this the number of layers and learning rate decay may be helpful to tune. We must also *find the values* that work possibly sampling in a grid. This works well for few hyperparameters. But in deep learning it is common to sample randomly instead.

![[Pasted image 20220722183302.png]]

Its hard to know which are the most important  But with random samples instead of only testing out a limited number of a given variables say if another hardly has an effect you will instead try as many as you have samples. You can also sample randomly in a higher dimensional space and so sample it more richly.

We can also use a **coarse to fine** sampling scheme. Yo may sample a region of a given size and find a cluster of well performing sample. At this point we can take the region around this and sample it with the same number of points getting a more densely sampled area. 

![[Pasted image 20220722183818.png]]

Using appropriate scale to pick **hyperparameters**. We shouldn't pick uniformly over possible values but instead over reasonable values. If we want to pick the number of layers say between 50 and 100. We may pick uniformly randomly within the range. Or within a small number of values say 2-4. This works well for these kinds of *hyperparameters*. We may also pick $\alpha$ from say 0.0001 to 1. If we sample uniformly we will sample using 90% of our search space from 0.1-1 and only 10% from 0.0001-0.1. But the relative difference for the greater values may be unimportant. Hence instead we can sample on a uniform log scale. Giving more samples to the smaller values. Say 20% from 0.0001 to 0.001 20% from 0.001-0.01 and so on. We do this from sampling form $10^a$ to $10^b$ we sample $r\in[a,b]$ then take $10^{r}$.

Another case is picking $\beta$ from 0.9 to 0.999. In this case the first is an average for 10 values and the second is for 1000 days. It doesn't make sense to sample on the linear scale. We can instead sample $1-\beta$ in a log scale as before we can sample from 0.1 to 0.001 hence we sample $r\in[0.1,0.001]$ and take $\beta=1-10^r$.

The idea behind all of these is the sensitivity is relative to the change of the values 0.9-0.9005 is a lesser change than 0.0001 to 0.0005.

### SoftMax Regression
This is a generalization of [[Binary Classification and Logistic Regression]] where by we classify an example into one of a range of classes instead of just one. For examples $4$ classes form class $0$ to class $3$. We use $C$ to be the number of classes. So $C=4$ for above. We build an output layer where we have $C$ units so $n^{[L]}=C$. We want the output to be the probability of all the other classes. So $a^{[L]}_0=P(class=0|x)$.  These activations in $a^{[L]}$ must sum to one and a **SoftMax** function is used to perform this. We calculate $z$ as usual as $$z^{[L]}=W^{[L]}a^{[L-1]}+b^{[L]}$$We apply the *SoftMax* activation function. We calculate a column vector $t$ of the sam dimension as $z$ to be.$$t=e^{z^{[L]}}$$Then we calculate our final activation to be the normalized version of $t$ such that all values sum to 1.$$a^{[L]}=\frac{e^{z^{[L]}}}{\sum_{j=1}^{n^{[L]}}t_{j}}=\frac{t}{\sum t}$$The unusual part of the SoftMax is the normalization over the whole output vector. The kinds of dissections this performs follows.

![[Pasted image 20220723173157.png]]

The name *SoftMax* comes in contrast to **HardMax** where we would set the max value to 1 and everything else to 0. With $C=2$ *SoftMax* becomes the same as logistic regression as we would only need to compute 1 number.

Our labels will be of the form $y=[0, 1, 0, 0]$ for example. Say our prediction is $\hat y=[0.3, 0.2, 0.1, 0.4]$. Our loss becomes $$\mathcal L(\hat y, y)=-\sum_{j=1}^Cy_jlog(\hat y_j)$$This reduces to just be the negative log of the probability of the class we wanted. Hence higher when its close to 0 and low when its close to 1. The cost will be defined as simple the sum of the losses over the training examples. When applying gradient descent $dz^{[L]}$ becomes $\hat y-y$ when we are using a *SoftMax*. Then we just use this derivative to find $da^{[L-1]}$ hence stating of the backprop chain.

[[Deep Neural Network Questions]]

