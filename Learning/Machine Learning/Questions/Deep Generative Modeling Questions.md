What is the main goal of deep generative modeling? #flashcard #MachineLearning #DeepGenerativeModeling
	The goal with deep generative modeling is to generate synthetic new data based on some training subset. The key idea allows for the learning of a model that reflects the data and may then be used elsewhere. Some examples are density estimation, outlier detection and sample generation.

---
What are latent variables? #flashcard #MachineLearning #DeepGenerativeModeling 
	Latent variables can be thought of as the hidden features that describe some sample from a distribution. When given a list of all the latent features a sample can be reconstructed. When we learn an effective representation of some data in a lower dimensional space we need to learn these features in order to model the object.

---
What are the two main types of generative models and what are they also an example of? #flashcard #MachineLearning #DeepGenerativeModeling 
	The two main examples are autoencoder and GANs (generative adversarial networks). These are both examples of latent variable models.

---
How do autoencoders work? #flashcard #MachineLearning #DeepGenerativeModeling 
	The idea with an autoencoder is we start with some high dimensional input $x$. A series of layers reduces this to some latent space vector $z$ which is lower dimensional. A further series of layers scales this up to be the same size again giving $\hat x$. We can then train the network by measuring its loss as how far $\hat x$ is from $x$.

---
What is the loss function of a standard autoencoder? #flashcard #MachineLearning #DeepGenerativeModeling 
	The loss function of a standard autoencoder will the the difference between the output predicted from the latent space vector $\hat x$ and the true input $x$ squared. $\mathcal L(x,\hat x)=|x-\hat x|^2$ This is called the **mean squared error**

---
What is a variational autoencoder? #flashcard #MachineLearning #DeepGenerativeModeling 
	A variational autoencoder is an expansion of a normal autoencoder where instead of outputting a single latent vector from the encoder side we output a mean vector and standard deviation vector. We then input a sample from the normal distribution described into the following layers.

---
How is the loss for a variational autoencoder different from a normal autoencoder? #flashcard #MachineLearning #DeepGenerativeModeling 
	A variational autoencoder has a reconstruction loss as before but also a regularization term. This is $D(q_\phi(z|x)||p(z))$ where $D$ is the divergence function between the the probability of $z$ and the predicted probability of $z$. This way the loss ensures $q_\phi(z|x)$ is brought closer to being normally distributed. This makes the KL-divergence when the distribution used is normal.

---
How does a gaussian distribution lead to regularization? #flashcard #MachineLearning #DeepGenerativeModeling
	With regularization we want our latent space to be meaning along as the value are close to the average no missing gaps that give rubbish results. This is called *completeness*. We also want *continuity* that is points that are close together have similar values once decoded.

---
What is the problem with training variational autoencoders  and how can this be solved? #flashcard #MachineLearning #DeepGenerativeModeling 
	The problem with training variational autoencoders is the $z$ term is random so how can we propagate gradients through it. To get around this we can create a new value $\epsilon$ that is our error term. All the randomness goes into this and we just even try to change it. The gradients now flow past this random part.

---
What is a benefit of variational autoencoders when it comes to disentanglement? #flashcard #MachineLearning #DeepGenerativeModeling 
	The benefit is similar output come from a similar part of the latent space. Therefore as we vary through this space we can generate new samples not seen in our training that are also similar in size.

---
How do generative adversarial networks work? #flashcard #MachineLearning #DeepGenerativeModeling 
	Generative adversarial networks work by having two networks competing against each other. These are called the *generator* and the *discriminator*. The generator's job is to take in some random noise $z$ and generate some fake sample $X_{fake}$. The *discriminator* then compares this to some real value $X_{real}$. The generator is treated well if discriminator thinks its fake sample is the real one and the opposite for the discriminator. This way the discriminator continually improves to better identify real samples while the generator better fakes samples. This way they both push each other to get better.

---
What is the loss for a generative adversarial network? #flashcard #MachineLearning #DeepGenerativeModeling
	Use a form of cross entropy loss of the predicted value compared to the true value. We then try to minimize the this with respect to $G$ (so take away gradients * learning rate) and maximize with respect to $D$ so (add gradients * learning rate).

---
How can an interpolation across the noise input to the generator in an adversarial network been seen in its output? #flashcard #MachineLearning #DeepGenerativeModeling 
	This can be seen as an equal interpolation in the output space. In this way we can think of the generator as performing a transformation from one space to another.

---
What are progressive growing GANs? #flashcard #MachineLearning #DeepGenerativeModeling 
	The idea here is to get the larger details worked out first we start with a small generator and discriminator. We use a downscaled version of the input We train then we increase the number of layers each layer until we reach the input image size.

---
What are conditional GANs? #flashcard #MachineLearning #DeepGenerativeModeling 
	Conditional GANs incorporate a controlled label aswell as a noise input. We then compare only images with the same label. This way be specifying a label and a noise value we can generate aswell as choose what kind of thing we want the network to generate. This may be useful if the same underlying representation in the network can generalize to al applications.

---
What is pared translation? #flashcard #MachineLearning #DeepGenerativeModeling 
	The idea here is to take out input image as the input to our generator and generate some output form this. We then compare if the pair generated looks fake compared to a real one.

---
What is CycleGAN and what does it allow? #flashcard #MachineLearning #DeepGenerativeModeling 
	Cycle GAN instead of taking a random value to data manifold we take a data manifold to another data manifold. This can be used for applications such as image to image or video to video domain translations.

---
