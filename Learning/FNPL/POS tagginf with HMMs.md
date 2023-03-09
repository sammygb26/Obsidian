For some definition we will use $\mathbb X=(x_1,x_2,\dots,x_{|x|})\in\mathcal X$ and our output sequence as $\mathbb y=(y_1,y_2,\dots,y_{|x|})$, $y_i\in\{1,\dots,N\}$. Generally word have different tags they can be but we need to disambiguate between them.

### Name Entity Recognition Note
Although sequence modeling is one way to approach this problem as previously in [[Part-of-Speech Tagging]] we labeled each word as which entity it belongs to. But instead we could label stats and ends of entities

![[Pasted image 20230302121754.png]]

This can capture extra detail as we can model the beginning tags differently this allows our model to be more flexible and powerful.

### Vision Gesture Recognition
In general sequence models can e used to recognize different task.

![[Pasted image 20230302121832.png]]

### Hidden Markov Models
**Decoding** is the case where we ask the sequence of states given the emissions (this comes form noisy channel model roots).

...

A simple example of a sequence being generated is

![[Pasted image 20230302122049.png]]

This is defined as a **generative process** but we don't use this model to generate.

##### 1st Order Hidden Markov Models
Generally a **graphical model** is used to represent our model. Different random variables are circles and arrows are conditional dependencies. So A -> B means B is conditionally independent given A. A 1-st order HMM can be described as

![[Pasted image 20230302122320.png]]

### Learning
When we are learning a HMM we want to learn the **transition** and **emission probabilities**. In the simplest case we will have a training corpus.

![[Pasted image 20230302122534.png]]

A simple way to find these is to use frequency estimation we can find the probabilities.

$$P(x^t=k\mid y^t=i)=b_{ik}=\frac{C_E(i,k)}{\sum_{k'}C_E(i,k')}$$

Then we apply **padding** to give start and stop tags.

### 1st order vs 2nd order
In a 2nd order HMM we have a trigram distribution over tags. Here last two states affect the current state.

![[Pasted image 20230302122845.png]]

### Decoding
Here instead of just using the model to get the probabilities of a sequence of states and emissions (set of random variables) we instead want the set of states given the emissions. We can use the [[Viterbi Algorithm]] to do this. The key things is for each state since we are looking for the most probably sequence we can ignore different sequences that reach the same state taking the most probable.

![[Pasted image 20230302123402.png]]

This table allows us to calculate the probability of each transition individually. Finally having multiple probabilities for possible words allows us to calculate exponentially many ways to reach  subsequent words but we just take the best as the other will never be chosen.

![[Pasted image 20230302123537.png]]

We store the best path along with its back pointing arrow. Eventually we reach the last word we can pick the best probability and trace back.

![[Pasted image 20230302123730.png]]

This gives a single path. This takes $O(M^2N)$ time for $M$ tags and $N$ words (emissions).

### 2nd order model
Here instead of storing single tags for each later we instead store we instead use pairs. But we only consider **consistent pairs**.

![[Pasted image 20230302124252.png]]

### Hidden Markov Models: decoding
In general we use log probabilities and sums instead of products. But we want work with a small part of the subgraph grouping the transition and emission probabilities together.

![[Pasted image 20230302124354.png]]

This allows us to generalize Viterbi into different steps

![[Pasted image 20230302124647.png]]

### What Else
Using Viterbi we can find the best tags. Once we have this we get a sentence probability and then use this as a language model. $P(x|\theta)$ where we are ignoring the tags. For this we want to calculate

![[Pasted image 20230302124904.png]]

But all the different $y$ values is exponential. We can apply a similar algorithm to Viterbi called the Forward algorithm.

![[Pasted image 20230302125052.png]]


### HMM Unsupervised Estimation
Here if we just have unlabeled data we may want to still tag them. The tags may be abstract and this way we are looking to cluster words by how they are used similarly. We want to learn

![[Pasted image 20230302125259.png]]

We can find best parameters given the state sequence (labeled examples). Then we can find tags given parameters using **Viterbi**. With this circularity we can use **expectation maximization**. In each iteration we will calculate **expected counts** (synthetic data) then we use these for the **maximization step**.

##### Expected Counts
Usually counts are just given by counts in our corpa where counts are given for sequences. With **expected counts** we compute probs for possible tag sequences, f sequence $y$ has probability $p$, we count $p$ for each possible sequence. We add up these fractional counts across all possible sequences.

But there is an exponential number of possible sequences...

![[Pasted image 20230302130017.png]]

[[Expectation Maximization]]