These get past the limitations of regular NNs and allow variable sequence length input to have their structure not destroyed.

![[Pasted image 20230405130110.png]]

So the RNN cell takes in a $h_t$ state vector and a $x_t$ input vector and produces the next state $h_{t+1}$.

### Vanilla RNN Cell
A simple version of this takes in a input state vector $h_t$ then we times this by a weight matrices. We then have two vectors of the same size. We add these together and then pass through a **nonlinearity**. In this case $\tanh$.

![[Pasted image 20230405130332.png]]

We want out final hidden representation to capture the meaning of the sequence we inputted into the RNN.

We can also make multi-layer RNNs stacking RNNs together and we would read an input from the layer below.

![[Pasted image 20230405130828.png]]

A problem with this is the learning signal will vanish as we get towards the start of the network. It will only learn recent parts.

### Bidirectional RNN
This attempts to get around the limitations of RNNs by having one the capture the beginning and one for the end. But of course this doesn't capture the middle. The output vector will then be sent to a text classifier.

![[Pasted image 20230405131112.png]]

## Language Modeling
A language model wants to assign probabilities to sequences of words $y_1\dots y_n$. We use the chain rule to expand this probability

$$p(y_1,y_2\dots y_n)=p(y_1)p(y_2\mid y_1)\dots p(y_n\mid y_1\dots y_{n-1})$$

All we need is to generate $p(y_t\mid y_{<t})$. A neural network can solve this problem if we think of the problem as classifying next word given previous context.

### High-Level Intuition for LM
One way to do this is have a NN that computes a representation for the prefix. We then compare this to output word embeddings to get a distribution over our vocabulary. Finally this is SoftMaxed to give a probability distribution.

### RNN Language Model
So we use the state vector as outputting the word and giving a distribution. 

![[Pasted image 20230405132204.png]]


And again we can stack these together.

![[Pasted image 20230405132217.png]]

### Training the language model
Training is done very much in the same way as we train a classifier. We take the $-\log$ loss of the probabilities of the true data given the prefix. We compare this output distribution to our target distribution with a one-hot encoding of our main word. 

![[Pasted image 20230405132537.png]]

## Sequence-to-Sequence Modeling
Here we want to move from a initial sequence to another sequence. The goal here is to find the most probable sequence in English given a Russian sentence for example. We need to *define this probability* model and how do we *learn* this model and finally how do we *search* to get our output sequence.

### Encoder-decoder frame work
**Encoder** - This reads source sequence and produces its representation
**Decoder** user source representation from the encoder to generate the target sequence.

![[Pasted image 20230405133627.png]]

Our language model changes little with a condition on the  new sentence. We just have a preset for the initial state.

In action we will generate the embedding then pass it to the encoder which processes it and generate the corresponding text.

![[Pasted image 20230405133823.png]]

### Simples RNN-based model
The simples model we just replace the initial state for the decoder with the output of the encoder. These will both use different parameters.

![[Pasted image 20230405133845.png]]

### Training
How we train on a source sentence and a prefix. We then train a distribution over the next word.

![[Pasted image 20230405134148.png]]
### Inference (aka Decoding)
Now we have a trained model we want to decode and find the best sentence for some input one. We can only enumerate everything as ML makes no independence assumptions. The simples idea is to take a greedy approach and take the most probable word at each step.

### Beam Search
This is a better than greedy approach where we keep the best $k$ outputs each time. $k$ is known as the beam size. Then out of the exponentially many we only keep two options. We basically perform $k$ searches at once. A problem here is we may get very similar texts so instead we can *sample* to get more diverse outputs.

### Key Problem with this Approach
A problem with this model is the entire representation is compressed into a single vector. There is a **bottleneck**.This is bad for the space of all sentences but we may want to translate entire documents and 

### Attention
![[Pasted image 20230405135403.png]]Attention was first applied to RNN encoders. But not **transformers** are used which only perform attention.

[[Recurrent Neural Language Processing Questions]]
