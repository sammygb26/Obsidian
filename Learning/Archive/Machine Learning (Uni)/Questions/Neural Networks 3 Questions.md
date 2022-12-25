After the breakthrough of back propagation and non-linear activation functions what lead to the slowing of NN research? #flashcard #MachineLearningUni #NeuralNetworks
	Problems were found: 1) It was **computationally very expensive** and networks could take weeks to train 2) Networks had **slow convergence** caused by vanishing gradients hence layers didn't improve after a given point 3) It was **Difficult to find optimal network topology** 4) There was poor **generalization** from the training data to test data.

---
What does it mean for a network model to overfit? #flashcard #MachineLearningUni #NeuralNetworks 
	A network **overfits** when it has too much flexibility leading to it memorizing the data. We get islands of good prediction around datapoints however it quickly diverges away form the true curve after this point.

---
How can we tell if a model is overfit or underfit? #flashcard #MachineLearningUni #NeuralNetworks
	We can compare the training accuracy with the test accuracy. If the training accuracy is much higher than test it mean we have overfit. But if the training accuracy is too low we have underfit.

---
What is early stopping and how can it help with overfitting? #flashcard #MachineLearningUni #NeuralNetworks 
	The idea is there is some **sweet spot** where the network is generalizing and hasn't yet memorized the training data. We keep checking the test accuracy and once it starts to increase (even as training accuracy decreases) we stop before the network overfits.

---
What is regularization? #flashcard #MachineLearningUni #NeuralNetworks 
	**Regularization** is a technique used to control a networks flexibility. This is done to help the model not overfit the training data.

---
What is weight decay regularization? #flashcard #MachineLearningUni #NeuralNetworks 
	**Weight decay** regularization is a regularization technique where we add some cost for weights being too large in our network. This is usually implemented by adding some weight decay term so: $$E(w)=\frac12\sum_{n=1}^N||\hat y_n-y_n||^2$$ becomes $$E(w)=\frac12\sum_{n=1}^N||\hat y_n-y_n||^2+\frac\beta2\sum||w||^2$$

---
What breakthroughs lead the resurgence of neural networks? #flashcard #MachineLearningUni #NeuralNetworks 
	Pretraining, Fine tuning, Dropout, use of GPUs, CNNs, LSTMs, ReLU activation function.

---
What is pretraining and fine tuning? #flashcard #MachineLearningUni #NeuralNetworks 
	**Pre-training** is where a network can be trained once for a specific dataset and then reused - plugged into a larger network and then **fine-tuned** where the whole network is trained for a small amount of time on some task specific data-set.

---
What is dropout? #flashcard #MachineLearningUni #NeuralNetworks 
	**Dropout** is a regularization technique where every time we train the network different nodes and weights are removed (weights set to 0). This forces the network to be more robust and so generalize better.

---
What is normalization? #flashcard #MachineLearningUni #NeuralNetworks 
	This is a technique where the weights activation units between two layers are normalized so each has a normal distribution. This allows the network to train faster.

---
