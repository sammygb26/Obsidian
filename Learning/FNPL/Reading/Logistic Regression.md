**Generative vs Discriminative Models** - Often you will hear the terms *discriminative* and *generative* for models. But what do these mean? It is an architectural difference in how the model attempts to understand the world. They can both perform discrimination but the **generative** models asks a question like given I'm generating a class how likely or how surprised am I for this given output. A **discriminative** model on the other hand directly ask which is more likely given the data. The two can be summarized formally as

**Discriminative** - We are directly estimating the probability $$\hat c=\underset{c\in\mathcal C}{\arg\max}P(c\mid d)$$for a document (set of features $d$) we are predicting a class $c$.

**Generative** - We are generating features for a class. So we estimate $P(d\mid c)$. This is called the *likelihood* and then we used the *prior* $P(c)$ in combination to perform discrimination so $$\hat c=\underset{c\in\mathcal C}{\arg\max}P(d\mid c)P(c)$$This model is more powerful than the *discriminative* one as it can also generate arbitrary examples.

## The Sigmoid Function
This is the function LR uses. The basic idea is we will generate some discriminative value that will be for example high when $P(y=1)$ is likely and low when $P(y=0)$ is likely. This value which we can call $z$ is calculated as the weighted sum of the **features** which we consider to capture the documents. So for $n$ features and so $n$ weights we get$$z=\left(\sum_{i=1}^nw_ix_i\right)+b$$where $b$ is the **bias** term. Generally all the $x_i$ values can be expressed as a feature vector $\mathbf x$ and the same for the weights -> weight vector $\mathbf w$. So the above equation simplifies to $$z=\mathbf w\cdot\mathbf x+b$$Now we want a probability so we want so squish this value to be between 0 and 1! We can use the **sigmoid** function for this.

![[Pasted image 20230420125958.png]]

It also has some nice properties and is differentiable which is useful. This has the formula $$\sigma(z)=\frac1{1+\exp(-z)}$$So we can write $$P(y=1)=\sigma(\mathbf x\cdot \mathbf w+b)=\frac1{1+\exp(-(\mathbf x\cdot \mathbf w+b))}$$Then we can find that since $P(y=0)=1-P(y=1)$ and $1-\sigma(z)=\sigma(-z)$ that $$P(y=0)=\frac1{1+\exp(\mathbf x\cdot\mathbf w+b)}$$

## Classification with Logistic Regression
We define a **regression boundary** when $P(y=1)$ becomes greater than $P(y=0)$ which will be $P(y=1)=0.5$ and so $$\text{desicion}(\mathbf x)=\begin{cases}1\space&\text{if }P(y=1\mid x)>0.5\\0&\text{otherwise}\end{cases}$$
For an example we could look at **sentiment classification**. We could have feature definition give our feature vector for the document as follows.

![[Pasted image 20230420131055.png]]

Now this feature vector can me evaluated with our weight vector. For example $[2.5,-5,-1.2,0.5,2.0,0.8]$ where negative values mean negative sentiment etc. 

![[Pasted image 20230420131206.png]]

Often features are deigned and found by hand but most recently feature extraction has been used to find features in a semi supervised way.

**Feature templates** can also be used and these will be populated during training. These allow features to be automatically detected.

**Scaling Input Features** - Generally input features are scaled so their value are similar. For example they can be **standardized**

![[Pasted image 20230420131631.png]]

Or **normalized**

![[Pasted image 20230420131645.png]]

##### Processing Many Example At Once
It is often faster to process in parallel rather than series. For example we could process multiple examples as 

![[Pasted image 20230420131747.png]]

in **series** but instead we can combine the features into a **matrix** and do things in parallel for example

![[Pasted image 20230420131815.png]]

For our features then our equation would be $$\mathbf y=\mathbf{Xw}+\mathbf b$$For a output vector $\mathbf y$, feature matrix $X$, weight vector $\mathbf w$ and bias vector $\mathbf b$.

##### Comparison to Naive Bayes
One advantage over naive bayes is LR isn't fooled by correlated variables as easily. *Naive Bayes* on the other hand will almost give double weight if to features are correlated together. LR spreads the weight between the two features. NB can also be less efficient to run on binary decisions as it has to manage each feature individually for each class. But general NB is a good baseline and is computationally less expensive when it comes to training.

## Multinomial Logistic Regression
The basic idea here is we can split out weights matrix into many values one for each class.  We also split up our output into a vector of probabilities (again one for each class).

