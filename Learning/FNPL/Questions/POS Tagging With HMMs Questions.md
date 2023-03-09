In the Name Entity Recognition problem what is another way of tagging other than giving all tokens in the same entity the same tag, what are the advantages? #flashcard #FNLP #POSHMMs
	One way is to tag the start of an entity differently than the intermediate elements. This gives the HMM recognizing the sequence more flexibility when it comes to capturing what words give the state of entity names and what don't.

---
How can gesture recognition be through of as a sequence modeling task?  #flashcard #FNLP #POSHMMs 
	The key thing with sequence modeling tasks is that the state in the previous time step informs us as to the possible states in the current time step. As gestures changes gradually overtime we can use previous gesture information to improve our estimates for current gesture pose even if we don't know the previous pose for certain.

---
What is decoding given a HMM?  #flashcard #FNLP #POSHMMs 
	In **Decoding** we attempt to find the sequence of hidden states given a sequence of emissions. The name decoding comes from the initial noisy channel use of these models.

---
How does the order of a Hidden Markov model affect its structure?  #flashcard #FNLP #POSHMMs 
	The HMM's order describes how many previous states a current state is given by. So a 1st order Markov Model has the current state dependent only on the previous state while a 2nd order MM has the current state conditioned on the previous two.

---
What is the learning task for HMMs?  #flashcard #FNLP #POSHMMs 
	In the learning task we are given some corpus and attempt to identity the $A$ (transition matrix) and $B$ (emission matrix) parameters.

---
How can we perform learning when we have a labeled dataset?  #flashcard #FNLP #POSHMMs 
	If we have a labeled dataset we can perform learning through maximal likelihood estimation. This is possible for the transition matrix as we know the true sequence of transitions. Then is possible for the emissions as we know for each emission the state that gave it.

---
