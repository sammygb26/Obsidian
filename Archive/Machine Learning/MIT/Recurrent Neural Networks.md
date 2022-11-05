# Recurrent Neural Networks
We will now move past simple feed forward neural networks to an approach capable of sequential modeling. The idea can be signified by the idea of predicting where a ball will be. We cannot predict form a still image but with more images we can get an idea. This is the core of **sequential modeling**. This can work for many systems like *audio* (into soundwaves), *text* (into sentences or words)these can all be labeled with time slices. Sequence can as you can see model many things that have some component of order to them.

In *feedforward networks* (covered in [[Machine Learning/MIT/Introduction]]) static data went to more static data there is no idea of time or change only **FROM** --> **TO**. With sequence modeling we add networks that can take in not only input but time as well so we can add a wider variety of relations that can be captured.

![[Pasted image 20220305030800.png]]

So *one-to-one* was seen before for binary classification or image interpretation. *Many-to-one* can also be done for example taking a sentence and predicting a sentiment value for it, there is an indeterminate amount of input stamps but a single output. Then we have the converse *one-to-many* an example of this is image-captioning where from a single static image w create a number of words in order. Then we have *many-to-many* best seen in language translation (from sequence to sequence). So *many* means a sequence and *one* means a value (vector).

## Neurons with Recurrence
We need to make changes to our *perceptron* to allow it to include *recurrence*. If we think about our basic feed forward network. We have a layer of perceptron taking our $m$ dimensional input to $n$ dimensional output. We could just for the sequence take search piece of the sequence and apply the network function replicated over and over again.

![[Pasted image 20220305031830.png]]

But we know we are using *sequential data* so the output for $\hat y_2$ for example will depend on $x_0$ and $x_1$. This is missed as the function we are capturing cannot be more than $\hat y=f(x)$. We want to be able to pass information on and take this into our function for $\hat y$. We add $h_t$ that is a state to our network.

![[Pasted image 20220305032438.png]]

So the output depend on the current input. So our function will become $\hat y_t=f(x_t,h_{t-1})$. So our output depends on the current input and past memory. This gives a recurrence relation hence the name *recurrence* which can either be though of as moving through time right or a loop left.

## Recurrent Neural Networks (RNNs)
We apply a *recurrence relation* at every time state to process a sequence. This is given by a function with weights $W$ taking in our current input $x_t$ and our prior state $h_{t-1}$. So 
$$
h_t=f_W(x_t,h_{t-1})
$$
We are again learning the weights $W$ in out learning process. We use the same function with the same weights on every layer of our process. The *RNN* network both updates for a new $h$ but also a new $y$. In the real workings we have two weight matrices, one for updating $h_{t-1}$ and $x_t$ then non-linearly transformed to $h_t$ then one from $h_t$ to $\hat y_t$.

![[Pasted image 20220305033557.png]]

So form this we can get a whole weight matrix diagram showing how the evolution takes place taking in input $x_t$ along to our final $\hat y$.

![[Pasted image 20220305033905.png]]

For each calculated $y$ we find a loss. The sum of this loss it what is used in the end to train the **RNN**. We run a pass on a value by calculating a new $h$ and returning a $y$.

## Design Criteria
When we are trying to model sequences we need to 
1. Handel *variable-length* sequences
2. Track *long-term* dependencies, things in the past affected long in the future
3. Maintain information about *order*
4. *Sharing parameter* across the sequences allows to meet the first two requirements

*RNNs* meet all this design criteria.

## Problem: Predict the Next Word
We are given a series of words in a sentence and we have to predict the most likely next work in a sentence.

![[Pasted image 20220305140921.png]]

### Embedding
Before we train our model we need to understand how to represent our words in a *RNN*. The problem is a *neural network* simply take in vectors and apply a function giving a new array.

![[Pasted image 20220305141042.png]]

So we need to transform our data into a vector representation. We will use *embedding*. Here we transform indices into a vector of fixed size. But how might we do this. We want to map any work to a fixed size vector. We start with a vocabulary and map each work to a unique index we then map this to a vector. One way would be to make a vector the length of our vocabulary then each word is represented by one row in the vector. This is called a *one-hot* embedding. Another way is to learn the imbedding. The way we do this is we apply another neural network to convert the *one-hot* to a lower dimensional form. The model is trained so that words that are similar encoded closer together in the lower dimensional space.

