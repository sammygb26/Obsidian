Language is a sequential phenomena, its communication always taking in tokens over time. May modeling techniques use this method but just using feedforward NNs limits their use to fixed windows sizes. **RNNs** (and their sub derivatives like LSTMs)  deal with the problem of sequential modeling by having a **recurrent connections** which can also be seen as a state.

## Recurrent Neural Networks
A RNN is any network that contains a cycle within its connections, meaning that the value of some unit is directly or indirectly dependent on its own earlier output as an input. 

![[Pasted image 20230427140458.png]]

In general the network takes in an input $x_t$ and this is multiplied by a weight matrix and passed through a non-linear activation function to compute the value for a layer of hidden units $h_t$. This hidden layer is then used to calculate a corresponding output $y_t$. The $h_{t-1}$ is combined with $x_t$ to make the new $h_t$.

![[Pasted image 20230427141213.png]]

The equations for this are $$\mathbf h_t=g(\mathbf U\mathbf h_{t-1}+\mathbf W\mathbf x_t)$$ $$\mathbf y_t=f(\mathbf V\mathbf h_t)$$We can see that this network when **unrolled** is really just a feedforward NN with shared weights matrices across the times steps. It evaluation over a sequence can be seen as.

![[Pasted image 20230427141830.png]]

When unrolled the transformations look like this

![[Pasted image 20230427141907.png]]

#### Training
**Backpropagation through time** is used to train the different weight matrices. The basic idea is that we take two steps to calculate the losses. 1st we make a **forward pass** which calculates the final output but saves the hidden state along the way. 2nd we make a **backward pass**. Where the previous hidden values where tells us the gradient at the previous time. This can be combined with the the error gradient which tells us how much changing some hidden state would change the loss. This gradient can be used to get the gradient on the different elements of the RNN.

## RNNs as Language Models
Previously we have used n-grams to create language models. These uses n-gram probabilities of the form $p(w_i\mid w_{i-N:i-1})$ aswell as the independence assumption that $$P(w_i\mid w_{0:i-1})=\prod_{j=1}^iP(w_j\mid w_{j-N:j-1})$$But instead of making this assumption **RNN language models** take in a previous word and use it to update the hidden state, this hidden state is then used to give a probability distribution over all words. In theory the *hidden state* can capture information that completely summarizes the previous words allowing for estimation of $P(w_i\mid w_{0:i})$ directly.

![[Pasted image 20230427144255.png]]

#### Forward Inference in an RNN language model
So one way this could be done is construct an RNN that takes $\mathbf x_i$ as an input 1-hot encoding of a word. Then multiply this by our embedding matrix $\mathbf E$ that coverts $\mathbf x_i$ values into word embedding by extracting a single column of $\mathbf E$. This can then be added onto a transformed version of the previous state $\mathbf h_{t-1}$ to give $\mathbf h_t$. Then $\mathbf y_t$ can be the output distribution over  possible word values. We can get this by transforming the hidden state and then applying a *SoftMax* to it. This can all be summarized as $$\mathbf e_t=\mathbf E\mathbf x_t\hspace{32pt}\mathbf h_t=g(\mathbf U\mathbf h_{t-1}+\mathbf W\mathbf e_t)$$ $$\mathbf y_t=\text{softmax}(\mathbf V\mathbf h_t)$$The $\mathbf y_t[i]$ value will be $P(w_{t+1}\mid w_{1:t})$. So we can get the probability of the entire sentence as $$P(w_{w:n})=\prod_{i=1}^nP(w_i\mid w_{1:i-1})=\prod_{i=1}^n\mathbf y_i[w_i]$$
#### Training an RNN Language model
We can use **self-supervision** to train our model. Essentially the gold labels for any sequence of words is the next sequence. So we can simply train the model to minimize its error in predicting the correct word at each timestep.

