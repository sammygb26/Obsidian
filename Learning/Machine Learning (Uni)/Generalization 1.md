We have minimized a loss to allow us to *program with data* instead of actually generating a program. But how do we know the program is correct and what does correct mean? It definitely minimized the loss. How do we get to proof like with sorting. An example of a system failing to generalize comes bellow where the pattern is actual non-linear in the device we are trying to predict:

![[Pasted image 20221021151316.png]]

Another failure case comes when we fit high degree polynomials to the data bellow. Bit is it a failure as the data is "fit" better.

![[Pasted image 20221021151429.png]]

A program written with data is correct if it produces the intended results on unseen data. **Generalization** is defined as being (approximately) correct on unseen data (most of the time). The way this is measured is with some data set aside called test data (they do not overlap): 

![[Pasted image 20221021151647.png]]

There exists a common (unknown) distribution $\mathcal D$ where both the training data and test data are drawn from. But $\mathcal D$ is unknown hence why we need the network. The training set $S$ is independent samples from the distribution. The **training error** for a loss $l$ and a program $h$ is defined as: $$L_s(h)=\frac1n\sum_{i=1}^nl(y_i,h(x_i))$$ If we have a test set $S'$ (sampled form $\mathcal D$, then $L_{s'}(h)$ is the error on the test set (or test error) for program $h$. We don't care too much about the training loss but instead the loss on unseen data hence we want: $$L_{\mathcal D}(h)=\mathbb E_{(x,y)\sim\mathcal D}[l(y,h(x))]$$ Where this is the expectation of the loss where we sample $(x,y)$ where $x$ is a feature and $y$ is the ground truth sampled from $\mathcal D$. The test error $L_{S'}(h)$ of a program $h$ is an estimate of the generalization error $L_{\mathcal D}(h)$. Remember our goal in general is to find $h$ with a low $L_{\mathcal D}(h)$.

We need to think larger about multiple programs. A **learning algorithm** $A$ is $$A:(\mathcal X\times\mathcal Y)^m\to\mathcal H$$This is said as our algorithm takes in some set of all the possible $x$s matched with all the possible $y$s then we have $m$ of them and we want it to return some $h$ out of the set of all programs. A **hypothesis class** $\mathcal H$ is the set of possible programs of a particular form. For example a linear classifier is $$\mathcal H=\{x\mapsto w^T\phi(x):w\in\mathbb R\}$$

### Probably Approximately Correct Framework
A hypothesis class $\mathcal H$ is a PAC-learnable with learning algorithm $A$ if for any distribution $\mathcal D$, there exist $\epsilon>0$ and $0\le\delta\le1$ such that $$\mathbb P_{S\sim\mathcal D^m}\left[L_{\mathcal D}(A(S))-\min_{h'\in\mathcal H}L_{\mathcal D}(h')>\epsilon\right]<\delta$$Here $\min_{h'\in\mathcal H}L_{\mathcal D}(h')$ is the best possible dataset loss. Then $L_{\mathcal D}(A(S))$ is the dataset loss of the program given by $A$ trained on $S$. $S$ is what is random hence this says our probability the distance of our result from the best we can do is less than delta. So we are better than $\epsilon$ $\delta$ percent of the time.

![[Pasted image 20221024151519.png]]

### No Free Lunch Theorem
Suppose $|\mathcal X|=2m$. For any learning algorithm $A$, there is a distribution $\mathcal D$ and $f:\mathcal X\to{0,1}$ such that $L_{\mathcal D}(f)=0$, but$$\mathbb P_{S\sim\mathcal D^m}\left[L_{\mathcal D}(A(S))\ge\frac1{10}\right]\ge\frac1{10}$$That is the our loss being worse than $\frac 1{10}$ is at least $\frac1{10}$ (arbitrary constants). So this means any learning algorithm can be made to fail. Hence we should instead of comparing to $f$ compare to the best in the hypothesis class.

**Tradeoff between model complexity and generalization** - When we only compare $\mathcal H$ we are comparing against $\min_{h\in\mathcal H}L_{\mathcal D}(h)$. When $\mathcal H$ is large $\min_{h\in\mathcal H}L_{\mathcal D}(h)$ becomes smaller. When $\mathcal H$ is the universe we cannot learn (No free lunch). Hence $\mathcal H$ needs to be the right size or at least the range of $\mathcal A$ needs to be about right as in we cannot take an infinite number of steps in SGD.

explain graphs above

### Error Decomposition
![[Pasted image 20221021154743.png]]

**Approximation Error** - best you can do error (floor).
**Estimation Error** - distance form the best we can do.

That is there are two sources of error. The hypothesis class and the error in the actual program we find.

### Training
Since we only have a data set $S$, we can only minimize $L_S(h)$. Minimizing  $L_S(h)$ is called empirical risk minimization (ERM). If $h_{\text{ERM}}=\text{argmin}_{h\in\mathcal H}L_s(h)$ do we know anything about $L_{\mathcal D}(h_{ERM})$?

### Uniform Convergence Framework
We say that $\mathcal H$ has uniform convergence property if for any distribution $\mathcal D$, there exist $\epsilon>0$ and $0\le\delta\le1$ such that for every $h\in\mathcal H$ we have:

![[Pasted image 20221021155403.png]]

So the difference between the training and generalization error being over some values is very small. Uniform convergence assures that the training error and generalization error are not far form each other. This has to happen for all $h\in\mathcal H$, the uniform part (and a strong requirement).

![[Pasted image 20221024151817.png]]

If we have uniform convergence then we get: $$L_{\mathcal D}(h_{ERM})\le L_{S}(h_{ERM})+\epsilon$$But we also know by the definition of $h_{ERM}$ that $$L_S(h_{ERM})+\epsilon\le L_S(h)+\epsilon$$Which is for any $h\in\mathcal H$ (ERM). We can apply uniform convergence again to get $$L_{\mathcal D}(h_{ERM})\le L_{S}(h_{ERM})+\epsilon\le L_S(h)+\epsilon\le L_{\mathcal D}(h)+2\epsilon$$Remembering this is for any $h\in\mathcal H$ we can find that $$L_{\mathcal D}(h_{ERM})\le\min_{h'\in\mathcal H}L_{\mathcal D}(h')+2\epsilon$$With probability $\delta$. If $\mathcal H$ has unform convergence property then $\mathcal H$ is PAC-learnable with ERM.

[[Generalization 1 Questions]]