What are the basic inputs and outputs of a RNN? #flashcard #FNLP #RecurentNeuralLanguageProcessing
	In an RNN we have $h_{t-1}$ our current state. We take in this and $x_t$ our current input. We produce $h_t$ our next state and and optional output.

---
What are the operations in a basic RNN?  #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	In a basic RNN we are given $h_{t-1}$ and $x_t$ our output will be $h_t$ and this is found with the formula $$h_t=\tanh(h_{1-1}W_h+x_tW_x)$$

---
How is a multi-layer RNN constructed? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	A multi-layer RNN is made by taking the state of previous layer through another layer. We may block propagation of state in the lower levels. At that point it is equivalent to replacing the inner RNN function with a NN.

---
What is the need for bidirectional RNNs? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	This comes from a problem with training RNNs. Basically the error signal is multiplied by some value in each layer to get to the final layer. In the end the signal to the early layers is week and changes frequently making training hard. One way to cheese this is to train two RNNs one running forward and one backward. Each help with the others weakness although the center is still an issue.

---
How can language modeling be performed with RNNs? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	Here we need to calculate $p(y_t\mid y{<t})$ and we can use this get the likelihood of an entire sentence from the chain rule. So we can train a RNN to output some sentence embedding vector which we will then apply LR to get a probability distribution over next words.

---
How would we train an RNN language model? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	We train it on text to just recreate the text. We minimize the $-\log$ loss of the true word given the previous words. $$Loss=-\log(p(y_t\mid y_{<t})$$

---
What is the framework allowing RNNs to perform sequence to sequence modeling? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	The Encoder-Decoder framework is used. Here we take in an entered sentence with a given RNN to produce a hidden state. This can then be sent to a Decoder RNN which converts it to a new sentence.

---
What loss is trained for RNNs? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	We can train $-\log$ loss for the word we should generate next given the old sentence and previous words.

---
What is the problem with just taking the most likely token when generating language from an RNN? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	This is the equivalent of greedy search. The best result may be to take less likely words now unlocking better ones later.

---
How does beam search work? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	The idea here is we sort of keep $n$ greedy searches alive at once. Each iteration we take the $n$ most probably paths and explore $n$ node from then and take the $n$ most popular again.

---
What is the main problem with and encoder decoder framework? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	The main problem is the state between acts as a bottleneck. Limited amounts of information can pass through it.

---
What is the idea behind attention? #flashcard #FNLP #RecurentNeuralLanguageProcessing 
	The idea is we don't just use the state passed from encoder to decoder to compute our answer. We also take a weighted SoftMaxed attention value which highlights the most important words in the input given the current state of the network.

---
