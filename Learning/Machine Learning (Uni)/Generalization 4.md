### Universal approximation
Neural networks are universal approximators. So for every $\epsilon>0$, given any Lipschitz function $f:[-1,1]^d\to[-1,1]$ there is a network $g$ such that $$|g(x)-f(x)|\le\epsilon$$ for any $x$. The number of nodes needed to achieve this is $O(2^d)$. Where $d$ is the input dimension. Even though we can approximate many functions with NN the error matters.

There are also other **universal approximators** such as *polynomials*, *decision trees* etc. SO what makes the networks **special**. 

We have **depth separation** which means there exists function which can be approximated with small depth 3 networks, but cannot be approximated by depth 2 networks without using $O(2^d)$ nodes. Functions to show these results tend to oscillate allot.  Like for example sine functions. Which have infinite VC dimension due to their oscillating structure allowing shattering of $\infty$ points once we have the right frequency. But if *depth separation* only helps with these kinds of functions so its up for grabs if it is what makes these networks strong.?

We can also ask what can be implemented with polynomial number of nodes (instead of exponential)?. We know each node can act as a Boolean function therefore any Boolean function with $T$ steps can be implemented with a neural network of dept $O(T)$ with a total of $O(T^2)$ nodes.  So a Turing machine with $T$ operations can be implemented with a NN of depth above.

### Hardness of optimizing NNs
Training a 2-layer 3-nodes NN is NP-complete. If we can find a solution to this we will solve NP problem. The proof converts instance of NP-complete problems into datapoints and then solves. We could use **approximate solutions** but this is NP Hard!! As the loss isn't necessarily convex. ERM is hard for NNs.  

A confusing result is that the NNs loss always goes to 0 even if we use random input:

![[Pasted image 20221028153104.png]]

The reason this is believed to happen in part due to overparameterization. For example below the number state the number of parameters times the size of the dataset (**overparameterization**). Hence all we need to do is increase the number of nodes to memorize nodes.

![[Pasted image 20221028153227.png]]

**Overparameterization** means using more nodes that the number of points (however there are many ways to define it). This helps optimization but this means instead our model memorizes the data. But wouldn't this massively increase the **generalization error**. However in reality the network not trained for too long will still get very good training error and generalize for a time.

![[Pasted image 20221028153701.png]]

We find that as the size of the network increases the test error keep reducing even though we would expect it to overfit.

![[Pasted image 20221028153923.png]]

**Interpolation** is fitting a data set to training error zero (memorizing the data). The result above doesn't fit the classical result:

![[Pasted image 20221028154115.png]]

In truther there isn't a contradiction and after a while the error gets smaller again.

![[Pasted image 20221028154217.png]]

The first section is called the **classical regime** and the second is called the **modern interpolation regime**. In the graph we also cannot see the interpolation point but this is due to the number of nodes required being very specific.

![[Pasted image 20221028154616.png]]

So overparameterization makes ERM easier and also makes overfitting harder.

### Kinds of overfitting

![[Pasted image 20221028154712.png]]
(from paper Mallinar et al)
These are the three kinds of **overfitting** benign is the idea way where as it is through that NNs create tempered overfitting.

### In Proactive
We always start by minimizing training error as we must overfit to need to regularize. Hence why we start with the ERM and then regularize.
