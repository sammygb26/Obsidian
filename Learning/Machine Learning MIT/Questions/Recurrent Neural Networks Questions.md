What problem does recurrent neural networks solve? #flashcard #MachineLeanringMIT #RNNs
	Recement neural networks solve the problem of **sequential modeling**. This is where not just a single input matters but a sequence of inputs and or a sequence of outputs. For this out neural networks needs some idea of order and state.

---
What are the three types of sequential modeling and give an example for each? #flashcard #MachineLeanringMIT #RNNs 
	**Many to One** (example would be sentiment classification, sequence of letters to a single sentiment). **One to Many** here se start with a single value and get a sequence and example would be image captioning. **Many to Many** takes one sequence and generates a corresponding sequence and example would be **Machine Translation**.

---
What is the basic idea behind a RNN (Recurrent Neural Network)? #flashcard #MachineLeanringMIT #RNNs 
	The basic idea behind a recurrent neural network is we incorporate some state as an input to each network and as an output. This allows the network to filter and update some self state which can be used to incorporate information about the previous sequence. The state has a recurrence relation and depends on the input and the previous state $h_t=f_W(x_t,h_{t-1})$

---
What is embedding? #flashcard #MachineLeanringMIT #RNNs 
	When we pass something through a network is needs to be in vector form. So we need to encode any input value into a vector in someway.

---
What are two common ways to embed word for a neural network? #flashcard #MachineLeanringMIT #RNNs
	We can use **one-hot-encoding** where we use a $n$ vector for a domain of size $n$. Then each dimension of the vector represents some value. The embedding for that value is just the corresponding dimension for a word 1 and everything else 0. We can also use a **learned embedding** here another network takes our *one-hot* embedding and converts it to a lower dimension vector where similar words are grouped together.

---
What is used to train RNNs? #flashcard #MachineLeanringMIT #RNNs
	We can use gradient decent as before. Back propagation through time is used as any gradients for pervious networks in the recurrence will have their gradients chained to the future networks. But against this will just happen in the opposite order to our modeling.

---
What are the upsides of an RNN (Recurrent Neural Network)? #flashcard #MachineLeanringMIT #RNNs
	We ca perform modeling with **variable sequence lengths** as we can use each recurrent to encode a different element in the sequence.  We can model **long-term dependences** within out hidden state as information can be passed on. We can **capture differences in sequence order** as the continuously different hidden states allow us to combine order with out new value.

---
What are some problems with back-propagation through time? #flashcard #MachineLeanringMIT #RNNs
	Back-propagation through time can have  involve many factors over and over again for each network. If some gradient stays above one or bellow 1 we can get quickly exploding and vanishing gradients respectively. This can make is hard to learn with larger sequences.

---
What are some solutions to the vanishing gradient problem in RNNs? #flashcard #MachineLeanringMIT #RNNs
	Some solutions are using a ReLU activation function as the gradient is either 0 or 1 hence there can be no exploding values. We can initialize the weights to the identity matrix and biases to 0. We can also use gated cells that modulate the flow of information in specialized RNNs.

---
What is a LSTM (Long Short Term Memory) Network? #flashcard #MachineLeanringMIT #RNNs
	An LSTM is a type of RNN that contains two states, the hidden state and the cell state. It aims to elevate the problem of exploding gradient by avoiding changing many values in the state across cycles.

---
What are the fours stages to updating a LSTM explain them? #flashcard #MachineLeanringMIT #RNNs
	These are **forget**, we pass the cell state through a gate (controlled by $h_{t_1}$ and $x_t$ by ) to remove some values we no longer care about. We then **store** where we add some $i_t$ vector to our reduced $c_{t-1}$. $i_t$ is created by modulating and gating the hidden state. We will now **update** our cell state in one one path with the forget and store operations. Finally we **output** by updating our hidden state this takes a modulated values from our cell state and gates it against our working hidden state.

---
What are some problems with RNNs? #flashcard #MachineLeanringMIT #RNNs
	The sequential processing of data can be quite slow and this doesn't work well with modern GPU hardware as it cannot be parallelized. We also need to go through $t$ networks to train a sequence. The problem of vanishing and exploding gradients also makes long term dependencies hard to capture.

---
What is attention when it comes to deep learning? #flashcard #MachineLeanringMIT #RNNs
	Attention is used to overcome the limitations of RNNs the idea is to weight the different parts of our sequence which apply to each other allowing us to pick out the pieces of information we will need.

---
How does attention work in practice (self-attention)? #flashcard #MachineLeanringMIT #RNNs
	We use an attention mask. We encode values based on their position in the sequences aswell as their value. We then extract a query, key and value through our network from the original embedding. We then compute our attention weighting which are the differences between the query and value for each value. This gives an attention matrix  capturing how much different elements of the sequence relate to each other. Features with high weighting are extracted (we get their values).

---
