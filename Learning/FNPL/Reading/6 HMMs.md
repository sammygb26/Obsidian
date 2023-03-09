HMM and MEMMs (Maximum Entropy Markov Models) are both **sequence classifiers**. These assign some class or unity to a item in a sequence.

### Markov Chains
This is also called an **observed Markov model**. This is related to a **weighted finite-state automata** where state transitions have probabilities. But instead of there being multiple state path for a given sequence there is only one path. This doesn't  work for any ambiguous input and so can only parse unambiguous data. It can be used to assign **probabilities** to these sequences. Here are some example for weather patterns and word sequences.

![[Pasted image 20230302140520.png]]

The word sequence mode is a **bigram model**. We can also think of these are **graphical models** with the following components:

![[Pasted image 20230302140735.png]]

The Markov assumption (1st order) means the previous state only depends on the current state.

![[Pasted image 20230302140908.png]]

As the elements of the matrix are probabilities we require

![[Pasted image 20230302141135.png]]

Instead of having a **start state** we can also have a distribution over states to start in as

![[Pasted image 20230302141242.png]]

An examples of his can be given as

![[Pasted image 20230302141503.png]]

### Hidden Markov Model
The **Markov chains** above work with known sequences. But instead we may want to analyze scenarios where the state is **hidden**. For example we estimate the weather based on the number of ice creams sold. HMMs are based on the components:

![[Pasted image 20230302142236.png]]

Again we can also use the $\pi$ notation to give initial states instead of having a start state.

![[Pasted image 20230302142339.png]]

With a 1st order HMM we use two simplifying assumptions. The Markov assumption:

![[Pasted image 20230302142425.png]]

Then the output independence assumption:

![[Pasted image 20230302142452.png]]

A HMM for ice cream and weather could be given as

![[Pasted image 20230302142530.png]]

Since there is always a non-zero probability of transitioning between two states this HMM is **fully connected** or **ergodic**.

For example is **left-to-right** (also called **Bakis**) HMMs, the state transition proceed form left to right. Here there will be no transition probabilities going from higher order number to lower order ones and so this HMM is not ergodic.

![[Pasted image 20230302142835.png]]

### Using HMMs
In general we can think of three problem HMMs can be used for

![[Pasted image 20230302142933.png]]

### Computing Likelihood: The Forward Algorithm
With a **Markov Chain** this is simple as we just multiply each transition sequence in order. Then for HMM this is more complicated as we need to find the state.

As a simpler case we can calculate the probability of a output sequence if we know the input probabilities. For example if we know the state is $hot\space hot\space cold$ then what is the probability of 3 1 3 (ice cream). Given the one-to-one mapping of states to observations we can calculate this as

![[Pasted image 20230302143353.png]]

Then for the above example this is given as

![[Pasted image 20230302143420.png]]

![[Pasted image 20230302143438.png]]

This isn't what we want be instead we can sum over all possible weather sequences along with the sequence and output probabilities. That is for a output sequence $O$ and state sequence $Q$ we want

![[Pasted image 20230302143550.png]]

We can sum out the $Q$s to give 

![[Pasted image 20230302143718.png]]

But this is impractical for large sequences as we have to go over the exponential number of possible sequences. Instead we use the **forward algorithm**. This is a [[Dynamic Programming]] algorithm that allows us to fold probability computations together to get a good result. These are folded into a **forward trellis**.

Each cell in the trellis $\alpha_t(j)$ represents the probability of being in state $j$ after seeing the first $t$ observations. This is the probability

![[Pasted image 20230302144140.png]]

We can calculate this as the sum over all possible extensions of all paths leading to this path. That will be 

![[Pasted image 20230302144314.png]]

At each step all we need are 

![[Pasted image 20230302144355.png]]

![[Pasted image 20230302144513.png]]

For more state we could get something like

![[Pasted image 20230302144731.png]]

The algorithm is given as

![[Pasted image 20230302144759.png]]

### Decoding: The Viterbi Algorithm
This is the task of finding the hidden states given a sequence.

![[Pasted image 20230302145013.png]]

We could calculate the probability of each combination as at the start of the previous section but again this will take exponential time. Instead the [[Viterbi Algorithm]] can be used. Here we can for each possible state after a given observation take the post probable sequence that would lead to there. This will be our trellis value giving

![[Pasted image 20230302145409.png]]

