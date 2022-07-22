What does nx represent in machine learning mathematics? #flashcard #MachineLearning #BinaryClassification
	$n_x$ represents the size of the input feature vector. If there are 3 values we take into account in some problem we have $n_x=3$.

---
With m examples and nx feature vector size what is the size of the X examples matrix? #flashcard #MachineLearning #BinaryClassification 
	This will be of size $(n_x, m)$ having $n_x$ rows and $m$ columns.

---
How can binary regression be performed with logistic regression?  #flashcard #MachineLearning #BinaryClassification 
		In binary regression we are trying to predict if a feature vector belongs to a class or not. Instead of outputting one class or another the logistic regression approach is to output a probability that the example belongs to a class or not. This is done by weighting each feature then passing through a non-linearity logistic function.

---
What is the point of a loss function when it comes to logistic regression?  #flashcard #MachineLearning #BinaryClassification 
	We are trying to maximize how much our predicted probabilities match the true data. The loss function generally used is a cross entropy loss. The gradient from this ties in well to the non-linearity of the logistic function to make the landscape easy to optimize over.

---
What is the cross entropy loss function for a single output prediction?  #flashcard #MachineLearning #BinaryClassification 
	This works well for definite answers where the training example will either be a 0 or a 1. The function is $\mathcal L(y,\hat y)=-(y\hspace{8pt}log(\hat y)+(1-y)log(1-\hat y))$ this reduces to $-log (\hat y)$ when $y=1$ and $-log(1-\hat y)$ when $y=0$. Hence gives very large values when the predicted value is the opposite of the training and very low in reverse. We will attempt to minimize this loss so this gives the effect we want.

---
What is the loss called when calculated over all examples?  #flashcard #MachineLearning #BinaryClassification 
	This is called the cost function. It is an average of the loss over all examples.

---
How does gradient descent work to minimize out loss?  #flashcard #MachineLearning #BinaryClassification 
	The idea is if we take the gradient of the loss with respect to our parameters (weights and bias before logistic function). We can take away a small fraction of this gradient to slowly minimize the loss (cost).

---
How can a computation graph be used for find gradients for specific parameters?  #flashcard #MachineLearning #BinaryClassification 
	The computation graph gives a diagram exampling how value influence each other. **Bach propagation** take place within this graph where we start with the output value (loss/cost) and figure out how changes to every value affecting it come together. The computation graph gives an easy visual description of how to do this.

---
