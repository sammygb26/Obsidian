This is used instead of [[TF-IDF- Weighing terms in the vector]] for *term-term-matrices*, when the vector dimension correspond to words rather than documents. The idea here is to ask how much **more** two word co-occur in our corpus that we would expect by chance. **Pointwise mutual information** defines how often two event $x$ and $y$ occur compared with what we would expect if they were independent. $$I(x,y)=\log_2\frac{P(x,y)}{P(x)P(y)}$$The PMI between a target word $w$ and a context word $c$ is defined as $$PMI(w,c)=\log_2\frac{P(w,c)}{P(w)P(c)}$$The numerator is the number of times we expect to see $w$ and $c$ together assuming we used MLE to calculate $P(w,c)$ then the denominator is what this would be assuming $w$ and $c$ are independent. These range from $-\infty$ to $\infty$ but the negative values are often ignored which means things are less likely to co-occur than we would expect with independence as these values aren't very accurate without large corpora. So it is more common to use **Positive Pointwise Mutual Information** or **PPMI** which replaces negative values with 0. That is $$PPMI=\max(\log_2\frac{P(w,c)}{P(w)P(c)},0)$$

### Formally
We we have a co-occurrence matric $F$ with $W$ rows (words) and $C$ columns (contexts), where $f_{ij}$ gives the number of times $w_i$ occurs in context $c_j$. This can be turned into a $PPMI$ matrix where $PPMI_{ij}$ gives the **PPMI** values of the word $w_i$ with context $c_j$. This will be defines as $$p_{ij}=\frac{f_{ij}}{\sum_{i=1}^W\sum_{j=1}^Cf_{ij}},p_{i*}=\frac{\sum_{j=1}^Cf_{ij}}{\sum_{i=1}^W\sum_{j=1}^Cf_{ij}},p_{*j}=\frac{\sum_{i=1}^Wf_{ij}}{\sum_{i=1}^W\sum_{j=1}^Cf_{ij}}$$$$PPMI_{ij}=\max(\log_2\frac{p_{ij}}{p_{i*}p_{*j}},0)$$A problem with **PPMI** is that low frequency words that co-occur will have very large PPMIs. One way to get around this is to raise the power of the context probability $P(c)$ to a power $\alpha=0.75$ for example. This way $$P_\alpha(c)=\frac{\text{count}(c)^\alpha}{\sum_C\text{count}(c)^\alpha}$$with $$PPMI_\alpha(w,c)=\max(\log_2\frac{P(w,c)}{P(w)P_\alpha(c)},0)$$Raising the context probability to $\alpha=0.75$ raises the probability for infrequent context and so lowers their PMI. We could also use [[Evaluation and Smoothing]] **Laplace Smoothing**.