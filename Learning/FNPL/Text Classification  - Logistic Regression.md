The **naive bayes** assumption is a problem since words are not independent. We also want to add more feature to our model. But this can add unwanted affects and results in over confidence. Instead a **maximum entropy model** which doesn't make the conditional independence assumption.

## MaxEnt Classified
These are common used as **multinomial logistic regression**. This can also be called a log-linear model. Similar to Naive Bayes, MaxEnt assigns a document $x$ to class $\hat c$, where

![[Pasted image 20230207121559.png]]

But we do not apply bayes rules to  $P(c|x)$

##### Discriminative Model
**MaxEnt** is a estimative model. We can distinguish correct vs incorrect values of $c$ given input $x$ but that is all. This is unlike naive bayes which can also generate data from a class $c$ (hence is a **generative model**).


These are trained to **discriminate** correct vs incorrect. They don't need to be probabilistic. 

## Example
We will be given a web page document. This gives $\vec x$ : the words in the document Plus inform, about headers and links. We want to predict $c$ the class.

![[Pasted image 20230207121940.png]]

Like Naive Bayes, MaxEnt models use **features** we think will be useful for classification. These features are trained differently in each model.

![[Pasted image 20230207122052.png]]

### MaxEnt feature examples

![[Pasted image 20230207122116.png]]

## Classification with MaxEnt
We choose the class with the highest probability according to 

![[Pasted image 20230207122151.png]]

where the normalization constant $Z=\sum_{c'}\exp(\sum_i w_if_i(\vec x, c'))$. This defines a dot product of the $\vec w$ and $\vec f$ vectors. $P(c\mid \vec x)$ is a **monotonic function** of this dot product. So we will end up choosing the class for which $\vec w\cdot vec f$ is highest.

(difference form previous linear models is $c$ changes the feature given)

As an example:

![[Pasted image 20230207122403.png]]

Then to find our class we use

![[Pasted image 20230207122528.png]]

We can take the max of these to find **Sport** is our predicted class.

## Feature Templates
In practice, features are usually defined using **templates** which are easy to implement.

![[Pasted image 20230207122702.png]]

These can be instantiated with all possible words $w$ and classes $c$. NLP tasks often have a few templates but 1000s or 10000s of features.

## Training the Model
Given annotated data we want to choose weights that make the labels most probable under the model. In **naive bayes** we had a simple formula. We attempt to **maximize likelihood**. Hence we maximize

![[Pasted image 20230207122934.png]]

But this can be inverted (-) to get a loss. This is called **conditional maximum likelihood estimation** (CMLE). Like MLE, CMLE will overfit so we use tricks (**regularization**) to avoid this.

We use **gradient descent** to maximize the likelihood and find $\hat w$. $$\vec w\gets\text{Random()}$$$$\vec w\gets \vec w+\eta\nabla_w\sum_{j=1}^N\log P\left(c^{(j)}\mid x^{(j)}\right)$$We repeat this for a subset of our data called a **batch**. This makes this **stochastic gradient descent**.

#### Getting the Gradient
We have our *model* as:

![[Pasted image 20230207123415.png]]

We want to consider the gradient with respect to a single feature $f_l$. Which could represent any feature. We can expand our derivative as

![[Pasted image 20230207123534.png]]

The $\log$ and $\exp$ cancels out revealing

![[Pasted image 20230207123611.png]]

That is the change with respect to $w_l$ is $f_l$. This feature is only present when for $f_l$  when $c=k$. For some class $k$. So we define this as

![[Pasted image 20230207123758.png]]

Then we need to differentiate $Z$ as:

![[Pasted image 20230207124006.png]]

We can combine both derivatives as 

![[Pasted image 20230207124040.png]]

This comes as the differences between what the model label is and the probability our model gives. Hence the gradient stops when the prediction and true label is the same. If the model is wrong the model changes the weight to get a better estimate for the model.

### Relation to naive Bayes
**Naive Bayes** is also a linear classifier, and can be expressed in the same form. Hence why they are the same format. They are both linear models. The different assumptions give rise to different training and different results.

![[Pasted image 20230207124329.png]]

The features are all used with **naive bayes**. This improves model robustness as t must use all possible values. Instead **EntMax** model may exploit features and so the model may relay on few features.

## NB vs MaxEnt
In Theoretical results: generative classifiers converge faster with training set size to their optimal error. But the discriminative model will eventually get a better result.

![[Pasted image 20230207124633.png]]

### Downside to MaxEnt Models
Supervised MLE in generative models is easy: compute counts and normalized. But with MaxEnt models is harder. It requires multiple iterations over the data to gradually improve weights. Each iteration computes $P(c^{(j)}|x^{(j)})$ for all $j$ and each possible $c^{(j)}$. This can all be time consuming.

**Robustness** - If our training distribution is different from our real usage (deployment / test). Then we will be left 

[[Text Classification Logistic Regression Questions]]
