This is part of **ensemble** learning (committee method). We have looked a many models in this course. This would be called **single models**. We also looked at **Mixture models** (like GMMs) which work to approximate more complex solutions. With **multiple models** we take a weighted average over the outputs from the networks.

![[Pasted image 20221111151516.png]]

This is the **committee method**. There are two options for training these committee models. We can train separately and we can also train sequentially where each model reduces the errors of the previous.

We belive taking many optinions increases the chance of getting a correct answer, but is this true? We can model our ensamble function ans $F(x)$. Where each $f_i(x)$ model make some small error as compared to the true functionn.

![[Pasted image 20221111151829.png]]

Then et can get the error average as follows

![[Pasted image 20221111151920.png]]

Hence the average error is just the average in the models. Hence w reduce the errors by a factor of $M$. This is assuming the errors have zero mean and are uncorrelated.

![[Pasted image 20221111152041.png]]

But this doesn't happen in reality and error will compound and lead to a lack of improvement.

**Another view** - we can take a collection of binary classifiers $\{f_i(x)\}$ where

![[Pasted image 20221111152235.png]]

We let $S$ denote the number of votes for class 1

![[Pasted image 20221111152257.png]]

The accuracy of the method will be modeled binomially as

![[Pasted image 20221111152345.png]]

Where $B(k,n,p)$ is the cdf of the binomial distribution of $k$ with parameters $n$ and $p$.

![[Pasted image 20221111152453.png]]

This will be modeled as above. This shows we can improve accuracy as much as we want as long as $p>0.5$ (assuming errors are uncorrelated).

### Bagging
This is a application of **bootstrap aggregating**. The idea is we train each $f_i(x)$ on a training dataset $D_i$ of size $n$ - sampled from the original data set $D$ uniformly and with replacement. Employ the same training algorithm of all $\{f_i(x)\}$.

![[Pasted image 20221111152854.png]]

Whether this works a lot depends on the task and the dataset used.

### Boosting
Boosting considers a weighted sum of all functions

![[Pasted image 20221111153034.png]]
($\theta_i$ should be replace with $\theta_m$)
Fine tuned to find $\alpha$?

Here all the $f_m$ functions have output +1 or -1. There is usually no closed form solution. We fit additive models sequentially fitting the data better and better.

![[Pasted image 20221111153308.png]]

### AdaBoost
Also known as adaptive boosting. We have training data set $\{(x_1,y_y),\dots,(x_n,y_n)\}$ and we have $M$ classifiers $f_m(x;\theta_m)$. We initialize the wieghts $w=(w_1,\dots,w_n)$ where $w_i=\frac1n$ For each $m$ we

1. Fir a classifiers $f_m(x)$ to the training data using $w$
2. Compute  ![[Pasted image 20221111154013.png]]
3. Compute ![[Pasted image 20221111154052.png]]
4. Update the weights ![[Pasted image 20221111154105.png]]

Then we output the final model 

![[Pasted image 20221111154127.png]]

##### Optimization problem in AdaBoost
Assuming we have trained all $f_1\dots f_{m-1}$ and obtained $\alpha_1\dots\alpha_{m-1}$

![[Pasted image 20221111154311.png]]

We now want tot train $f_m(x)$ and estimate $\alpha_m$ with the exponential loss function $L_m$ defined bellow

![[Pasted image 20221111154350.png]]

Since we already pretrained all the $m$s up to $m-1$. Confusion!!!

We now would like to minimize $L_m$ with respect to $\alpha_m$

![[Pasted image 20221111154827.png]]

taking logarithms yields

![[Pasted image 20221111154846.png]]

Hence

![[Pasted image 20221111154856.png]]

### Exponential loss in AdaBoost
We have $l(y,F(x))=e^{-yF(x)}$. This is differentiable and an approximation of the ideal misclassification error function (0,1 loss). Tis sequential minimization leads to the simple AdaBoost algorithm. It penalizes large negative values of $yF(x)$ (as it is exponential in these), hence it puts a lot of weight on misclassified samples (outliers made by people) $\to$ it is very sensitive to outliers (mislabeled examples).

![[Pasted image 20221111155118.png]]

### Applications of boosting - face detection
This used to be what AdaBoost was used for. This is very hard for computers hence a simpler technique is sued (Viola Jones Face Detection).

![[Pasted image 20221111155426.png]]

This takes the difference between the white and black areas. It is a week classifier that utilizes five types of privative features. The detector is trained on training data set of a large number of positive and negative samples. So it scans the input image with a sub mask.

### Other Methods of Software Tools for Boosting
Some other methods were tried after AdaBoost. For example Logit Boost

![[Pasted image 20221111155653.png]]

We can use gradient boosting where we differentiate with respect to the functions in order to find boosting values. Then extreme gradient boosting which works best for small tabular data sets.

[[Boosting Questions]]