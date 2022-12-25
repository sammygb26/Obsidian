# Tasks
In *linear regression* we are trying to find some function from $\textbf R^d\to\textbf R$ but we don't have to be limited to just one real number we can instead do $\textbf R^d\to\textbf R^k$ where we have $\textbf W$ matrix instead of $\textbf w$ vector. For some classification we learn a function $\textbf R^d\to\mathcal Y$. 

### Problem Reduction
The idea with reduction is if we can solve some *problem B* then if we can convert some *problem A* to *problem B* then convert to solution back to problem A we have basically solved A.

![[Pasted image 20221003152438.png]]

We say *problem B* is **harder** than A.

### Digit Recognition
Here we are trying to recognize problem from $\textbf R^{28\times28}\to\{0,1,...,9\}$.

![[Pasted image 20221003152612.png]]

So this is a form of *multiclass classification*. An bellow are the learned $w$s.

![[Pasted image 20221003152703.png]]

### Face Recognition
![[Pasted image 20221003152742.png]]
Saying if there is a face in an image. It is binary classification hence form some $m\times n$ image we are learning a function. $\textbf R^{m\times n}\to\{-1,+1\}$. We need to design some $\phi$ to do this well.

The green boxes are called bounding boxes so we may want to learn how to find these boxes. For example we may want to find the two red boxes bellow.

![[Pasted image 20221003152952.png]]

In this case we are learning a function which takes in some image and two points. It will therefore be $\textbf R^{m\times n}\times\textbf N^2\times\textbf N^2\to\{-1,+1\}$.

### Speaker Identification
The task here is to take a wave form and tell who is speaking. A *waveform* is really a series of real number say $T$ of them. Then there may be $K$ speakers hence the function we learn is $\textbf R^T\to\{1,...,K\}$.

![[Pasted image 20221003153324.png]]

### Speaker Recognition
Here we take two speech sample and we want to try if they are the same speaker. Hence this is a *binary decision*. $\textbf R^T\textbf R^T\to\{-1,+1\}$.

![[Pasted image 20221003153437.png]]

### Speech Recognition
Here we want to find the words someone is actually saying. The input will be a *waveform*. An example of how we could formulate this is with $T$ samples in our dataset then we have $V^*$, where $V$ is a set of possible words. $V^*$ is called the Kleene closure of $V$, meaning zero or more items concatenated. We can cast this into a classification problem where one problem is to say if there is another word. Then the other is what the word we have picked out is.

![[Pasted image 20221003154135.png]]

### Speech Synthesis
Here we are trying to take a sentence to a wave form. The input is $V^*$ then the output is $\textbf R^K$. Then we cay say this is a sequence of regression problems. We we do $T$ regressions.

![[Pasted image 20221003154706.png]]

### Sentiment Analysis
Here we take in a sequence of words $V^*$ and we want to predict how positive or negative it is.

![[Pasted image 20221003154809.png]]

Then this I just regression.

### Machine Translation
![[Pasted image 20221003155041.png]]

### Example Representations
We need representations $\phi$ that encode our different input types.

![[Pasted image 20221003155157.png]]

