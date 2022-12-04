This type of network expands on [[GANs (Goodfellow et al)]]. GANs provide **attractive alternative** to **maximum likelihood techniques**(?). Lack of heuristic cost function can also be useful i.e. the **discriminator** defines the cost function. 

### Findings
1. GANS are **unstable to train**: proposed solution is **DCGAN** (Deep Convolutional GAN).
2. Trained **discriminators** can be used for image classification.
3. GANs empirically show specific filters have learned to draw specific objects.
4. Generators have interesting properties allowing for manipulation of outputs.

### Model Architecture
This was motivated by failing attempts to scale up GANs using CNNs to model images. The approach here is motivated by three factors

1. **Convolutional Nets** (Springberg et al) replacing deterministic special pooling functions with strides convolutions. So the network learns its own spatial down sampling. This is applied to both the **generator** (learning its own special upsampling) and the **discriminator**.
2. Removing fully connected layers from the top of the convolution. One option is **global average pooling**. This was found to **improve stability** but **reduce convergence speed**. Instead the highest convolutional features are connected to the input and output of the generator and discriminator respectively. E.g. the first layer of the generator is basically a matrix multiplication outputting a 4D tensor volume. The last layer of the discriminator outputs a projection of the final convolutional volume to a single value.
3. **Batch Normalization** to stabilize learning and reduced the likelihood of **mode collapse**. Using purely batch norm on all layers causes oscillations and model instability.

Furthermore **ReLU** was used on generator layers accept for the last layer (using tanh instead). The tanh function was found to work well allowing the color space of the output to be saturated faster.

**Setup for training** - Images were rescaled to $[-1,1]$ to match tanh output. Minibatch size 128, weights initialized to 0 centered normal with deviation 0.02. LeakyRelU used negative slope of 0.2. Adam sed with learning-rate of 0.0002 (rather than 0.001 to increase stability). **Momentum** set to 0.5 instead of 0.9 to increase stability.

### DCGAN Capabilities
Classifier trained on features from all layers of the discriminator achieved 82% accuracy showing network learns meaning full representations (or just some information could be achieved). Also trained L2-SVM classifier on features extracted from discriminator after training on SVHN this gave state of the art performance 22.8% error with the L2-SVM and wasn't down to the network architecture as training the some architecture in a labeled way achieved 28.9% error.

### Visualizing Internals of the Network
**Waling in the manifold** - sharp transitions may show overfitting has taken place. The walks between random points in this space add and remove objects which suggest the points themselves are semantically important and hence the generator is learning some representation.

**Visualizing the discriminator Features** - Using [[Guided Convolutions (Mostafa et al)]] shows features learned represent part of specific objects in room (this is training of SVHN).

**Forgetting objects** - authors managed to train logistic regression to identify features in the second highest layer (a presume the 1st as 200 features are removed). The linear classifier used activations inside bounding box as positive and random samples as negative. Then the 200 feature maps with positive weights were removed and replaced with noise in all images. This removed windows in this case form rooms.

**Vector arithmetic** 
In word representations it was found that learned word vector representations obeyed some linear arithmetic. $\text{vector}(king)-\text{vecotr}(man)+\text{vector}(woman)\approx\text{vector}(queen)$ being a classic example.
