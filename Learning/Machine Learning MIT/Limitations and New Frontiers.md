# Limitations and New Frontiers
Deep learning has been able to revolutionize many domains. We've looked at the learning problem in general. Taking in some data and giving some output but also generating some data. What these networks do is learn a function, they approximate a function. This comes back to the **Universal Approximation Theorem** which states a feedforward network with a single layer is sufficient to approximate to an arbitrary precision any continuous function. This isn't even a deep network but just a single layer. This means that any function taking in a set of input and output can in theory be modeled by a neural network. But no claims are made on the number of neuron needed to get a good approximation. It also doesn't state what weights you would need and how to find them. It also doesn't apply any *generalization* and may only work with the given inputs.

### Limitations
One of the key limitations is *generalization*. How well will our network perform on inputs not seen during training. This can be seen when we consider how well a trained model does in a training set compared to a testing set when we *randomize labels*.

![[Pasted image 20220527175206.png]]

The model could train no matter what so modern networks can perfectly fit to random data. Hence the *universal approximation theorem* is being show to be used here. Another problem is outside of our networks with new data we have no idea how our network will perform outside of our training data.

![[Pasted image 20220527175513.png]]

This comes into the idea of failure modes. When we have a neural network it can fail understand real world data as it may wrongly expand form its original data. It may take the wrong lessons from the data and we cannot know how it will act in the real world. We need to know then the results are likely to be correct or false. This also need to be used for spares, noisy and imbalanced data so we can have some assurance as to how it will act.

#### Uncertainty
We can look at an example where we classify an image as either cat or dog. We output a probability of this over a *fixed number of classes*

![[Pasted image 20220527180639.png]]

So what about if the image is cat and dog? We can use our model to give a probability but the probability doesn't give a confidence in the prediction. This type of uncertainty is **aleatoric uncertainty** (data). We can also input in image of a horse which the network cannot classify. The network may classify this as a dog or cat but it should also be able to specify how uncertain it is in this as it is different from the training images. This is **epistemic uncertainty** (model).

### Adversarial Attacks
Another problem is adversarial examples. Here we construct some data that takes some image and some perturbations to it. To us these images look the same but the network considers one correctly and the other wrong.

![[Pasted image 20220527181218.png]]

We apply *gradient descent* to optimize some $\mathcal L$. We fix the input and ask about the label. We can instead fix the *weights* and change the label. We seek to then increase the loss. You can even make robust examples that are misclassified. It was even shown you can print something into the real world and it will still be classified wrong.

### New Frontiers
One new field is encoding structure into deep learning architectures. We want to encode our architecture to be better suited to some problem. An example is **CNNs**. Here the convolution is liked to the idea of spatial structure in images. 

*Graphs* are a structure that many data takes the form of hence much research has been put into encoding new data structures past the standard encodings like these *graphs*. In CNNs we slide a matrix over a network. In *Graph Convolutional Networks* or (GCNs) we represent our data as a set of nodes and edges. Like like a weight matrix we learn the weights for feature kernel. The kernel then traverses the graph and encodes the neighboring nodes. We can iteratively apply this to extract information about the local graph structure. These networks can now be used in *chemistry and biology* where the molecules are represented as nodes in the structure. This was even used to find a new antibiotic compound that works differently to standard antibiotics. This can also be used for *traffic prediction*.

Another data type is point clouds where we try to perform computation on an unordered set of points. We can even use GCN techniques after encoding these representations into a graph to do much of the computation.

Another new frontier is automated machine learning: learning to learn. The problem is it require a bit of practice and trial and error to make a neural network for a task. The idea here is to use *machine learning* to solve this. It designs the models! This can be done with AutoML. A classic example is done in a Reinforcement Learning setting where we have a controller and a child network. The controller chooses the child hyperparameters. We run the child and reward the controller based on how well the child did. This also just becomes general architecture search problems. These architectures in many cases work better than human designed ones.

![[Pasted image 20220527183909.png]]

