What is the difference between single and multiple models? #flashcard #MachineLearningUni #Boosting
	With single models we have a single model computing our output. In multiple models we take a collection of models that could work in their own right and combine them to get a hopefully better output.

---
What are the two ways to get a model linear average? #flashcard #MachineLearningUni #Boosting 
	If we have models $f_i(x)$ for $M$ different $i$ values we can either take an average $$y=F(x)=\frac1M\sum_{i=1}^Mf_i(x)$$ or a weighted average $$y=F(x)=\frac1M\sum_{i=1}^M\alpha_i f_i(x)$$ where $\alpha_i$ values have the properties of probabilities.

---
What are the two options for training a multiple model in ensemble learning? #flashcard #MachineLearningUni #Boosting 
	We can either train each model separately or all together as one large model.

---
What positive result can be found for a multiple model when we consider the expected error of the multiple model, and what do we have to assume for this? #flashcard #MachineLearningUni #Boosting 
	This will be $E_{comm}=\frac1ME_{avr}$ where $E_{avr}$ is the expected average error in the committee is inverse with the number of sub-networks and proportional to the average error in those networks. However this assumes the error is 

---
How can the number of "votes" be written for a binary classification task? #flashcard #MachineLearningUni #Boosting 
	We can say each $f_i$ has probability $p$ then a vote for one out of the two classes is given by $\mathbb 1(f_i(x)>0)=y_i$ hence $$S=\sum_{i=1}^My_i$$ is the number of votes by the network for $S$ being in the positive class.

---
How can the accuracy of network voting be codified into a formula? #flashcard #MachineLearningUni #Boosting 
	If we have $S$ as the number of votes for the right class then $p(S>M/2)$ is the probability we will choose the right class. If $p$ is the probability we are correct then $S$ is a binomial random variable with parameters $M$ and $p$. Hence we have $$p(S>M/2)=1-B(M/2,M,p)$$

---
What does the probability of success for a committee with individual uncorrelated accuracy p mean? #flashcard #MachineLearningUni #Boosting 
	This means for any probability $p>0.5$ we can make the network as accurate as we like but we will need exponentially more networks.

---
What is another name for the bagging method and why? #flashcard #MachineLearningUni #Boosting 
	This can also be called bootstrap aggregating. **Bootstrap** is the part where we divide the data into the models then **aggregating** 

---
What is the bagging committee method? #flashcard #MachineLearningUni #Boosting 
	Here for a dataset $D$ we train $i$ models. each has some $D_i$ dataset which is **randomly sampled with replacement** from $D$.  The idea here is to give us a distribution of answers about the mean.

---
What is boosting? #flashcard #MachineLearningUni #Boosting 
	This is a technique for a multiple model where weight many different models together each of which has different parameters $\theta_m$. Our model will be $$F(x;\theta)=\sum_{m=1}^Ma_mf_m(x;\theta_m)$$ Here each model predicts either $0$ or $1$.

---
What is the objecting/loss for a boosting model? #flashcard #MachineLearningUni #Boosting 
	This will be to minimize the loss with respect to the weights and the parameters: $$\min_{\theta,\alpha}\sum_{i=1}^nl(y_i,F(x_i,\theta)$$ where $$F(x;\theta)=\sum_{m=1}^Ma_mf_m(x;\theta_m)$$

---
What is the idea behind AdaBoost? #flashcard #MachineLearningUni #Boosting 
	The idea is that we keep track of weights for each datapoint. Then to construct our Boosted model by fitting in turn each sub model to the weighted data then increasing the weights to the remaining incorrect data.

---
What are the steps in AdaBoost? #flashcard #MachineLearningUni #Boosting 
	1. Initialize the weights $w=(w_1,...,w_n)$ so that $w_i=\frac1n$.
	2. For m=1 to ML
		1.Fit a classifier $f_m(x)$ to the weighted training data.
		2. Compute $\text{err}_m=\frac{\sum_{y_i\neq f_m(x_i)}w_i}{\sum_{i=1}^nw_i}$ as the sum of unexplained weight over the total weight.
		3. Compute $\alpha_m=\frac12\log\left(\frac{1-\text{err}_m}{\text{err}_m}\right)$ the inverse logit of the err percentage
		4. Update the weights $w_i\leftarrow w_ie^{\{\alpha_m\mathbb1(y\neq f_m(x_i))\}}$, that is they stay the same if correctly classified and are scaled up by $e^{\alpha_m}$ if not.
	3. Output the final model $F(x)=\text{sgn}\left(\sum_{m=1}^M\alpha_mf_m(x)\right)$ 

---
What loss function does AdaBoost employ? #flashcard #MachineLearningUni #Boosting 
	It uses an exponential loss function $$L_m=\sum_{i=1}^me^{-y_iF_m(x_i)}$$ where $F_m(x)=\alpha_1 f_1(x)+\dots+\alpha_mf_m(x)$

---
When we have some Ada function F_{m-1} and we want to make F_m what do we need to minimize with the new f_m? #flashcard #MachineLearningUni #Boosting 
	We need to minimize $$\min_{f_m}\sum_{y_i\neq f_m(x_i)}w_{m,i}$$ where $w_{m,i}=e^{-y_iF_{m-1}(x_i)}$ so we are trying to minimize the previous loss (weight) of all misclassification made with the new $f_m$.

---
How is the weight defined in AdaBoost and how is it updated? #flashcard #MachineLearningUni #Boosting 
	The weight in Adobos is defined as the loss of the network calculated with $F_{m-1}$ only previous $f_{u}$ ($0<u<m$) functions. Hence is $$w_{m,i}=\sum_{i=1}^ne^{-y_iF_{m-1}(x_i)}$$ Hence to calculate it we just add on $w_{m,i}=w_{m-1,i}e^{\alpha_{m-1}\mathbb 1(y_i\neq f_{m-1}(x_i))}$ 

---
What solution does minimizing L_m yield for the alpha values for the new function in AdaBoost? #flashcard #MachineLearningUni #Boosting 
	This yields $$\alpha_m=\frac12\log\left(\frac{1-\text{err}_m}{\text{err}_m}\right)$$

---
What are the affects of the exponential loss function  in AdaBoost? #flashcard #MachineLearningUni #Boosting 
	The exponential loss function is a **differentiable approximation** of the ideal error function. Sequentially minimizing it leads to Adaboost. It penalizes very negative values and so misclassifications.

---
What is Viola-Jones face detection? #flashcard #MachineLearningUni #Boosting 
	This is a face detection technique that uses a combination of weak classifiers and many different privative features.  We train this on a large number of positives and negatives then scan it over an image to detect where a face could be.

---
What are some methods of boosting other than AdaBoost? #flashcard #MachineLearningUni #Boosting 
	These could be **logit boost** using the loss function $$L_m=\sum_{i=1}^n\log\left(1+e^{-yiF_m(x_i)}\right)$$ **Gradient boosting** where we differentiate with respect to the functions and maximize that way. Then **extreme gradient boosting** which works for small tabular datasets.

---