![[Pasted image 20220305141508.png]]

### Variable Sequence lengths
We need to be able to handle *variable-length sequences* as stated above. We can have sequences where the information needed is far away or very close. *Feed-forward* neural networks can't handle this since the input is a fixed size. We can do this since we can just keep inputting new words or elements in the sequence.

### Model Long-Term Dependencies
We need to be able to remember *long-term dependencies*, *RNNs* can do this using their internal state using the recurrence relation and so information can be maintained.

### Capture Differences in Sequence Order
We also need to be able to understand how the *order* changes the meaning not just what is encoded.

![[Pasted image 20220305142050.png]]

So these sentences have the same words in the same orders but opposite meanings. We can accomplish this with *RNNs* as each time step is processed by the same weights and so order this are encoded in will change what the state is when later words are encoded.

And so we can with *RNNs* meet the sequence modeling criteria.

## Training RNNs
We use *backpropagation through time* (BPTT). The way basic *BP* work is we feed forward our input through the network then we compare this to a loss and take the derivative (gradient) of the loss with respect to each weight parameter. This gives us a direction to move each weight by a small amount.

![[Pasted image 20220305142645.png]]

In *RNNs* we make a forward pass by running the network many times over a sequence. We then calculate a loss for each step and sum them together. 

![[Pasted image 20220305142819.png]]

The propagation happens through each instance of the *RNN* but also through each time step going backwards through time hence the name *backpropagation through time*.

![[Pasted image 20220305143234.png]]

When we are calculating the gradients with respect to the state of the RNN $h_0$ involves *many-factors* of $W_{hh}$ and repeated computation of the gradients. Hence if the weight is continually greater than 1 our gradients can *explode* where gradients becomes extremely large (we can do gradient clipping by scaling back large gradients). Another problem is when our gradient values are smaller than 1 hence we get *vanishing gradients*. 

## Vanishing Gradient Solutions
We will look at 3 ways to solve this by cleverly choosing our activation function, my smart choice of weight initialization and then by changing the architecture. But why are they a problem. If we keep multiplying a small number by another smaller number (smaller than 1) this will cause the product to get smaller and smaller. This will cause errors the further back in time we go hence if can cause errors with taking gradients for relationships that are far back in time.

![[Pasted image 20220305145411.png]]

Standard *RNNs* struggle with longer term reasoning. But how can we get around this.

### Activation Functions
We can select a activation function like *ReLU* where the derivative is 1 for all values greater than 1.

![[Pasted image 20220305145651.png]]

This means our gradients are determined by the weights and not so much by the portion of the activation function it usually relates to.

### Parameter Initialization
We can initialize the *weights* to the identify matrix and *biases* to 0. This helps prevent the weights from shrinking to 0.

### Gated Cells
We have a more *complex recurrent unit with gates* to control what information is passed through. We will look at a type called a *Long Short Term Memory (LSTMs)*. Network built with these are better suited to maintaining information over longer times.

## Long Short Term Memory (LSTM) Networks
These are the main sequence modeling networks for deep learning. Lets first look at the general structure of an *RNN*.

![[Pasted image 20220305150210.png]]

So we are built up as a repeating instance over time. We show what is taken in given out and a state change. The black lines are matrix representations and the yellow box is a *non-linear* activation function. So above there is a single layered neural network with a single *tanh* activated layer. *LSTMs* have the same repeating structure but the insides are more complicated.

![[Pasted image 20220305150443.png]]

The recurrent unit has multiple layers (defined by non-linear activations and matrix multiplications). The layers control the flow of information through time and track information through timesteps.

The key idea is the *gate*. Information can be added or removed selectively. 

![[Pasted image 20220305151238.png]]

The gates consist of a sigmoid neural net layer and a point wise multiplication. Hence is capture how much information can be let through. There are four parts to how *LSTMs* capture data.

**LSTMs** capture information in two state one is $h$ which can be transformed to out output same as before so can be though of as the exact thought that would have given way to the last output. We also maintain $c$ the cell state which can be thought of as a wholistic description of what has been seen so far.

### Forget
They need to forget irrelevant information form the previous state.. They *gate* modulates how much information gets in and is passed on. This is controlled by the output from the previous node.

![[Pasted image 20220305151703.png]]

