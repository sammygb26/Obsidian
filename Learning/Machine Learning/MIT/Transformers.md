# Transformers
This is a more modern neural network architecture built around **attention**. It has revolutionized the area of *natural language processing* however has begun to be applied to other areas aswell. The networks takes as input a sentence in the form of a sequence of *vectors* this is converted into a vector called an encoding, this is then decoded back into another sequence. 

The **attention** mechanism quantifies how important every token is for some given token. This allows for example the network to calculate for some token or word like "it" how important each other word is for a correct translation of "it" say in another language. By being able to focus on particular words before and after a word this network replaces the older RNN, LSTM and GRU network designs.

### Network Design
The network received as input a sequence/sentence. This is converted into two further sequences a sequence of *word vector embeddings* and a sequence of *positional encodings*. The *word embeddings* give each word a vector so that the network can process it and the *positional encoding* gives a vector describing the position of a word in the sequence. The **transformer** adds the two encodings together to create an encoding capturing the different tokens and their positions. All the tokens are passed through a sequence of encoders then a series of decoders. Unlike RNNs and LTSMs the whole sequence is fed into the network at once allowing for parallelization. The *encoders* break each encoding into a sequence of vectors called **encodings**. The *decoders* do the reverse converting the encodings back into a sequence of *probabilities* of different output words. This is then used to output a word using a SoftMax function. An **attention mechanism** is present in each encoder and decoder, this allows only relevant tokens to be used by the network while masking irrelevant tokens. These attention mechanisms are implemented in *parallel* as they must be evaluated many times.

![[Pasted image 20220619155729.png]]

### Positional Encoding in the TNN
Many networks use vector embedding to convert words to vectors which the NN can work with. There is a direct mapping from every work to a vector space.

![[Pasted image 20220619152919.png]]

But the context of a work matters to it's meaning. A *positional vector* made out of some sensible function is used so that relative positions of words can be seen.

![[Pasted image 20220619153205.png]]

### Attention Mechanism in the TNN
This is the most important part of the TNN; the **attention mechanism**. This tells the network which parts of the input vector the network should focus on when generating the output vector. The importance of this can be seen in translation where the *order might change* for example "la casa roja" compared to "the red house". The attention allows a decoder while generating output words to focus on relevant words or hidden states while discounting irrelevant information. For example when generating the first word the following attention may be seen.

![[Pasted image 20220619153704.png]]

In practice *three* different way to use *attention* are present in the TNN

1) **Encoder-decoder attention** -> This is as the above sample and allows the TNN to attend over the input sequence when generating the output sequence.
2) **Self-attention in the encoder** -> This allows an encoder to attend to all parts of the input.
3) **Self-attention in the decoder** -> Allows decoder to attend to all parts of its sequence.

All these mechanisms allow the model to  draw information form inputs and hiddens states at any other point in the sequence. Everything is automatically remembered while nothing useless is attended to. This can also be used to generate an **attention matrix** showing the attention vector between each input word in the source and output languages.

![[Pasted image 20220619154306.png]]

### Attention Formula in the TNN
*Attention* works like a fuzzy dictionary lookup. It takes a query and a set of key-value pairs. It return a weighted sum of the values by the similarity of their key to the query. This gives the most common attention formula the **scaled dot-product attention** 

$$
\text{Attention}(Q,K,V)=\text{softmax}(\frac{QK^T}{\sqrt d_k})V
$$

Here $Q$ is a vector of queries of dimension $d_k$, $K$ is a vector of keys  of dimension $d_k$ and finally $V$ is a vector of values of dimension $d_k$. Then $d_k$ itself is the size of the attention keys and is a *hyperparameter* chosen at design time. The **sources** for $Q$, $K$ and $V$ are different depending on where the attention mechanisms is used in the transformer.

### Calculating Attention in the TNN
We can consider an example with attention key size 3 ($d_k=3$) and the bellow values for the keys, values and query.

![[Pasted image 20220619160133.png]]

We can see the query is *identical* to the second key and therefore we want to return just the second values/second row of $V$. We calculate a matrix multiplication $QK^T$ giving a dot product over all keys to the query.

![[Pasted image 20220619160328.png]]

Now we calculate the scaled attention *logits*

![[Pasted image 20220619160355.png]]

We can then apply the *SoftMax* to obtain

![[Pasted image 20220619160619.png]]

Finally this vector can be left multiplies with the value matrix to give a weighted sum of the columns of the matrix.

![[Pasted image 20220619160705.png]]

So this just returns the second key as expected. Usually however it will be a weighted combination of many keys. In the TNN we either have *self attention* where $Q$, $K$ and $V$ all come from the same value or we have *encoder-decoder attention* where $Q$ is taken from the previous decoder layer and $K$ and $V$ come from the encoding layer.

### TNNs vs RNNs
RNNs have a fundamentally different design from transformers. RNNs keep a hidden state which is passed along as the network processes a network sequentially. However much if this information is lost over time an little useful information is retained. Therefore these networks perform poorly over long sequences. TNNs allow for the whole sequence to be processed at once allowing each output to draw from each input and hidden state. RNNs sequential nature makes them hard to parallelize with GPUs however TNNs do allow this allowing for performance gains.

### TNNs vs LSTMs
LSTMs are a special kind of RNN that were more successful due to their ability to maintain a longer lasting cell state. This was achieved by the use of gates which limited changes made to the cell state. Later *attention* mechanisms were used to further speed up LSTMs which are still slow due to their sequential nature. It was then discovered that only the attention mechanism was needed and instead inputs could be processed sequentially.