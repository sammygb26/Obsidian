Broadly what can feed forward neural networks be used to do? #flashcard #MOB #FeedforwardNeuralNetworks
	They can be used to approximate functions. That is a task that takes in some input vector and outputs some vector and that we can learn we can use neural networks to solve.

---
What are some examples of tasks that can be performed by neural networks? #flashcard #MachineLearningUni #Optimization 
	Neural networks can perform tasks such as object classification, depth perception and semantic segmentation.

---
What are hidden units in neural networks? #flashcard #MachineLearningUni #Optimization 
	Hidden units are the units of the values passes inside the network. Their range is controlled by the activation function applied over the node activation (input weighted sum).

---
What are convolutional neural networks? #flashcard #MachineLearningUni #Optimization 
	Convolutional neural networks instead of training for a weight and bias matrix instead perform a convolution operation on each layer. This instead of taking a vector to a vector takes a 2D or 3D matrix to a 2D matrix.

---
What is stride when it comes to convolutions? #flashcard #MachineLearningUni #Optimization 
	Stride is the distance we move the convolving matrix over the input matrix for each output pixel. With a stride of 1 this means we perform a convolution for every possible combination of pixels.

---
How does the number of filters change the output from a convolutional layer in a neural network? #flashcard #MachineLearningUni #Optimization 
	This gives the number of output layers. If we take in say a RGB image we have three input layers. But applying $K$ filters we get $K$ output layers. This gives us a feature volume rather than a grid.

---
What is the width out of a convolution given the width in, kernel width and padding? #flashcard #MachineLearningUni #Optimization 
	This will be for a kernel size $m$ and padding $P$ $$W_{out}=\frac{W_{in}-m+2\times P}S+1$$

---
What is the height out of a convolution given the height in, kernel height and padding? #flashcard #MachineLearningUni #Optimization 
	For a kernel size $m$ and padding $P$ this will be $$H_{out}=\frac{W_{out}-m+2\times P}S+1$$

---
What other layer is used in Convolutional Neural network commonly other than a convolution layer? #flashcard #MachineLearningUni #Optimization
	A pooling layer will be used. This reduces the size of the layers by breaking it into different chunks of a given pool size and then picking the largest or most active cell as the value for the new created cell.

---
