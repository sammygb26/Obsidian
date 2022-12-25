What does the universal approximation theory state mathematically? #flashcard #MachineLearningUni #Generalization #Generalization4
	This would be that for every $\epsilon>0$, given any Lipschitz function $f:[-1,1]^d\to[-1.1]$ there is a network $g$ such that $$|g(x)-f(x)|\le\epsilon$$For any $x$. Where the number of nodes needed to achieve this is $O(2^d)$.

---
What are some other universal approximators other than NNs? #flashcard #MachineLearningUni #Generalization #Generalization4 
	Polynomials and decision tress are also universal approximators. Hence this isn't what makes NNs special.

---
What is depth separation? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This is the idea that as the depth of the network increases function not possible to approximate before becomes possible even with a limited number of nodes. Or just not exponential $O(2^d)$

---
What is the VC-dimension of a sine function? #flashcard #MachineLearningUni #Generalization #Generalization4 
	As we can place all our points in a line then all we need for any given labeling is a frequency making all the points above the sine curve or bellow a sine curve has an infinite VC dimension.

---
What is the VC dimension of a neural network asymptotically? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This would be for $E$ edges in the network $$O(|E|\log|E|)$$

---
What order of nodes is required to implement a Turing machine on a NN with $T$ operations? #flashcard #MachineLearningUni #Generalization #Generalization4 
	We would need on the order of $O(T^2)$ nodes to do this.

---
What order of hardness is training a 2-layer 3-node network? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This problem is actually NP-complete. This is proved by converting a NP problem into a space of datapoints and if we can minimize the loss we have solved the problem.

---
What is the hardness of approximating ERM and what makes it hard? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This is an NP-hard problem. Partially due to the loss function not always being convex and ERM being hard for NNs.

---
For NNs what is the limit on training data that can be optimized for? #flashcard #MachineLearningUni #Generalization #Generalization4 
	There is not limit and in fact we can minimize loss for random data and still get 0 loss.

---
What is overparameterization? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This is where far more nodes than datapoints are actually used leading to the network memorizing the data quickly.

---
What are the expected problems with overparameterization? #flashcard #MachineLearningUni #Generalization #Generalization4 
	We could expect a high approximation error as we would have a larger hypothesis class and we would expect our network to just memorize the data.

---
What happens to performance in practice with overparameterization? #flashcard #MachineLearningUni #Generalization #Generalization4
	In practice the network continues to generalize and the performance continues to improve.

---
What is interpolation? #flashcard #MachineLearningUni #Generalization #Generalization4 
	Interpolating is a stage after overfitting where the capacity of $\mathcal H$ is so large we no longer just memorize the data but interpolate between points.

---
What is the point at which the capacity of H begins to hurt the generalization less called? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This is called the interpolation threshold.

---
What are the three kinds of overfitting? #flashcard #MachineLearningUni #Generalization #Generalization4 
	These are benign, tempered and catastrophic.

---
What is benign overfitting? #flashcard #MachineLearningUni #Generalization #Generalization4 
	Here we memorize the data but only at the points in our dataset everywhere else follows the underlying distribution nicely.

---
What is tempered overfitting? #flashcard #MachineLearningUni #Generalization #Generalization4 
	This is basically interpolation between datapoints we are overfitting but it remains as close as our datapoints were.

---
What is catastrophic overfitting? #flashcard #MachineLearningUni #Generalization #Generalization4
	This is where we fit the data but in doing so loose any underlying distribution and become wildly inaccurate.

---