We can use the **cross entropy** loss which is minimized when our model perfectly predicts the gold distribution. In this case though the gold distribution is given by a one-hot encoding of the next word. Therefore the cross entropy will just be the $-\log{\hat{\mathbf y}}_t[w_{t+1}]$ at each timestep. If we take the average of this to be our true loss then it can be written as $$\mathcal L=-\frac1T\sum_{t=1}^T\log(\hat{\mathbf y}_t[w_{t+1}])$$A drawing of the whole process can be seen as

![[Pasted image 20230427150141.png]]

So at each step we use the models prediction to get the loss then **ignore it**.

#### Weight Tying
This is a method to **reduce the number of parameters** in a model. The basic idea is that the $\mathbf E$ and $\mathbf V$ matrices are quite similar. Being the embedding matrix $d_h\times|V|$ and the almost **unembedding matrix** which take the hidden state and converts it to a distribution over all words. That is $|V|\times d_h$. 

In **weight Tying** we use the same matrix for both and simply transpose $\mathbf E$ to get $\mathbf V$ and so reduce the number of parameters massively. That is $$\mathbf e_t=\mathbf E\mathbf x_t\hspace{32pt}\mathbf h_t=g(\mathbf U\mathbf h_{t-1}+\mathbf W\mathbf e_t)$$$$\mathbf y_t=\text{softmax}(\mathbf E^T\mathbf h_t)$$

## RNNs for other NLP tasks
We can now look at how to apply the RNN architecture to different NLP tasks.

#### Sequence Labeling
Here we want to apply some label to each element of the sequence for example POS tagging or entity recognition. In the RNN approach a SoftMax layer will give the probability of each tag for element $t$ as $\mathbf y_t$. 

![[Pasted image 20230427151444.png]]

We will have to compare this to **gold labels** which give a single definite pos tag. But in these cases we simply use the **cross entropy loss** again.

#### RNNs for Sequence Classification
Here we classify an entire sequence rather than the tokens within. Here the clearest way is to see the entire network unrolling it. The hidden layer are each step $\mathbf h_t$ should be a representation of the entire sequence up to time $t$. We pass this $\mathbf h_n$ to a feedforward network that chooses a class via a SoftMax over the possible classes.

![[Pasted image 20230427151937.png]]

Another option rather than using just the last hidden function is to use a **pooling function**. This way we combine all hidden states together into one. For example $$\mathbf h_{mean}-\frac1n\sum_{i=1}^n\mathbf h_i$$
#### Generator with RNN-Based Language Models
The idea of a generator of text can be seen when we sample from the distribution of words a **language model RNN** creates and then add the sampled word to our sequence and use it to generate the next word and so on. This kind of generation state with $<s>$ tag and the continues until $</s>$ is generated. This technique is called **autoregressive generation** (although this is technically false if there are non-linearities).

![[Pasted image 20230427153137.png]]

## Stacked and Bidirectional RNNs
There are many ways to combine RNNs as they as basically simple recurrent units.

#### Stacked RNNs
We previously used only word inputs as the input into our RNN but we can also use the output of another RNN. In **stacked RNNs** there are multiple networks where the output of one layer serves the input to the next layer.

![[Pasted image 20230427153419.png]]

This seems to work by creating a series of **layer of abstraction** that lead to different level of understand at each layer.

#### Bidirectional RNNs
RNNs generally work with time taking in input in the same order time passes. But if we have an entire sequence there is no reason we cannot do this the other way. The **forward-RNN** can be taken to generate $\mathbf h_t^f$ as $$\mathbf h_t^f=RNN_{forward}(\mathbf x_1,\dots,\mathbf x_t)$$Then we have a **backward-RNN** which takes inputs in the reverse order and sums inputs to the right of the last input $t$.$$\mathbf h_t^b=RNN_{backward}(\mathbf x_t,\dots,\mathbf x_n)$$In a **bidirectional RNN** the output is a *concatenation of these two inputs* that is $$\mathbf h_t=[\mathbf h_t^f;\mathbf h_t^b]$$

![[Pasted image 20230427154355.png]]

This is quite useful for **sequence labeling** since instead of using a final hidden state (which will be biased towards details in the end of the sequence) we instead use the bidirectional output. 