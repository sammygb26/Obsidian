# Deep Generative Modeling
This is a different type of task where we generate synthetic new data base don some training subset. This is an example of *unsupervised learning*. As apposed to *supervised learning* where we have a pair of data $(x, y)$ and we want to learn the function $x\to y$. In *unsupervised* take just some data $x$ and we attempt to learn the underlying structure of the data. **Deep Generative Modeling** is an example of . We take in data that is distributed bellow some model and we want to generate out own model represents the the data.

![[Pasted image 20220517144327.png]]

Examples will be *density estimation* and *sample generation*. In both cases we are looking to predict $P_{model}(x)$ to be similar to $P_{data}(x)$ where $x$ is highly dimensional.

This is useful as our models learn *underlying features*. We can then work to make our models fair and equal over these underlying features.

Another example is outlier detection which can be used in self driving cars. We estimate the probability distribution and then highlight outliers.

![[Pasted image 20220517144842.png]]

The two types of classes of generative models we will look at are *autoencoders* and *generative adversarial networks* (GANs). Both of these are examples of **latent variable models**

#### What is a latent variable
Latent variables can be through of as the underlying variables that describe some behavior. If the behavior was a shadow on the wall the variables would be the objects actually casting those shadows. The goal is to learn the true facts therefore to learn the *latent variables*.

## Autoencoders
This is a simple generative mode. The idea is to build an encoding of the input that allows us to recreate the original input.

![[Pasted image 20220517145527.png]]

We encode the higher dimensional input into a lower dimensional segment $z$. This gives a compressed and hopefully meaning full compression of the input data. So the *encoder* (green) learns to generate $z$ from $x$. We also have a *decoder* (blue). This takes $z$ and predicts $x$ giving $\hat x$.This will be an imperfect reconstruction of the data. We evaluate the loss of this network as the summed differences between $x$ and $\hat x$.

![[Pasted image 20220517145749.png]]

This is called the *mean squared error*. Giving the following as a simplified version. This is a way of extracting latent variables in $z$ is completely unsupervised and the number of latent variables gives us more and more control over the actual final product.

![[Pasted image 20220517150020.png]]

We learn a compressed representation of the input data automatically. From this we can also get *variational autoencoders* witch is more commonly used.

## Variational Autoencoder
In the original version is completely deterministic instead we want to incorporate some element of randomness to make the representations learnt less brittle and more complete.

![[Pasted image 20220517151048.png]]

The way this is done is we break the $z$ vector into a mean and a standard deviation. The encoder outputs these two vectors giving a distribution of $z$. We then sample from this distribution to get out value to pass through into the decoder. Both the network will now be probabilistic in nature. We learn two sets of weights $\phi$ and $\theta$  which we will then compute our loss over.
$$
\mathcal{L}(\phi,\theta,x)=(\text{reconstruction cost})+(\text{regularization term})
$$
We still have our reconstruction cost but also we add a regularization term. The reconstruction loss is the same as before in regular autoencoders.

#### Regularization Term
This is a new term added for when we  are using *variational autoencoders*. It is defined as 
$$
D(q_\phi(z|x)||p(z))
$$
Where $D$ can be through of as the difference / divergence between the two distributions $q_\phi$ and $p$. $q_\phi(z|x)$ is the distribution we are learning our prior will be $p(z)$ that is what our decoder predicts is the chance for $z$. This ties our encoders output to our decoders interpretation of it so the two don't diverge too much. This helps preventing certain parts to *overfit* and so smooths out and improves the quality of our output distribution.

We need to choose a prior a common choice is a *Normal* or *gaussian* distribution where. $$P(z)=\mathcal N(\mu=0,\sigma^2=1)$$This encourages our encoder to place latent variables evenly around the latent space. Now that we are using the gaussian distribution we can find our original $D(q_\phi(z|x)||p(z))$ to be the *KL-divergence*.
$$=-\frac12\sum_{j=0}^{k-1}(\sigma_j+\mu_j^2-1-\text{log}\hspace{3pt}\sigma_j)$$

#### How does the gaussian allow regularization
We may think why are we choosing the gaussian isn't it a bit arbitrary. Well we may consider what we want from our latent space's properties. We *continuity* meaning points that are close in latent space have similar content after decoding. We want *completeness* sampling from latent space gives "meaningful" content after decoding. Without regularization points that are close together may not be similarly decoded.

