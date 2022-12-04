CycleGAN allows side by side example to lead to image generation via and **GAN loss** and a **cycle constraint loss**. This allows images from one set to be **translated** into another. This works in the absence of **paired training examples**. This is important as **few datasets exist** for image to image translation. 

* **CycleGAN** only works when we assume there is some underlying relationship between the two domains.
* It isn't completely unsupervised and exploits set level supervision.

The sets will be $X$ and $Y$ and we want a mapping $G:X\to Y$ such that we can **translate** and image from $X$ to $Y$. We want this new $\hat y=G(x)$ where $x\in X$ to be indistinguishable from images $y\in Y$. That is we want the distribution over $\hat y$ to be the same as $p_{data}(y)$ (his requires $G$ be **stochastic** [[GANs (Goodfellow et al)]]). Our **optimal** $G$ therefor translates the domain $X$ to the domain $\hat Y$ distributed identically to $Y$.

* This doesn't ensure $X$ and $\hat Y$ are paired in a **meaningful way**.

There are $\infty$ many mapping that will induce the same distribution in $\hat y$. To get around this problem and the problem of **mode collapse** the idea of the translation being **cycle consistent**. The classic example is translating from a language to another if the meaning is preserved the original sentence should be given by a translation into the other language and a translation back. That is $G$ and $F$ should be **inverses of each other** and both mappings should also be **bijections** (one to one correspondence). To account for this a **cycle consistency loss** is used to encourage $x\approx F(G(x))$ and $y\approx G(F(y))$.

![[Pasted image 20221120103755.png]]

### Formulation
We want to learn mapping functions between $X$ and $Y$ given training samples $\{x_i\}^N_{i=1}$ where $x_i\in X$ and $\{y_i\}_{i=1}^N$ where $y_i\in Y$. We would say $x\sim p_{data}(x)$ and $y\sim p_{data}(y)$. We have two mapping $G:X\to Y$ and $F:Y\to X$. There are also two **adversarial discriminators**, $D_X$ and $D_Y$. $D_X$ aims to tell apart images from $\{x\}$ and $\{F(y)\}$ while $D_Y$ aims to tell apart images $\{y\}$ and $\{G(x)\}$. The **objective function** contains two types of terms *adversarial losses* form matching distribution of generated and training images and **cycle consistency losses** to ensure $G$ and $F$ are inverses of each other.

##### Adversarial Loss
The adversarial losses have the form $$\mathcal L(G,D_y,X,Y)=\mathbb E_{y\sim p_{data}(y)}[\log D_Y(y)]+\mathbb E_{x\sim p_{data}(x)}[\log(1-D_Y(G(x)))]$$ as taken from [[GANs (Goodfellow et al)]].

##### Cycle Consistency Loss
Cycle consistency loss aims to make $x\approx F(G(x))$ and $y\approx G(F(y))$. Hence to do this we can take the L1 distance between $x$ and $F(G(x))$ to minimize the difference. That is $$\mathcal L_{cyc}(G,F)=\mathbb E_{x\sim p_{data}(x)}[||F(G(x))-x||_1]+\mathbb E_{y\sim p_{data}(y)}[||G(F(y))-y]$$
##### Full Loss
The full loss then becomes $$\mathcal L(G,F,D_X,D_Y)=\mathcal L_{GAN}(G,D_Y,X,Y)+\mathcal L_{GAN}(F,D_X,Y,X)+\lambda\mathcal L_{cyc}(G,F)$$ where $\lambda$ controls the relative importance of the two objectives. Then in optimization we aim to solve $$G^*,F^*=\arg\min_{G,F}\max_{D_X, D_Y} \mathcal L(G,F,D_X,D_Y)$$

### Implementation
For the **Generator** the images are first downsized using convolutions and then 6 **residual blocks** ([[Deep Residual Learning (Kaiming He et al)]]) and then upsizing using fractionally sided convolutions. This is for 128x128 images and for 256x256 images instead 9 residual blocks are used.

For the **Discriminator** 70x70 **PatchGANs** are used where we aim to tell if 70x70 overlapping patches are real or fake. This is good as it can work on **arbitrarily sized images**.

### Training Details