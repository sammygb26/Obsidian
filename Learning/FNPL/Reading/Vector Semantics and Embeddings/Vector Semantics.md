**Vector Semantics** is the standard way to represent work meaning in NLP. It was discovered that a 3D point could explain much of the connotation of a word and it was through that the meaning of a word could be described by the **distribution** (neighboring words or grammatical environment). This idea is clear when we look at an example of an unknown word like "ongchoi"

![[Pasted image 20230411151549.png]]

These context are similar to these

![[Pasted image 20230411151603.png]]

suggesting the meaning is similar. We can represent this as counts for surrounding words. This gives a vector in high dimensions representing that word. These vector representations are called **embeddings**.

![[Pasted image 20230411151843.png]]

The benefit of representing words this way is we can transfer meaning from words that appear often in training onto recently learned ones that only appear in similar contexts.