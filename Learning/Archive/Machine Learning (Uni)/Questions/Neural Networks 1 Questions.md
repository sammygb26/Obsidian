What is a perceptron? #flashcard #MachineLearningUni #NeuralNetworks 
	A perceptron is a simple model designed around neurons. The simplest perceptron takes in some number of inputs performs a weighted sum, adds a bias and then predicts a 0 or 1 (if it is active or not based on this).

---
What is the mathematical model of a simple perceptron?  #flashcard #MachineLearningUni #NeuralNetworks 
	A perceptron can be through of as having an input vector $\textbf x$, some weights $\textbf w$ and a bias $w_0$. The internal state of the perceptron is then $\textbf w^T\textbf x+b$ and the output is then set to 0 or one. We would write $y(\textbf x)=H(\textbf w^T\textbf x+w_0)$. Where $H(a)=\mathbb 1(a>0)$.

---
What is the decision boundary of a perceptron?   #flashcard #MachineLearningUni #NeuralNetworks 
	A perceptron takes in a weight vector $\textbf w$ that is uses to find it activation. This defines a hyperplane in the dimension of that vector for which values of $\textbf w^T\textbf x+w_0=0$. Where on one side we have activation and on the other side deactivation.

---
How did the training of the first perceptron work?  #flashcard #MachineLearningUni #NeuralNetworks 
	The first system was trained via a simple update method. We compare the binary output $y(x_i)$ to the ground truth $y_i$. This comparison tell us whether we should not move the decision boundary. Or move its normal towards or away form some point. This combines such that if a + point is on the - side we move the normal (pointing in the positive direction) towards that point and the revere in the -/+ case.

---
What are the two options for using the basic perceptron training algorithm? #flashcard #MachineLearningUni #NeuralNetworks 
	We can either use *Batch* mode or *Incremental mode*.

---
What is the difference between batch and incremental mode when it comes to the basic perceptron training algorithm? #flashcard #MachineLearningUni #NeuralNetworks 
	When we run in batch we take the changes to $w$ over the whole data set and average them, while in incremental mode we take a data point at a time and modify $w$ a small amount to better fit this.

---
Why can AND and OR be created with a perceptron decision boundary by not XOR? #flashcard #MachineLearningUni #NeuralNetworks 
	We can lay the two inputs to these logical operators in a 2D plane. We find that AND and OR only need a single decision boundary so one perceptron can perform this task however XOR require two and so 2 perceptron to create the boundaries and 1 to combine (3 total).

---
What are hidden nodes in a multilayer perceptron system? #flashcard #MachineLearningUni #NeuralNetworks 
	These are nodes (perceptrons) that aren't in the first (input) or last (output) layers.

---
How can we generalize perceptron to have multiple inputs and outputs? #flashcard #MachineLearningUni #NeuralNetworks 
	We can use a matrix instead of a vector. For example we use a $n\times m$ matrix to go from $m$ to $n$. We can then add a bias vector and apply a activation function over the whole vector.

---
What is a limitation with using a simple perceptron based model? #flashcard #MachineLearningUni #NeuralNetworks 
	This can only produce a linear classifier and so many types of inference cannot be done with this model. We also cannot differentiate past the binary output and therefore this type of model is hard to train. 

---
What extensions can be made to simple perceptrons to solve their shortcomings? #flashcard #MachineLearningUni #NeuralNetworks 
	 We can use a different activation function for example sigmoid. This also allows differentiation and so easier optimization/training.

---
What is the universal approximation theorem? #flashcard #MachineLearningUni #NeuralNetworks 
	This states that any function of $n$ real variables can be approximated by some network with just one hidden layer. However it doesn't say how many nodes to use or how to train this.

---
