What are the two calculations that go into making a neural network layer/node function? #flashcard  #MachineLearning #BasicNeuralNetwork
	Each layer/node takes in some activation vector in layer $l$ of size $n_{l-1}$. In the case of a node a $z$ activation is found by doting this with the $w$ vector. In the case of a layer the $z$ activation vector is found by right multiplying $a^{(l-1)}$ with $W^{(l)}$. We then add on a bias of size $b$ to make up $z^{(l)}$. This is then passed through our activation function to give $a^{(l)}$

---
What is the dimension of the weight matrix and bias vector from some layer of size a to some layer of size b? #flashcard  #MachineLearning #BasicNeuralNetwork 
	We need to take in an $a$ size vector and give a $b$ size vector. Hence our matrix must be $(b, a)$ $b$ rows and $a$ columns. Our bias vector $b$ must be a column vector of size $b$. Hence $b$ rows and 1 column $(b,1)$.

---
Why is random initialization required for neural networks? #flashcard  #MachineLearning #BasicNeuralNetwork 
	Without this all nodes in the network will have the same gradients with respect to their weights. Hence each node will end up doing the same calculate after each iteration causing the network to act as if each layer only has one node.

---
