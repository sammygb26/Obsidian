# Batch Normalization
*Batch Normalization* (Batch Norm) is a special type of activation layer in a neural network just like other [[Activation Functions]] like **ReLU**, **sigmoid** or *soft-max*. The effect of *Batch Norm* is it stabilizes the learning process and increases the learning rate, reducing the number of epochs needed to train a network. A simple implementation is as follows:

![[Pasted image 20220703192353.png]]

Basically we are finding the *mean* and *variance* of the activations of a layer in some batch. This is used to standardize the batch as a whole before the values progress to the next layer in the network. A **scale and shift** is also added so that control can still be maintained in the range of values sent to the following layer. If the layer is $d$ dimensional then each dimension can be *normalized* individually.

![[Pasted image 20220703192739.png]]

The $\epsilon$ term is added for numerical stability and is some small constant. The *scale and shift* terms $\gamma$ and $\beta$ can be learned by the network.

### Clear Benefits
**A DNN can be trained faster** the training iterations will be flower due to the extra normalization calculation during the forward pass and additional *parameters* to train during backpropagation. Overall it converges much quicker .

**Higher learning rate** instead of using small learning rates as usual back propagations allows much larger learning rates. This is afforded by the stability of the gradients and hence training takes less time.

**Easier to initialize weight** it can be hard to choose the correct weights for a network but *Batch Norm* reduces how much initial weights affect the network .

### Problems
Sometimes *normalization* can lead to **instability** in the evaluation phase. In this case the network will return NaN.

**Batch Normalization** is also seen as superior when *CNNs* are involved but **RNNs** work better with [[Layer Normalization]]

### Test/Deployment vs Training Phases
In the real world and when testing we cannot normalize over some values in a *batch* we must normalize each batch at once. One way of doing this is to use the batch stats as estimations of $\mu$ and $\sigma^2$ for the population but this only makes sense for testing as in deployment we have no batch to predict. In the *evaluation* phase the average of the $\mu$ and $\sigma^2$ used in training can be used. We can do this by taking a exponentially weighted average of the minibatch $\mu$ and $\sigma^2$ values. This gives the highest weight to the earlier batches but doesn't discount all batches. We keep this over all the batches we have computed.

A problem with this comes when some value the network isn't used to is inputted. Since the mean and variance was calculated with the training data. Hence with these values which are not taking into account when calculating the $\mu$ and $\sigma$ may have a normalized distribution where $\mu\neq0$ and $\sigma\neq1$. This shift is called **covariate shift**. This means the training set must be *"similar enough"* to the evaluated data.

### Results from Test
The *underlying mechanism* for batch norm isn't fully understood however it does clearly work. Bellow is the results from the original paper:

![[Pasted image 20220703195601.png]]

The results show **BN** is clearly faster aswell as allowing a wider range of training rates while still *converging*. It can be seen comparing the same network with and without *BN* that BN increases the accuracy and decreases the loss (even in the limit).

![[Pasted image 20220703200041.png]]

It can also be seen that using **BN** affects the *activation values* in the hidden layers of the network. With BN the values change much more smoothly and settle to a distribution that is less skewed.

![[Pasted image 20220703200957.png]]

The main results as seen at the top of this section show just adding **BN** layers dramatically increases learning but the best case is achieved when also modifying the learning rate to take advantage of this. We can also see *large datasets are more affected*. The higher learning rates unlocked by **BN** allows. This type of training also allows sigmoid activation functions to be trained effectively which wasn't possible without **BN**. The noise created by the batches having different averages and variances causes regularization and helps reduce overfitting.

### Applying Nonlinearity
There is debate as to whether the *non-linearity* should be applied before or after batch normalization. The original position is right before the **non-linearity** and this ensures that the distribution is better controlled.  However some more recent work suggests the best approach is to have the **BN** layer right after the *non-linearity*.

### Why it works
We know it does work but **why**? This isn't fully known yet however there are some hypotheses. The *original paper* assumes BN effectiveness is due to the **reduction** of what they called *internal covariate shift*. But this has been refuted by a recent paper. Another hypothesis is it *mitigates the interdependency between layers during training*. The paper refuting the original hypothesis also states it is due the increasing the **smoothness** of the landscape being optimized.

##### What is (internal) covariate shift
**Covariate shift** describes a shift in the model input distribution. *Internal Covariate Shift* describes how the same shift just in the internal activations. This shift can come for example from the type of data in the evaluation not being present during training.

**ICS** can also be defined from an optimization perspective in this case it refers to the change in gradients calculated given then loss is one higher or one lower.

[[Batch Normalization Questions]]