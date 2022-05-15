What is a perceptron? #flashcard #MachineLeanringMIT #Basic
	A perceptron is the most basic part of a neural network. It takes in a number of values weights them, adds a bias then passes the result through a non-linear transformation $\hat y=g(w_0+\sum_{i=1}^mx_iw_i$

---
How can the result form a perceptron be represented using linear algebra? #flashcard #MachineLeanringMIT #Basic 
	Linear algebra helps simplify the calculate. We can make the weights into a weight vector and the input values into a weight vector. The result will then be the cross product between the two vectors and then we add a bias and pass through our non-linear function.

---
What is the non-linear function called for a perceptron and give some common forms? #flashcard #MachineLeanringMIT #Basic 
	This is called the activation function. Some common forms are the sigmoid which varies between 0 and 1. The hyperbolic tangent which varies between -1 and 1. Then the ReLU (Rectified Linear Unit) which is at 0 for negative values then 1 otherwise.

---
What to activation functions allow in terms of function approximation? #flashcard #MachineLeanringMIT #Basic 
	Without the matrices all we would really be able to do is rotate and transform in space. The non-linear functions allow for more complex functions to be approximated that are non-linear hence non-linear patterns can be modeled by the network.

---
What makes up a neural network? #flashcard #MachineLeanringMIT #Basic
	A neural network is made up of many layers of perceptron. We can feed the outputs from one layer into the next layer. The simples kind would be a single layered neural network.

---
What can the transition from one layer's values to the next be thought of in terms of linear algebra? #flashcard #MachineLeanringMIT #Basic 
	The outputs for one layer can be through of and an $n$ vector for $n$ vertices. Then from this layer to the next with $m$ perceptron/neurons. This can be a $m\times n$ matrix. This would then have each value in the resulting $m$ dimensional vector passed through its corresponding activation function.

---
What are the layers in a network called that aren't the first and last? #flashcard #MachineLeanringMIT #Basic 
	These are called the **hidden layers**.

---
What is the loss of a network a measure of? #flashcard #MachineLeanringMIT #Basic 
	This is a measure of how well the network performs a greater loss means a worse performance. This is used to allow training of the network. It is obtained by comparing $y^{(i)}$ (wanted) to $\hat y$ (actual). We sum over all our examples to get a total loss.

---
What is the aim of neural network training? #flashcard #MachineLeanringMIT #Basic 
	In neural network training we are attempting to minimize the loss of our network. The goal is to find the assignment of weights that minimizes the loss over the training data.

---
What is the main way of training a neural network? #flashcard #MachineLeanringMIT #Basic 
	The main way of training a neural network is gradient descent. The idea is that we treat our loss as a function on out weights then we get a gradient for all out weights for a given total weight assignment. We can then nudge all the values down their gradient to get a loss that will hopefully be smaller.

---
What is backpropagation and what does it solve? #flashcard #MachineLeanringMIT #Basic 
	Backpropagation is a techniques used to find all the gradients for the weights in a neural network given some function. This works by using the chain rule. The first layer of weights is simple we just take $\frac{\partial J(W)}{\partial w_i}$ which is expanded to $\frac{\partial J(W)}{\partial\hat y}\cdot\frac{\partial\hat y}{\partial w_1}$ with the chain rule. Now to find the gradients in the next layer we can use the gradients we have already calculated with the chain rule to find.

---
What is the learning rate in gradient decent?  #flashcard #MachineLeanringMIT #Basic 
	The learning rate describes what percentage of the gradient we take of out weights. With a higher learning rate our weights will change more but we may not be able to get any find detail needed to find good set of values. If this value is too small we can get stuck on local minima and fail to reach a good set of values.

---
How can batching be used to speed up neural network training? #flashcard #MachineLeanringMIT #Basic 
	It is intractable to calculate loss over many training samples this is due to each step in our gradient decent needing a average over all the gradients for all functions. Instead we can take a small step many times in mini batches where we only average over a a small number of examples. This can be done in parallel on a GPU to make the calculations much faster.

---
What is underfitting and overfitting? #flashcard #MachineLeanringMIT #Basic 
	If our weights aren't specified enough our network can miss curtail detain and patterns in our data. However when we learn our weights too much we can get overfitting where we pick up the random patters in the data and start to just memorize it. This will reduce performance in the true cases.

---
What are some ways to reduce overfitting? #flashcard #MachineLeanringMIT #Basic 
	**Dropout** will help reduce overfitting. This is where we randomly set the activation of some neurons to 0 each time. This ensures the network is resilient and there are many redundant paths for modeling. **Early Stopping** is another technique where we keep track of how well we are doing in the training and testing data once we start getting worse in the test set (which we haven't trained against) we stop.

---
