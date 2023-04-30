Vector and distributional models of meaning are generally based on a **co-occurrence matrix** which represents how often words co-occur!

### Vectors and Documents
In a **term-document matrix** the rows are for words int the vocabulary and the columns for different documents.

![[Pasted image 20230411152741.png]]

Each word and document can be seen as vectors where ethe **documents** are in a $|V|$ dimensional space and the words are in a $|D|$ dimensional space. These matrices were original used for **information retrieval**. We can visualize these vectors to spot similarities between the documents.

![[Pasted image 20230411153201.png]]

In **Information retrieval** we want to find a document that best matches a query. We can represent the query as a vector in a $|V|$ dimensional space then we compare the $q$ to the $d$ vectors to get similarity to rank documents.

### Words as Vectors: document dimensions
Here we represent each word with a **row vector**. Similar words should have similar vector as they occur in similar documents. But this is only for some collection of documents giving a size of $|D|$ for the vectors.

### Words as Vectors: word dimensions
We can instead use a **term-term matrix** also called a **word-word matrix** or **term-context matrix**. The columns are words rather than documents giving a $|V|\times|V|$ matrix. Each entry describes the number of times the *row* (target) and *column* (context) word co-occur in some context in a training corpus.

This **context** could be the *document* which would mean the entries were the number of times the words were in same document summed up. But often small context windows like 4 words to the left and right are used.

![[Pasted image 20230411154103.png]]

A sample of a matrix we may get could be

![[Pasted image 20230411154137.png]]

Words occurring the same window will have similar vectors.

![[Pasted image 20230411154232.png]]

The vector size will be 50,000 only the top most frequent words (not the 50,000th) are useful in word context. These counts will often be 0 giving a **sparse** vector representation.