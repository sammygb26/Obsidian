Raw-frequency as in [[Vector Semantics]] and [[Cosine for Measuring Similarity]] don't capture enough as what we really want to know is if words are more frequent that we would expect given how frequent the word is anyways. So this works well for *cherry, digital, information and strawberry* since they aren't that common and their context is very dependent on them. But for words like *the, it* or *they* which are very common with many different words this isn't good enough.

This means very low occurrences don't matter as their is no connection between words but equally very high occurrences don't matter as the word appears with everything. The options for this are **tf-idf** and [[PPMI]].

**Tf-idf weighting** is a product of two terms. The **term frequency** for a word $t$ in a document $d$ can just be the raw count. $$tf_{t,d}=\text{count}(t,d)$$More commonly a squashed version is used in $\log_{10}$ since a word appearing 100 times in a document isn't 100 times more likely to be relevant. So we use $$tf_{t,d}=\log_{10}(\text{count}(t,d)+1)$$We add 1 so we don't take the $\log$ of 0! The second factor gives a higher weight to words that occur rarely. Terms limited to few documents are more useful than ones present in all documents. The **document frequency** $df_t$ of a term $t$ is the number of documents it occurs in. This *isn't* the same as **collection frequency** which is defined as the total number of times it occurs in a given collection.

![[Pasted image 20230411185330.png]]

Terms with low document frequency are emphasized with the **inverse document frequency** or **idf**. This is defined as the fraction $N/df_t$ where $N$ is the total number of documents in the collection. Since a large number of documents is used in many collection again we usually squash this with a log function. $$idf_t=\log_{10}\left(\frac N{df_t}\right)$$The $idf_t$ can be given for different terms as bellow and we see that low $df$ terms are weighted highly while terms which are seen in all documents are ignored.

![[Pasted image 20230411185834.png]]

In **tf-idf** the weighted value $w_{t,d}$ for a word $t$ in a document $d$ combines the term frequency and idf. $$w_{t,d}=tf_{t,d}\times idf_t$$This tf-idf weighting is how weighting is done for matrices in information retrieval but also plays other roles in NLP.

![[Pasted image 20230411190207.png]]

