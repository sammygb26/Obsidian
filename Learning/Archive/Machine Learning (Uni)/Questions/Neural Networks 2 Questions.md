Why is an error function needed to train neural networks? #flashcard #MachineLearningUni #NeuralNetworks 
	Error functions are needed to give feedback to the network; tell it what its doing wrong. It can then use gradient descent to learn form this.

---
When we are training a model what are we trying to find with respect to the error function? #flashcard #MachineLearningUni #NeuralNetworks 
	We are trying to find the minimum of the error function when the weights are allowed to change.

---
Why is gradient descent needed to optimize the weights of a model? #flashcard #MachineLearningUni #NeuralNetworks 
	There is no **analytical** solution to find the weights (closed form). Hence an approximation method is needed. Gradient descent is simple the best option.

---
Given an error function how can we find the gradients on our weights for a single node? #flashcard #MachineLearningUni #NeuralNetworks 
	We need to differentiate. This is complicated by our relatively complex neuron model functions. We can break the function into steps though and apply the chain rule. This allows us to calculate gradients in terms of gradients further up.

---
What problem can arise when pushing gradients behind a sigmoid or similar function? #flashcard #MachineLearningUni #NeuralNetworks 
	The derivative for sigmoid has values close to 0 for large and small input values.  This means the training on our network becomes glacially slow when our networks intermediate values are very small and very large.

---
How can the problem of gradient becoming very small be reduced if the last layer of our network is a SoftMax or sigmoid in the binary case? #flashcard #MachineLearningUni #NeuralNetworks 
	We can use cross-correlation error as this will cancel our the sigmoid when it comes to differentiating through.

---
What are some other common activation functions? #flashcard #MachineLearningUni #NeuralNetworks 
	Some other common ones are Tanh, ReLU aswell as LReLU.

---
What is the function for tanh? #flashcard #MachineLearningUni #NeuralNetworks 
	This would be: $$g(a)=tanh(a)=\frac{1-e^{-2a}}{1+e^{-2a}}$$

---
How is a entire network layer represented as we move from one output node to multiple? #flashcard #MachineLearningUni #NeuralNetworks 
	With multiple output nodes each node will be defined simple by a different vector of weights. All the derivations and calculation stay the same form the single case and we can just add in some index $(i)$ to the variables. Or the entire things can be compressed into a single vector multiplication followed by a non-linearity.

---
What insight allows gradient propagation through multiple layers of a network? #flashcard #MachineLearningUni #NeuralNetworks 
	We can break the network layers up as different functions. Then the chain rule means we only need the gradients on the output of some layer with respect to the loss to calculate the gradients on its weights.

---
