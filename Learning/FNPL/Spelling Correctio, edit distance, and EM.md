When we are doing spelling correction we will perform an argmax over what was meant to be said.

![[Pasted image 20230202121826.png]]

But we can't argmax over all possible words / sequences of words as there are SO MANY possibilities.

### Algorithm sketch
A very basic correction scheme to get this working we can assume:

![[Pasted image 20230202121949.png]]

If we make these assumptions then we can do the following to correct each non-word $x_i$:

![[Pasted image 20230202122040.png]]

As we generate misspelled words we get $P(\vec x|\vec y)$ as the chance this mistake was made. We can then also multiply by $P(\vec y)$ (language model).

### Simple Nosie model
We suppose we have a corpus of **alignments** between actual and corrected spellings

![[Pasted image 20230202122228.png]]

The example has:

![[Pasted image 20230202122239.png]]

We assume that the types character $x_i$ depends only on indented character $y_i$. That is each mistake is independent. So $o\to e$ is equally probable regardless of whether the word is effort spoon etc. For each observed sequence $\vec x$, made p of a sequence of characters $x_1,... x_n$ we have

![[Pasted image 20230202122435.png]]

Hence

![[Pasted image 20230202122457.png]]

### Estimating the Probabilities
Using our corpus of alignments, we can easily estimate $P(x_i|y_i)$ for each character pair. Simple count how many times each character (including empty character for del/ins) was used in place of each other character. The table of these counts is called a **confusion matrix**. We then use MLE (or another technique).

![[Pasted image 20230202122703.png]]

We saw $G$ when the indented character was $C$ 36 times for example.

### Big Picture Again
We have a simple language model. We have trained it on a corpus (correct and misspelled. This gave the noise model. We then use argmax to  get the best probable sentence.

A problem is the size of the character aligned corpus. It can be very hard to get this assignment. We are more likely to have matched corrected and uncorrected examples. But we also hay have multiple errors which we assumed earlier.

### Alignment and Edit Distance
This can solve both problems above. We find the **optimal character alignment** between two words (the one of the fewest character changes: the **minimum edit distance** or MED)

![[Pasted image 20230202123127.png]]

Writing this as an alignment we can write

![[Pasted image 20230202123210.png]]

This is solved with **dynamic programming**. But there are more possible alignments (these are both the best)

![[Pasted image 20230202123323.png]]

There are also lots of **non-optimal alignments**

![[Pasted image 20230202123402.png]]

##### Could Brute Force

##### Dynamic Approach
Other algorithms like this (using **Memoization**) are Veterbi and CKY. The minimum distance $D(stall, table)$ bust be the minimum of

![[Pasted image 20230202123631.png]]

Similarly for the smaller subproblems. We solve the smallest subproblems first. Then we build up a chart and use this to find the best substitution.

**Costs** -

We write out the two words (this is assuming spaces are correct). Then any cell is going from all vertical labels at or above it to all horizontal labels at or behind it. So here (2,2) is $ST\to TA$. 

![[Pasted image 20230202124206.png]]

We keep back pointers to allow us to figure out the best path to align the strings. The direction you move in defines the error that was taken.

![[Pasted image 20230202124308.png]]

Overall this gives us:

![[Pasted image 20230202123821.png]]

##### MED Uses
This is used in many areas like DNA sequencing and morphological analysis given words and finding their origins.

Using MED algorithm we can now product the character alignments we need to estimate our error model, given only corrected words.

![[Pasted image 20230202124453.png]]

This then gives our confusion matrix and then error model.

### Catch-22
We used 1 and 2 as costs to compute alignments. But we need the costs to give optimal alignments. The costs are actually what we are trying to find in the first case. To solve this we use [[Expectation Maximization]]. Here we pick some initial value. Then we use this to get some alignment. This can be used to recompute better estimates for costs. This repeats until convergence.

### EM vs hard EM
This is known as **hard-EM** since we get out parameters straight out instead of estimating some posterior probability distribution. True EM is guaranteed to converge to a local optimum of **likelihood function** but hard EM can't even do this.

...

### Likelihood function
We call the parameters of our model $\theta$. So for our spelling error mode, $\theta$ is the set of all character probabilities $P(x_i\mid y_i)$. For any value of $\theta$, we can compute the probability of our dataset $P(data\mid\theta)$. This is the **likelihood**. If our data includes hand-annotated character alignments then $$P(data\mid \theta)=\prod_{i=1}^nP(x_i|y_i,a)$$If the alignments $a$ are latent, sum over possible alignments $$P(data\mid\theta)=\sum_a\prod_{i=1}^nP(x_i\mid y_i,a)$$

[[Spelling Correction, Edit Distance and EM Questions]]