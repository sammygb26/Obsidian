# Classification
[[Machine Learning (Uni)/Linear Regression]] is about fitting a line to data. Instead we may want to classify different features into classes for example with the set bellow:

![[Pasted image 20220930195811.png]]

Set label one set $y=-1$ and one $y=+1$ then we draw a line to classify this. We can make a line as before $w^Tx+b=0$ where $x=[x_1\hspace{3pt}x_2]^T$. This lends itself to two areas where $w^Tx+b\ge0$ and 
$w^T+b\le0$

![[Pasted image 20220930200432.png]]

We can define $f(x)$ so that it returns a class based on these results.

![[Pasted image 20220930200601.png]]

Note this is only for *binary classification*. We need a **loss** to measure how well the classifier is doing. We will use a **Zero-one loss** defined as follows:

![[Pasted image 20220930200718.png]]

So we loose $1$ if we are wrong and $0$ if not. In the binary case we can also write $\textbf 1_{y\hat y<0}$ that is if they are the same we get a 0 as $y\hat y=1$ and if they are different we get $y\hat y=-1$ and so a $1$. We use the same classification as before where $S$ is a list of pairs of $x$ feature vectors to $y$ ground truths. Our function $f(x)$ is called a *linear predictor* or *linear separator*. Our task is to find $w$ and $b$ to minimize our *loss*. So we write the **loss** as:

![[Pasted image 20220930201225.png]]

This loss is *interesting* as changing $w$ and $b$ a little doesn't change the labels and so doesn't change the loss. This means that the $w$ doesn't have curvature and so the derivative will always be $0$. Hence for this loss finding $w$ and $b$ is NP-hard.

### A probabilistic approach
We can instead us a *probabilistic approach*. We define the probability of being $+1$ or being $-1$ and we pick a function to do this.

![[Pasted image 20220930201539.png]]

This function is called the *sigmoid* function:

![[Pasted image 20220930201604.png]]

As there is a limit to $-\infty$ as 0 and limit to $\infty$ as 1 we can use it to get probabilities. This means that if $w^T+b$ is very large $p(y=+1|x)$ tends to be close to $1$ and if it is very negative it is close to $0$. The two functions are compared below. The transition becomes smooth and so has *curvature*.

![[Pasted image 20220930201851.png]]

In the 2D case we get the following:

![[Pasted image 20220930202029.png]]

From the definition of $p(y=+1|x)$ we can get $p(y=-1|x)$ as follows:

![[Pasted image 20220930202216.png]]

This gives a very symmetrical interpolation and so we can encode the different in the $y$ value itself and so we get the following for both cases:

![[Pasted image 20220930202352.png]]

Now if we assume independence in our data points we know the probability of all of them as the product of their individual probabilities. Hence we can define the data given some $w$ as

![[Pasted image 20220930202600.png]]

Now this has curvature so we can take *derivatives* and solve. But there is no **closed form** solution so there is no exact value for $w$. **Note** when we write $-\log p(y|x)$ we don't mean that $y$ and $x$ are free. Instead $y=y^*$ given some pair $x$ and $y^*$.

### Features
We can also include features by replacing $x$ with $\phi(x)$ to add non linearity into the mix.

![[Pasted image 20221001132951.png]]

This would lead to out probability function changing.

![[Pasted image 20221001133036.png]]

##### Two circle example
We may want to separate two circles as bellow. But what function should we include in $\phi$ to have this property. We can include a distance function giving:

![[Pasted image 20221001133328.png]]

The radius is on one axis. Then we can just cut it with a simple plane. 

### Multiclass Classification
To begin to work with multiple classes we can break the single $w$ vector into two $w_{+1}$ and $w_{-1}$ with $w=w_{+1}-w_{-1}$. This gives:

![[Pasted image 20221001133846.png]]

Note we have placed only one $w$ on the top in this case $w_{+1}$ So we can have the top one being the $w_y$ vector as in this case $y=+1$. Hence for $y=-1$ we have:

![[Pasted image 20221001134055.png]]

Then this can be combined into the first equation and **generalizes** in the multiclass case to the second

![[Pasted image 20221001134157.png]]

We can try to find the class of $x$ with the function $f(x)$ that is we take $$\underset{y\in\mathcal Y}{\arg\max}\hspace{3pt}p(y|x)=\underset{y\in\mathcal Y}{\arg\max}\hspace{3pt}\frac{\exp(w_y^T\phi(x))}{\sum_{y'\in\mathcal Y}\exp\left(w_{y'}\phi(x)\right)}=\underset{y\in\mathcal Y}{\arg\max}\hspace{3pt}w_y^T\phi(x)$$The reason the second sum equals the third is as the bottom section is independent of out choice of $y$ and $\exp$ is monotonically increasing to removing it doesn't make a different to the argmax function. We can then follow the bellow case to see that this is consistent with the *binary case*:

![[Pasted image 20221001135008.png]]

The *multiclass* and *binary* cases can be summarized as follows:

![[Pasted image 20221001135305.png]]

##### Log Loss


### SoftMax
The *multiclass* case is related to **SoftMax** where we have  for all values in some column vector we apply the following function:

![[Pasted image 20221001135538.png]]

This leads to all the values being scaled such that all values are between 0 and 1 and all sum to 1 and the highest values belong relatively to the highest value before hand. This allow us to transform a $\textbf R$ distribution to a corresponding probability distribution. *SoftMax* has the property that the more extreme the number in are the more extreme the output probabilities are:

![[Pasted image 20221001135839.png]]

When the **dynamic range** is high the result is *sharp*.

[[Classification Questions]]