### Store
The also need to store relevant information for this the previous state is combined compared to itself using a *gate* this is then added to the current cell state.

![[Pasted image 20220305151743.png]]

### Update
The *LSTM* also has to update its current cell state from the previous one. It is selectively updated by the gat operations based on what the previous hidden state.

![[Pasted image 20220305152052.png]]

### Output
We need to decide what information form the cell state is outputted in a given state. It is gated by an operation on our hidden state.

![[Pasted image 20220305152441.png]]

This part controls what is outputted din $y_t$ and also what is passed on in $h_t$. 

The key idea is that **LSTMs** can regulate and control information flow through them. This also helps with the vanishing gradient problem. The way this is done is where we have $c_t$ where the gradient flow is uninterrupted over time. Hence the vanishing gradient doesn't matter as much as our

![[Pasted image 20220305152810.png]]

So in **LSTMs** a *separate cells state* is maintained from what is outputted. *Gates* are used to control the *flow of information* (forget, store, update, output). Then backpropagation through time with *uninterrupted gradient flow* is achieved through the use of a *sperate cells state* and so allows more efficient and effective training. This is what makes **LSTMs** the main workhorse of modern deep learning.

## RNN Applications
This is how *RNNs* can be used in the real world. One of them is *music generation*. Here we take in a sequence of musical notes and we output the next character in a song. We can also use this to generate completely new music by seeding a *RNN* with a note then feeding this plus the output back through the network to get another note and so on.

![[Pasted image 20220305154800.png]]

Another example will be *sentiment classification*. Here we take in a sequence of letters and output an emotion or sentiment. This is like classification in a basic feed forward neural network however there is a variable length input sequence.

![[Pasted image 20220305154842.png]]

Another example is *machine translation*. This is how for example *google-translate* works. We input a sentence in one language then we want an output in another language.


![[Pasted image 20220305155002.png]]

Here the language is encoded into a *state vector* then we use a decoder that converts this to a different language sentence. There are some issues with this fore example we have an *encoding bottleneck* that goes from the encoder to the decoder. We need to condense out input into the network which can loose a lot of the meaning.  These *RNNs* are also quite slow as they need sequential processing of the data. This means they don't work well on modern GPU hardware since they are hard to parallelize. Then also to train the *RNN* we need to go from the decoded output all the way back to the input here we need t go through order $t$ networks to train. But this is more costly the larger the networks we are training will be. There is also no long term memory, *RNNs* have vanishing gradients, *LSTMs* work better but still not perfect.

## Attention
So overcome these problems a method called *attention* was devised. They way this works is the decoder component doesn't just have the single *state vector* to make the output but has access to every previous output form the *RNN* layers.

![[Pasted image 20220305155656.png]]

The network they weights and combines these different outputs and this is learned. The attention learn what from the input is important. This is more efficient as it doesn't pay the same amount of *attention* to every single state. This is more efficient as only a single pass through the attention layer is needed instead of backpropagation through time as it is learning to access memory in an efficient way.

## Attention in Practice
Attention is done through an *attention mask*. We can think about a search where we have a query then every result has a key. We measure the similarity to the key to decide on how much attention to pay to a given piece of information. We then extract value based on the information we are now paying attention to. This is analogous to how *self-attention* works in practice.

The way this works in *self-attention* is we encode our values based on *position*. This is as since using attention we are trying to eliminate recurrence to get rid of its limitations but we still need to incorporate order in some way that previously came form the recurrence. We then extract our *query, key, value* for search, this is done by a linear matrix multiplication for each. We then *compute attention weighting*. As these are vectors we can compute the similarity between the key and query based on a dot product. We can also do this with a matrix giving a similarity matrix capturing the difference between the query and key matrices. We finally apply a SoftMax to get the values between 0 and 1.

![[Pasted image 20220513162047.png]]

We can then see in a heatmap the relationships between the words. so tossed and ball are related. We finally use this matrix to *extract feature with high weighting*. We can just multiply our value matrix through our attention matrix to finally get an output matrix of features we care about (high attention). In steps this is

1. Encode *position* information
2. Extract *query*, *key*, *value* for search
3. Compute *attention weighting*
4. Extract *features with high attention*

![[Pasted image 20220513162424.png]]

Transformer networks are most famous in language processing. 

[[Recurrent Neural Networks Questions]]
