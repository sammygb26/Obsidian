# Regularization
We can look at regularization from a logistic regression point of view. In  logistic regression we are trying to predict $y$ from some $x$ vector. We have *weights* $w\in \textbf R^{n_x}$ and $b\in \textbf R$. We have our loss function to fit this as:

$$
\mathcal J(w,b)=\frac1m\sum_{i=1}^m\mathcal L(\hat y^{(i)},y^{(i)})
$$

This can be made into a form with *regularization* as follows

$$
\mathcal J(w,b)=\frac1m\sum_{i=1}^m\mathcal L(\hat y^{(i)},y^{(i)}) + \frac\lambda{2m}||w||_2^2
$$

Here $||w||_2^2$ is the *Euclidian norm* or *l2 norm* of $w$ which is equal to $\sum_{j=1}^{n_x}w_{j}^2=w^Tw$. $\lambda$ is the regularization term used to control regularization. We call this *l2 regularization*. We can also add a regularization term for $b$ however this usually doesn't make much difference. There can also be *l1 regularization* where the term used is $\frac\lambda{2m}\sum_{i=1}^{n_x}|w|=\frac\lambda{2m}||w||_1$ this will make $w$ *sparse* meaning it has a lot of 0s (an explanation of this is given in [[Regularization]]). This may help compressing the model as some parameters can then be removed. $\lambda$ is picked using the dev set (hold our cross validation). 

This is slightly different in a NN. There we have a cost function as follows:

$$\mathcal J(w^{[1]},b^{[1]},...,w^{[l]},b^{[l]})=\frac1m\sum_{i=1}^m\mathcal L(\hat y^{(i)},y^{(i)})$$ 
To add *l2 regularization* this becomes

$$\mathcal J(w^{[1]},b^{[1]},...,w^{[l]},b^{[l]})=\frac1m\sum_{i=1}^m\mathcal L(\hat y^{(i)},y^{(i)})+\frac\lambda{2m}\sum_{l=1}^L||w^{[l]}||_F^2$$

This time the *squared norm of a matrix* is defined as $||w^{[l]}||^2=\sum_{i=1}^{n^{l}}\sum_{j=1}^{[n^{[l]}]}(w^{[l]}_{ij})^2$ as $w^{[l]}$ is an $n^{[l-1]}\times n^{[l-1]}$ matrix. This is also called the *Frobenius Norm*. So this isn't technically the *l2 norm* for LA reasons. This ties into **back propagation** by changing the $dw$ gradient in the weights. We can simply add to $dw$ the term $\frac\lambda m W^{[l]}$. This just comes from the calculus if you work it out. For this reason it is also called **weight decay**. Hence little extra computation is needed to implement this into back propagation.

### Why Regularization Reduces Overfitting
When we have a network with high variance. We would add in a *regularization* term that punishes the weights from being too large. With weights close to 0 in $w$ the idea is that with much smaller  hence the network wont be able to fit data and will be reduced in capability. This could cause **high bias** however. The network is less capable then it will be less able to overfit.

![[Pasted image 20220713101457.png]]

Another example comes rom the *tanh* function. Without large weights our values will be close to 0 hence $g(z)$ will be roughly linear.  If this is true the whole network becomes roughly linear hence cannot fit more complicated boundaries and so overfit. Another problem with *regularization* can be it is hard to debug and can cause the original cost to not decrease *monotonically*.

### Dropout Regularization
In dropout we have for each layer a probability a node will be **dropped out**. This could be say 0.5 for each node. We remove all these nodes and all the links going in and out.

![[Pasted image 20220713102437.png]]

For each example we can *drop out* a different set of nodes. The most common way to implement dropout is "Inverted dropout". We will do this with layer $l=3$. We set a drop out vector for layer 3. $d3=\text{np.random.rand(a3.shape[0],a3.shape[1])}<\text{keep-prob}$. Where $\text{keep-prob}$ is the probability a nodes will be kept. Then $d3$ will be a vector with a random chance (based on the keep probability) each entry is 1 or 0. Then when we have $a3$ we set it equal to $a3*d3$ hence zeroing the element corresponding to 0. Then we **scale up** $a3$ by $\text{keep-prob}$. $a3/=\text{keep-prob}$. The idea is that for elements in the next row the $z$ value will be equal to a weighted some of the $w$ values. But if they are all zeroed out this will reduce the value on average by a factor of $1-\text{keep-prob}$. Hence we scale it up to overcome this. This *scale up* step is what makes this **inverted dropout** and this ensures the expected value of $z$ remains the same. Different units are removed for each iteration and so the same examples will run through different drop out versions of the network in training.

At test time no drop out is used and no scaling is used. Hence we run the network at *full capacity*. Without the scaling step $z$ would be at a different expected value at hence why we perform the scaling.

### Understanding Dropout
One reason it *drop out works* is we cannot rely on any one feature as features may be lost at any iteration. Because of this the weights will be more spread out and hence shrank to give the same value. It may also cause the models understanding to be more robust and it relies of a variety of features instead of only a few. It has been shown that *l2 is similar* in effect to *l2 regularization*. We have to choose the keep-prop for different layers. For example with larger weight matrices we may have a lower keep-prob hence we focus on reducing overfitting on certain layers. You can even apply dropout to the input layer.

Dropout also came about from computer vision where the inputs are very large. Hence it allows dropout on the data. This combined with there usually not being enough data allows *drop-out* to be highly effective in this field. 

A problem with **drop-out** is that the cost function is not well defined as the value will change for different dropouts. One way to get around this is to only plot the network without dropout on.

### Other Regularization Methods
There are a few more regularization techniques to reduce overfitting. One is **data-augmentation** for example we can *flip* and image in out examples. There is some redundancy in the data so this isn't as good a?

[[Regularization Questions]]