What is batch normalization? #flashcard #MachineLearning #BatchNormalizaiton
	Batch normalization is a special kind of modification that can be made to a neural network activation. This works to keep the outputs from the layer in a given range.

---
What are the effects of batch normal on the training? #flashcard #MachineLearning #BatchNormalizaiton 
	This allows for an increased learning rate while maintaining stability leading to a increased learning rate. Hence less epochs are needed to train a network. It also allows for less care to be taken when initializing weights.

---
How does batch norm work for a given batch? #flashcard #MachineLearning #BatchNormalizaiton 
	We process the data through the network in a batch taking advantage of **vectorization**. From this every output after each layer of the network is a matrix with a column for each example. We normalize across these examples and add a scale and shift which are learned parameters to ensure that on average the mean and variance of the activation form the layer remain the same.

---
What are some problems with batch norm? #flashcard #MachineLearning #BatchNormalizaiton 
	Batch norm can lead to instability in the evaluation phase returning NaN values. Batch norm can be seen to work better when CNNs are used but not as well with RNNs.

---
How is batch norm treated in the different test deployment and training phases? #flashcard #MachineLearning #BatchNormalizaiton 
	In the training phase the batch mean and variance used to normalize are calculate form the batch however in the evaluation and test phase these values must be estimated from the training versions.

---
What is covariate shift? #flashcard #MachineLearning #BatchNormalizaiton 
	This is when due to some later used values or the test/evaluation data not coming from the same distribution as the trained distribution. This causes the average and variance of the true activation values to be different.

---
What are the effects of batch normalization of the performance of a network? #flashcard #MachineLearning #BatchNormalizaiton 
	The network will perform better reaching a higher accuracy and lower loss in the training and evaluation phases suggesting this allows for more generalization.

---
What effects does batch normalization have on the hidden layer activation for networks? #flashcard #MachineLearning #BatchNormalizaiton 
	It has the effect of normalizing the distribution of activation values. This may help make the network more general as a wider range of values are used to explore the possibly interactions between layers giving more options for use.

---
What are the options when applying a non-linearity to neural batch normalized layers? #flashcard #MachineLearning #BatchNormalizaitons
	The options are to apply it before normalization or after. Originally it was applied before but more recent works suggest after may be a better option. 

---
Why is batch normalization through to work? #flashcard #MachineLearning #BatchNormalizaiton 
	It is through to be due to either an increase to the smoothness of the landscape being normalized similar to how normalizing the inputs to a layer helps that layer function. Or it may be due to a reduction in interdependency between layers.

---
What is internal covariate shift? #flashcard #MachineLearning #BatchNormalizaiton
	This describes a change to the internal distribution of activation vectors. If the outside changes its distribution the inside may aswell. Another way to define it is as the change in gradients calculated given the loss is higher or lower.

---
