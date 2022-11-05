What is the difference between a standard neural network and a deep neural network?  #flashcard #MachineLearning #DeepNeuralNetwork
	This would simply be the number of layers in use. With more than 2 beginning to be considered deep.

---
What does more layers in a neural network allow?   #flashcard #MachineLearning #DeepNeuralNetwork 
	This allows for more complex functions and higher order inference to be carried out. Few layers may be able to say form an image find simple shapes and lines while deeper layer may be able to model shapes and objects. 

---
How is the structure of a standard dense neural network captured?   #flashcard #MachineLearning #DeepNeuralNetwork 
	The connections form one layer to the next are captured by a weight matrix where each row describes the weighted sum that will give the z values for the following layer. each layer then also has a bias vector applied to get the z value and an activation used to get the a value.

---
How are the number of layers calculated in a NN?   #flashcard #MachineLearning #DeepNeuralNetwork 
	This would be all the layers bar the initial input layer and activation sometimes labeled as layer 0.

---
How is forward propagation performed mathematically over the layers of a DNN?   #flashcard #MachineLearning #DeepNeuralNetwork 
	we start with the input feature vector $x$. Then each following layers activation till the final layers (the output $\hat y$) are calculated gives the following recursion.$$z^{[l]}=W^{[l]}a^{[l-1]}+b^{[l]}\hspace{64pt}a^{[l]}=g^{[l]}(z^{[l]})$$ With $W$ being the weight matrix, $b$ the bias column vector and $g$ the activation function. Then $z$ is the $z$  value and $a$ is the activation value. For some object $o^{[l]}$ means $o$ is of layer $l$. We initialize $a_0$ to be $x$ and then $\hat y$ is $a^{[L]}$ where we have $L$ layers in our network.

---
What must each layers keep stored in order to perform back propagation?   #flashcard #MachineLearning #DeepNeuralNetwork
	The input activations as well as the layers $z$ values must be cached. The later to allow backpropagation through the activation function and the former to allow the derivative of cost with respect to the weight matrix to be found.

---
How is back propagation implemented in a standard dense neural network layer?   #flashcard #MachineLearning #DeepNeuralNetwork
	The gradients for the activation out of the layer are given. This can be through of as telling the layer how it must change its output to minimize loss. This can be combined with the cached $z$ values and the derivative of the activation function to give the change in the $z$ values needed. Overall the chain rule is used to propagate these changes through the other objects calculated within the layer. This will Then output the derivatives for $W$ and $b$ for that layer aswell as the change required of the next layer.

---
What are the train dev and test sets in machine learning?   #flashcard #MachineLearning #DeepNeuralNetwork 
	These sets are used to train the network, evaluate this trained network to pick better hyperparameters and finally test the overall success of the network.

---
Why are the dev and test sets kept separate?   #flashcard #MachineLearning #DeepNeuralNetwork 
	The dev set is used to try out different hyper parameter values. This runs the risk of the hyperparameters being fit to the actual dev set. Instead the train set is used to stop this type of fitting and give a more accurate evaluation of the data.

---
What is bias and variance when it comes to neural networks?   #flashcard #MachineLearning #DeepNeuralNetwork 
	Bias can be through of as how fit the network is just to the training set relative to what is possible (usually humans). When the network doesn't even predict the training set is can be said to have high variance. The idea with variance is the network will fit the training data but not generalize to the test or dev data. This is spotted by a much higher dev/test set error. It can be imagined as the boundary described by the network being very irregular.

---
What is a basic set of steps to train a network and find good hyperparameters?   #flashcard #MachineLearning #DeepNeuralNetwork 
	Its easiest to take this in two steps first we train the network only on the training data and attempt to get a low training set error. If this isn't found we can use a bigger network, training longer or use another architecture. Then we compare the network to the dev set to test for overfitting. If this is found we need whether more data, regularization or another architecture.

---
When it normalizing inputs and what effect does this have on the training of a NN?   #flashcard #MachineLearning #DeepNeuralNetwork 
	Here we make the bias and variance of every feature 0 and 1 respectively.  This allows for higher learning rate to be used and so quicker learning for the network. This happens as the landscape we are optimizing over will be more regular leading to more stable gradients the point in a more useful way toward the minima.

---
What are vanishing and exploding gradients?   #flashcard #MachineLearning #DeepNeuralNetwork 
	This problem arises when the weights of a matrix are consistently above or bellow 0. The gradients will then rise or fall exponentially with the number of layers. This can be somewhat overcome with smart weight initialization.

---
How should the weight of matrix be initialized with respect to their size?   #flashcard #MachineLearning #DeepNeuralNetwork 
	The overall size of the network should be around 1 to prevent exploding and vanishing gradients. Hence we should normalize by the number of input nodes. For example dividing by $n^{[L-1]}$. But half of this works well for ReLU but just the original works well for tanh.

---
How can gradients be numerically approximated?   #flashcard #MachineLearning #DeepNeuralNetwork 
	A network's gradients can be numerically  by for each value we want the gradient of taking the loss with some slightly higher and some slightly lower . The small difference in the value will be $\epsilon$ we can take the difference in these two and divide by $2\epsilon$ for small values of $\epsilon$ this will approximate the value for the gradients.

---
What is gradient checking?   #flashcard #MachineLearning #DeepNeuralNetwork
	Gradient checking is a numerical approximation technique where proximate gradient techniques are compared to the calculate ones. This can be used to debug NN programs and find where math errors may back snuck in. It can however not be implemented with dropout.

---