But we know the max probability for previous states given we have already calculated Viterbi for them. It doesn't matter that we aren't comparing non max states as once the have fallen behind they can never catch up to beat a now most probable sequences as each sequence has the same options going forward. Hence we can restate the above as

![[Pasted image 20230302145617.png]]

For each step all we need is

![[Pasted image 20230302145648.png]]

We also require back-pointers to give the sequence (unlike in the Forward Algorithm)

![[Pasted image 20230302145800.png]]

### Training HMMs: The Forward-Backward Algorithm
Here given a number of sequences of observations we want the HMM parameters $A$ (transition probs) and $B$ (emission probs). We will give a sequence of observations $O$ and a vocabulary of potential hidden states $Q$. For this the **forward-backward** or **Baum-Welch** algorithm is used this is a special case of an [[Expectation Maximization]] algorithm.

We can start with **Markov chains**. We observe the hidden states so we know for each state how likely it is to transition to a following state. That is 

![[Pasted image 20230302150947.png]]

We cannot see the counts with a **HMM** but we instead can *iteratively* estimate the counts. We first derive probabilities in $A$ and $B$ and use these to generate better counts giving better $A$ and $B$ and so on.

To help worth this we will define  a probability related to the forward probability called the **backward probability**. This is called $\beta$ and is defined as the probability of seeing the observations form the time $t+1$ to the end, given the we are instate $i$ at time $t$. This is given as

![[Pasted image 20230302152654.png]]

Again similarly to the **forward algorithm** this can be calculated inductively with: 

1. **Initialization** - Here the $a_{i,F}$ are the terminating probabilities. ![[Pasted image 20230302152810.png]]
2. **Recursion** - Here the probability of the observations from $t+1$ to the end is the probability of that emission ($b_j(o_{t+1})$) summed for each state $j$ along with the probability of going to that state and that the rest of the sequence follows from that state $\beta_{j+1}(j)$. ![[Pasted image 20230302152819.png]]
3. **Termination** - finally we bottom out to the start states and get the probability of the entire sequence. ![[Pasted image 20230302152832.png]]

This can be illustrated as:

![[Pasted image 20230302153646.png]]

##### In Full
First we node we will estimate $\hat a_{ij}$ as 

![[Pasted image 20230302153757.png]]

One way we could attempt to find the numerator is the consider the probability at a time $t$ that the transition $i\to j$ is made. Then sum this up for all times would give our probability. We define the probability $\xi_t$ as the probability of being in state $i$ at time $t$ and state $j$ at time $t+1$, given the observation sequence and the model.

![[Pasted image 20230302155627.png]]

A similar probability must first be computed where we don't condition on $O$. That is

![[Pasted image 20230302155725.png]]

The different parts of this probability are given as:

![[Pasted image 20230302155819.png]]

One we have *not-quite-$\xi_t(i,j)$* we can compute $\xi_t(i,j)$ with some simple probability rules

![[Pasted image 20230302160041.png]]

Then $$P(O\mid\lambda)=\alpha_T(N)=\beta_T(1)=\sum_{j=1}^N\alpha_t(j)\beta_t(j)$$That is it can be computed many ways. Finally we can get

![[Pasted image 20230302160247.png]]

Then to get the expected number of transitions from $i\to j$ we sum over all $t$. Finally we we also need this summed over all states possible $j$ to give the denominator. This gives

![[Pasted image 20230302160532.png]]

##### Emission Probabilities
We also need the emission probabilities. This is given by

![[Pasted image 20230302160704.png]]

For this we need the probability of being in state $j$ at time $t$ which we will called $\gamma_t(j)$ this is given by:

![[Pasted image 20230302160745.png]]

We will compute the final value therefore as

![[Pasted image 20230302160842.png]]

The states required look like

![[Pasted image 20230302160912.png]]

This can be calculated using the forward and backward probabilities from $s_j$ as

![[Pasted image 20230302161232.png]]

Now for the numerator we sum $\gamma_t(j)$ for every time step where $v_k$ is observed and for the denominator we sum over all time steps. This gives

![[Pasted image 20230302161447.png]]

This gives our final iterative algorithm where $A$ and $B$ are initialized to some value as

![[Pasted image 20230302161652.png]]

The **expectation step** here is calculating $\xi$ and $\gamma$ then the **maximization step** is re-calculating $A$ and $B$. Generally this initial state plays a key role in the final output and for this reason special care may be taken to set it.