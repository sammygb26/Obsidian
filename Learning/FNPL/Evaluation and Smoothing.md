Trigrams may not always work better than bigrams if the extra context they add doesn't give real clues [[N-gram language models]]. There are two kinds of evaluation

**Extrinsic**: here we measure the performance eon a downstream application. Can plug and play different language models. Measure how well it performs a task. But this isn't available in many cases as switching model can be hard.

**Intrinsic**: design a measure that can test models independently. A measure that is inherent to current task. These take little time unlike *extrinsic*. One possible measure is accuracy, but for this to increase the perfect guess must be made. But there are many viable guesses (variability!) and our model can be right on all of these. We get an extreme probability distribution instead of a balanced distribution.

##### Entropy
**Entropy** is defined as $$H(X)=\sum_x-P(x)\log_2P(x)$$this is the same as expected information. This is high when there are is lots of mass between many values instead of concentrated in one. Entropy rises most with more evenly likely distributions. But it depends most on the number of distributions. We use entropy to measure how certain a model is. We want certainty.

Base two is used so that the number is equivalent to how many Y/N questions we need to ask on average to know the answer. To encode a sequence in entropy we need to examine all possible events and their likelihood.

The average number of bits needed to encode our random variable is always greater than the entropy of $X$.

##### Entropy in English
For humans entropy is only about 1.3, meaning on average given the preceding context a human would need only 1.3 y/n questions to guess well.

Our LM estimates the probability of word sequences but it should align with the expected / gold label values. We use **cross-entropy** to examine this 

![[Pasted image 20230127122845.png]]

This is always greater than entropy.

For $w_1,...w_n$ with large $n$ per-word cross entropy is approximated by

![[Pasted image 20230127122959.png]]

This is the average negative log prob our model assigned to each word in the sequence. As an example with Moby Dick cross entropy of the sentence "spend three years before the mast" is

![[Pasted image 20230127123149.png]]

With a unigram the model uncertainty is about 11 (5 more bits).

##### Data Compression
If we designed an optimal code based on our bigram model, we could encode the entire sentence with about $42$ bits. This is just the sum of the information in each decision (unaveraged entropy). With a unigram model this would be $11*7=77$.

##### Perplexity
LM performance is often reported as **perplexity** rather than cross-entropy. Perplexity is simply $2^{\text{cross-entropy}}$. This is the average branching factor at each decision point if our distributions were uniform. So in the case about we get $2^g=64$ perplexity.

### Interpreting these measures
How well these measures look depends a lot on our corpus. May mean the corpus is easy or the model is good. We have to compare on a common corpus. We have to measure these models against each other. We also need held out data to ensure we are testing our models performance on more realistic data it hasn't seen.

### Sparse Data
We still have a problem using MLE with bigrams or trigrams. Even assume our corpus is of representative quality. We will get zero counts and so any examples not appearing in the text will get infinite cross-entropy. So while training we also include smoothing to take care of these cases.

# Smoothing
There are two kinds of smoothing 1. hallucinate counts we don't see, 2. reassign count from what we have seen 3. back of to simpler models and incorporate their estimates. This is all to get over the floor of MLE.

### Add-One (Laplace) Smoothing
Here we just pretended we saw everything one more time than we did. We **hallucinate** counts for everything.

![[Pasted image 20230127123838.png]]

But this doesn't work as the probabilities wont sum to 1!

![[Pasted image 20230127123951.png]]

We have to add some $x$ to the bottom of the probability calculation. As we add 1 for every possible word we have to add the number of words $v$.

![[Pasted image 20230127124129.png]]

But this doesn't work due to **Zipf's** law we drown our the true probabilities with all the random words in our copus.

![[Pasted image 20230127124410.png]]

### Add-$\alpha$ (Lidstone) Smoothing
Another alternative to is **add-$\alpha$**. We now have a parameter we could use to

![[Pasted image 20230127124530.png]]

We use the development set to test this value.

### Good-Turing
This is a better option. Instead of changing the denominator, which can have big effect on frequent events. Good-Turing changes the numerator. We steal count from things we have seen to those we haven't seen.

![[Pasted image 20230127124718.png]]

We move all the probability mass totals down to the lower (less seen words.)

![[Pasted image 20230127124905.png]]

![[Pasted image 20230127124915.png]]

This takes into account the true distribution. This gets confusing! In general the  counts are given as

![[Pasted image 20230127125322.png]]

Note we time by $c$ and $c+1$ since we are artificial increasing the number of time these were achieved. We estimate the probability that the next observation is previously unseen.

![[Pasted image 20230127125723.png]]

Then we divide that probability equally amongst all unseen events

![[Pasted image 20230127125750.png]]

[[Evaluation and Smoothing Questions]]