So how does *regularization* help with this. By dragging all distributions back to the center and having greater loss further away we ensure our different groups centers are close together. Without this we may have caps between where the decoder has not trained therefore giving many useless outputs when we sample there. The variance is also regularized to 1 ensuring similar contents must be close together

![[Pasted image 20220517153907.png]]

In reality the *reconstruction* quality can suffer with more regularization.

#### Training variational autoencoders
The problem here is that by adding a variation in the middle of our network from the creation of a $z$ distribution passed onto a value to the decoder. We can't propagate gradients through the stochastic layer. To solve this problem we reparametrize $z$ such that $\mu$ and $\sigma$ are fixed vectors but we calculate $z$ as $$z=\mu+\sigma\circledcirc\epsilon$$ Now $\epsilon$ is a random term we can divert our randomness here and so maintain the gradients over the middle layer.

![[Pasted image 20220517161153.png]]

#### Latent space disentanglement
The benefit of variational autoencoders is when changing latent variables we can vary the output to generate results that are different from our training set.

![[Pasted image 20220517160517.png]]

We want latent variables that are uncorrelated with each other. With a $\beta$-VAE we also include the hyperparameter $\beta$ that controls the *strength* of our regularization term. With $\beta>1$ will encourage a more efficient latent encoding that will lead to disentanglement.


## Generative Adversarial Networks
The key problem with variable autoencoders is a problem of estimating the probability of the latent variables $z$. Instead we can ignore this to focus on generating new samples. We want to sample from a complex distribution but this is very hard when there any many many variables. Instead we start with a random noise distribution and learn a model that transforms this into our target sample space.

![[Pasted image 20220517161925.png]]

In a **generative adversarial network** we make a generative remodel by having two networks compete with each other. We have a *generator* that turns noise into a imitation of the data to trick the discriminator. The *discriminator* tries to identify real data from fakes created by the generator.

![[Pasted image 20220517162632.png]]

The *discriminator* will work to find flaws in the generated samples it can use to beat the generator. the *generator*  will the find ways to improve its generation to nullify the *discriminators* advantage. Over time they will get better and better until hopefully there is not distinguishing even for humans.

We need a loss function that specifies an objective called an **adversarial objective**. The loss function is as follows $$\underset D{\text{arg max}}E_{z,x}\left[\text{log}\hspace{3pt}D(G(z))+\text{log}\left(1+D(x)\right)\right]$$ We are trying to maximize the probability that our discriminator $D$ will have picked $x$ over $G(z)$.$$\underset G{\text{arg min}}E_{z,x}\left[\text{log}\hspace{3pt}D(G(z))+\text{log}\left(1+D(x)\right)\right]$$Out generator will do the inverse and try to minimize this loss. The loss is really a form of *cross entropy loss*. Since it cannot change $x$ its aim it to optimize $G(z)$. Overall we get a min-max objective as $$\text{arg }\underset{G}{\text{min }}\underset{D}{\text{max }}E_{z,x}\left[\text{log}\hspace{3pt}D(G(z))+\text{log}\left(1+D(x)\right)\right]$$

#### Generating new data with GANs
When we have a trained generator we take random noise to a target distribution. One point will lead to one outcome. We can *interpolate* between these random values and this will interpolate in the target space.

![[Pasted image 20220517165304.png]]

#### Progressive growing of GANs
One way to improve the performance of GANs is we start with low dimensional representations and slowly build up to larger representations over time. This means we start with larger features and improve over time.

![[Pasted image 20220517165557.png]]

We *iteratively* add more and more layers to improve the training. This speeds up training and improves overall stability.

Another improvement with this is style transfer in which we grow a network while allowing style transfer to take place in the different layers. This allows for.

![[Pasted image 20220517165927.png]]

#### Conditional GANs
Here we also add a label into the network. This way we can generate samples and also describe what kind of sample we want.

![[Pasted image 20220517170148.png]]

An example of this is **pared translation**. For one example we can pass in a segmentation map as $c$ then the network will try to discriminate against real and fake generated real scenes.

![[Pasted image 20220517170310.png]]

This can allow for translation in images from one to another.

![[Pasted image 20220517170418.png]]

#### Domain transformation with CycleGAN
Here we have two generators and two discriminators. We move and learn a mapping between the two.

![[Pasted image 20220517170637.png]]

The main idea here it that GANs are key is transferring between different distributions. Originally we went from *gaussian to a target data manifold* but now we are going from a *data manifold to another data manifold*. So this can move to many different domains.

![[Pasted image 20220517170949.png]]

