What are optimizers and optimization? #flashcard #MachineLearning #Optimizers
	Optimization is the process of finding the weights that minimize the cost/loss of the model as compared to the data. The optimizers are algorithms that are able to efficiently find these values.

---
What is stochastic gradient descent? #flashcard #MachineLearning #Optimizers 
	SGD is one of the simpler optimizers. Like many it uses the gradients calculated through pack propagation through the neural network. Technically it takes place over just one example from the network at a time. But generally it is called SGD and a subset **batch** of the examples is used.

---
Why does mini-batch gradient descent work?  #flashcard #MachineLearning #Optimizers 
	The idea with minibatch gradient descent is we train on small portions of our training example set. This speeds up how often we change the gradients for large networks. It however means the gradients will change depending on the batch we are optimizing for. However the vastly greater amount of steps taken means we will still converge quicker to a general minima.

---
What is an exponentially weighted average?  #flashcard #MachineLearning #Optimizers 
	An exponentially weighted average is a moving averaged calculated via a recurrent function. Each time we get a new values $\theta$ we update the average $$V_\theta:=\beta V_\theta+(1-\beta)\theta$$This causes $V_\theta$ to be a weighted average where the effect of each past $\theta$ is exponentially weighted into the calculation. The factor $\beta$ controls this.

---
How can bias correction be performed with an exponentially weighed average and why is this needed?  #flashcard #MachineLearning #Optimizers
	We initialize $V_\theta$ to be $0$ hence it will take some time to discount its initial state and reach the true value. We can set $V_{\theta}^{\text {Corrected}}$=$\frac{V_\theta}{1-\beta^t}$ where $t$ is the number of iterations since $V_\theta=0$.

---
What is gradient descent with momentum?  #flashcard #MachineLearning #Optimizers
	This is an alteration to standard gradient descent where we instead of taking of the learning rate times the calculated gradients we take of the learning rate times the weighted moving average of the gradients.

---
What is RMSprop?  #flashcard #MachineLearning #Optimizers 
	This is an alteration to gradient descent where we take a weighted average of the squares for the gradients. We then take of the true gradients divided by the square root of this working average.

---
Why is gradient descent with momentum through to work?  #flashcard #MachineLearning #Optimizers 
	It will smooth out instable gradients reducing the need for a low learning rate and causing the step taken to be more largely in the same direction hence less are steps are needed again.

---
Why is RMSprop through to work?  #flashcard #MachineLearning #Optimizers 
	It will shrink gradients down such that small but stables ones are larger but large unstable ones are smaller. Hence creating a gradient that is more stable and even.

---
What is the Adam optimizer?  #flashcard #MachineLearning #Optimizers
	Adam is a combination of RMSprop and momentum optimizers. It takes two exponentially weighted averages one of the gradients and one of the squares of the gradients. We then take of the weighted average of the gradients average and divide it by the square root of the gradients square average. 

---
What is learning rate decay?  #flashcard #MachineLearning #Optimizers 
	Learning rate decay is a technique where by we start with an initially high learning rate and over time reduce it to make the finally result from out network smaller and smaller. This can be done with a simple formula like $$\alpha=\frac1{1+\text{decay-rate$*$epoch-num}}\alpha_0$$Where $\alpha_0$ is the initial decay rate.  Many other formulas can be used however

---
What the local optima problem and why is it no longer through to be a problem with large networks?  #flashcard #MachineLearning #Optimizers 
	This is the problem where our parameters get stuck in a local optima where all the gradients are 0 however we are not at the true minima so we may still have a high loss. This isn't thought to be a problem in higher dimensions as each of these minima must have all gradients being convex. If even one is concave we will have a saddle instead with a possible way our given by small distortions to the gradients.

---
What problem replaced the local minima problem when training large networks?  #flashcard #MachineLearning #Optimizers 
	This was replaced by the plateau problem where small gradients can cause learning to slow down massively.

---
