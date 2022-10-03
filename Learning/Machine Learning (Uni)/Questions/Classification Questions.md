What is the classification problem? #flashcard #MachineLearningUni #Classification
	In the classification problem we are trying to instead of predicting a value from some feature vector as in regression we are predicting the class of a feature form instead.

---
How can we define a binary classification model simply? #flashcard #MachineLearningUni #Classification 
	We can take a linear model as in regression then pass it through a $f(x)=\text{sgn}(w^Tx+b)$.

---
What is a zero-one loss? #flashcard #MachineLearningUni #Classification 
	We define a zero one loss as $1$ if the ground truth value doesn't equal our assigned class and $0$ if it does.

---
What are the different ways of writing a zero-one loss? #flashcard #MachineLearningUni #Classification 
	We can write $\mathcal l_{01}(\hat y,y)=\{1 if \hat y\neq y, 0 \text{ otherwise}=\textbf{1}_{\hat y\neq y}=\textbf{1}_{\hat yy<0}$

---
How can the zero-one loss be summed up over an entire dataset? #flashcard #MachineLearningUni #Classification 
	We can just average all the zero-one losses for all the data points that is we take. $$L=\frac1N\sum_{i=1}^N\mathcal l_{01}(w^Tx+b,y)=\frac1N\sum_{i=1}^N\textbf{1}_{y(w^Tx+b)<0}$$

---
What is the problem with using a zero one loss when it comes to estimating the correct values for $w$ and $b$? #flashcard #MachineLearningUni #Classification 
	The problem is that small changes to $w$ and $b$ don't change $L$ hence we cannot use **differentiation** to solve for $w$ or $b$.

---
Why might it be good to take a probabilistic approach to classification? #flashcard #MachineLearningUni #Classification 
	Using a probabilistic approach allows for a smooth rather than disjoint change form one class to another. This allows calculus to be used for optimization.

---
How can we make a function to give the probability of being in one of two classes? #flashcard #MachineLearningUni #Classification 
	We want to define $p(y=+1|x)$ and $p(y=-1|x)=1-p(y=+1|x)$ one way to define this is with the **sigmoid function**. This way we get $$p(y=+1|x)=\frac1{1+\exp(-(w^Tx+b))}$$

---
What makes the sigmoid suited as a function giving probabilities? #flashcard #MachineLearningUni #Classification 
	Before we were taking the *sign* of $w^Tx+b$ to give the class so we want to the probability to be high when this value is very positive and very low when its verry negative. Furthermore we want the function to give values between 0 and 1. All these properties are exhibited by $\sigma$ $$\lim_{x\to\infty}\sigma(x)=1\hspace{16pt}\lim_{x\to-\infty}\sigma(x)=0\hspace{16pt}\forall x\in\textbf R. 0<\sigma(x)<1$$

---
What is the definition of the sigmoid function? #flashcard #MachineLearningUni #Classification 
	$$\sigma(x)=\frac1{1+\exp(-x)}=\frac1{1+e^{-x}}$$

---
Given that $p(y=+1|x)=\sigma(x)$ what is $p(y=-1|x)$? #flashcard #MachineLearningUni #Classification 
	This would be $$1-p(y=+1|x)=1-\frac1{1+\exp\left(-(w^Tx+b)\right)}=\frac{\exp(-(w^Tx+b))}{1+\exp(-(w^tx+b))}$$$$=\frac1{\exp(w^Tx+b)+1}=\frac1{1+e^{
	w^Tx+b}}$$

---
How can we combine $p(y=+1|x)$ and $p(y=-1|x)$ into one equation defining $p(y|x)$? #flashcard #MachineLearningUni #Classification 
	Since the only difference in $p(y=+1|x)$ and $p(y=-1|x)$ is the sign of the exponent and since this is encoded in $y$ we can write $$p(x|y)=\frac1{1+\exp(-y(w^Tx+b))}$$

---
How can we use the likelihood of our dataset given our model values $w$ and $b$ to get a loss? #flashcard #MachineLearningUni #Classification 
	The likelihood of our dataset given $w$ and $b$ will be (if we assume independence) $$\prod_{i=1}^Np(y_i|x_i)=\prod_{i=1}^N\frac1{1+\exp(-y(w^Tx+b))}$$So we can write a loss by taking the log of this:$$L=\log\prod_{i=1}^Np(y_i|x_i)=\sum_{i=1}^N\log\frac1{1+\exp(-y(w^Tx+b))}=\sum_{i=1}^N-\log\left(1+\exp((-y(w^Tx+b))\right)$$

---
How can categorize non-linear shapes in a similar way to capturing non-linearity in linear regression? #flashcard #MachineLearningUni #Classification 
	We can include a function $\phi(x)$ that projects $x$ into some higher dimensional space where one what we want to capture can be expressed as a linear combination of the dimensions. Then we can just perform linear classification and fund $w$ that works best.

---
How can we generalize binary classification to multiclass classification? #flashcard #MachineLearningUni #Classification 
	We can split the weight matrix $w$ into two for each case $w_{+1}$ and $w_{-1}$. This then allows us to write $w=(w_{+1}-w_{-1})$ this combined with our definition for $p(y|x)$ gives us $$p(y|x)=\frac{\exp(w_y^T\phi(x))}{\sum_{y'\in\{0,1\}\}}\exp(w_{y'}^T\phi(x))}$$Which is equivalent to $$p(y|x)=\frac{\exp(w_y^T\phi(x))}{\sum_{y\in\mathcal Y}\exp(w_{y'}^T\phi(x))}$$In the multiclass case.

---
How sum up the operation of probability estimation on multiple classes? #flashcard #MachineLearningUni #Classification 
	For each class $y$ we have a vector of weights $w_y$ this can be through of as giving a score for that class. For each class the probability is the the $\exp$ of this weights vector times the $\phi(x)$ features of $x$ divided by the sum of this exponent over all classes.

---
Why is argmax over $p(y|x)$ the same as argmax over $w^T\phi(x)$? #flashcard #MachineLearningUni #Classification 
	We have $\underset{y\in\mathcal Y}{\arg\max}\hspace{3pt}p(y|x)=\underset{y\in\mathcal Y}{\arg\max}\hspace{3pt}\frac{\exp(w_y^T\phi(x))}{\sum_{y'\in\mathcal Y}\exp\left(w_{y'}\phi(x)\right)}=\underset{y\in\mathcal Y}{\arg\max}\hspace{3pt}w_y^T\phi(x)$ which is true the bottom of the fraction in equation 2 is a constant so doesn't affect the values of argmax. Then as $e$ is monotonically increasing we can remove it as maxing over it will be the same as maxing its exponent.

---
What is the $f(x)$ function for selecting a class in multiclass classification? #flashcard #MachineLearningUni #Classification 
	This will be $f(x)=\underset{y\in\mathcal Y}{\text{argmax}}w_y^T\phi(x)$.

---
What is $p(y|x)$ (probability of $y$ given $x$) in multiclass linear classification? #flashcard #MachineLearningUni #Classification 
	This will be $p(y|x)=\frac{\exp(w_y^T\phi(x))}{\sum_{y\in\mathcal Y}\exp(w_{y'}^T\phi(x))}$

---
What does the SoftMax function do? #flashcard #MachineLearningUni #Classification 
	The SoftMax function takes a range of values say a vector $\textbf a$ and creates a equally sized vector of corresponding probabilities.

---
What is the SoftMax function? #flashcard #MachineLearningUni #Classification 
	This will be for some $N$-vector $\textbf a$ we have a new $N$-vector $\textbf p$ where each element $p_i$ we have $p_i=\frac{\exp(a_i)}{\sum_{i=1}^N\exp(a_i)}$. That is we raise $e$ to ever value and then normalize such that the values sum to 1.

---
How does SoftMax act differently when the values are small say $[1,2,3]$ vs large say $[100,200,300]$? #flashcard #MachineLearningUni #Classification 
	This has the effect of making the result more sharp we will get much more extreme values. In the second case the first two are almost exactly 0 and the final one is very close to 1. While in the first case the values are much more event 0.09, 0.24 and 0.67.

---