#### SoftMax
This is the function we use to make all the dot product sums of our features probabilities who all sum to 1. We apply $$\text{softmax}(\mathbf z_i)=\frac{\exp(\mathbf z_i)}{\sum_{j=1}^K\exp(\mathbf z_j)}\hspace{32pt}1\le i\le K$$So we are normalizing an exponentiated value between all classes. So for a class $k$ with a weight matrix $\mathbf w_k$ we can write $$P(y_k=1\mid\mathbf x)=\frac{\exp(\mathbf w_k\cdot \mathbf x+b_k)}{\sum_{j=1}^K\exp(\mathbf w_j\cdot\mathbf x+b_j)}$$This can be combined into $\hat{\mathbf y}=[y_1\dots y_K]$ which is the estimated probability vector. Then we compare this to $\mathbf y$ which is the true vector. This will be a one-hot encoding of the true class and is provided by supervision. 

## Learning in Logistic Regression
Now we have $\hat{\mathbf y}$ we want to change the weights so that $\hat{\mathbf y}$ s closest to $\mathbf y$.  The way this is done is with a **loss function** and an **optimization algorithm**. 

**Cost function** - In general the cost function is defined as the distance between the desired vector and true vector. We optimize our algorithm to minimize this on the training data.

**Optimization algorithm** - This allows us to choose how to change our weights when we compare against the ideal vector.

## The Cross-entropy loss function
We want to find a measure of our estimation's distance form the true value. We train to make the correct class labeles more likely. This is called **conditional maximum likelihood estimation**. To derive this one way is to look at the probability our estimation will be correct. That is $p(y\mid x)$ given $\hat y$ the true probability. Since this is a binary decision and so we have a **Bernoulli distribution** this will be $$P(y\mid x)={\hat y}^y(1-\hat{y})^{1-y}$$We want to maximize this. To make it simpler we can take the log of it and so maximize the log likelihood. This will be $$\log P(y\mid x)=y\log\hat y+(1-y)\log(1-\hat y)$$Now our loss will be minimized so we can just make this negative to give our loss. That is $$\mathcal L=-[y\log \hat y+(1-y)\log(1-\hat y)]$$

## Gradient Descent
We will call the model parameters $\theta$ and we want to find the minimum $\theta$ for our loss function $L_{CE}$ given some dataset. That is

![[Pasted image 20230420153208.png]]

One way to minimize is through **gradient descent** where we use the gradient which points in the direction of creates growth (in parameter space of our loss function). So we will use

![[Pasted image 20230420153330.png]]

Where the gradient is a multidimensional array of the gradient for each parameter. So it would be

![[Pasted image 20230420153403.png]]

Each of these can be worked out analytically unlike the true minimum. For example the loss with respect to a particular $j$th weight will be

![[Pasted image 20230420153505.png]]

#### Stochastic Gradient Descent
Here we take one step at a time (controlled by $\eta$) for a random sample from all our training examples.

![[Pasted image 20230420153615.png]]

#### Mini-batch training
The above option can be computationally tractable but the gradient changes a lot as the examples can be very different. One option is to take a slice of our data and get the gradient for the loss of the whole dataset. Infact since the likelihood of the whole dataset given our parameters is just the product of the individual likelihoods. Hence the log likelihood is the sum! This allows us to average the gradients from each batch (as derivatives distribute over sums!). 

![[Pasted image 20230420153947.png]]

And so the cost can be rewritten as

![[Pasted image 20230420154011.png]]

Which changes our final gradients giving us

![[Pasted image 20230420154028.png]]

Similarly to **multinomial GD** we can use matrices to parallelize and speed up computation.

![[Pasted image 20230420154115.png]]

Finally we could do this over the entire dataset and this would give us **batch gradient descent**.

## Regularization
When we optimize our model will use any features that is correlated with the output. If we suppose there is some noise then our model can fit this rather than the features this is **overfitting** and we will not **generalize** to data not in the training dataset. One option to help avoid this is **regularization** in which a term $R(\theta)$ i added to the objective function which limits the models flexibility and so ability to fit the noise in the dataset. We hope the weights needed to fit the true distribution are simpler that these ones. Our loss becomes

![[Pasted image 20230420155026.png]]

There are two common kinds of regularization **L2** and **L1**. L2 uses Euclidian distance of the weights from 0 squared. That is 

![[Pasted image 20230420155420.png]]

While l1 is the Manhattan distance from the origin

![[Pasted image 20230420155454.png]]

L1 is also called **lasso regression** and L2 **ridge regression**. L2 is easier to optimize while L1 leads to  a sparser distribution for weights. Both can be seen as assuming a distribution over the input weights and attempting to minimize that L1 assumes a laplace while L2 assumes a gaussian. That is

![[Pasted image 20230420155800.png]]

Our likelihood likewise becomes

![[Pasted image 20230420155827.png]]

which assuming $\mu=0$ and $\sigma^2=1$ corresponds to