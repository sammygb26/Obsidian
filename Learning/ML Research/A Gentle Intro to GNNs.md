Many things can be seen as graphs. Graphs can be represented as a set of vertices $V$ and a set of edges $E$. The set of edges will be either ordered (in which case it will be a set of ordered pairs of vertices) or unordered (in which case it will be a set 1 or 2 order sets).

##### Images as Graphs

![[Pasted image 20230211151028.png]]

An image can be seen as a graph with edges connecting pixels to their neighbors.

##### Text as Graphs
If we create digitize text by making the vertices (and so indices to the adjacency matrix) the words of the graph. We then associate each word to the next.

![[Pasted image 20230211151233.png]]

##### Graphs in the wild
These kinds of data may be hard to capture without a graph representation.

**Molecules** - These can be represented as graphs with their atoms and vertices and bonds as edges.

![[Pasted image 20230211151633.png]]

**Social Networks** - Peoples can be vertices and edges relations

![[Pasted image 20230211151746.png]]

![[Pasted image 20230211151812.png]]

**Citation networks** - Citations between scientists can also be represented by graphs. This would include either the papers or the scientists as vertices and edges as citations (possible directed).

Graph data can be very diverse and the number of edges and vertices and change wildly.

![[Pasted image 20230211152014.png]]

### Problems with Graph Structured Data
There are generally three general types of prediction we may want to perform on a graph.

##### Graph level
We predict a single property for a while graph. For example for a molecule we may want to know its affinity for a receptor of its toxicity.

![[Pasted image 20230211152513.png]]

##### Node level 
We predict some property for each node in the graph. This could be to detect the role of each node within a graph.

A classic examples is **Zach's karate club**. Here a political rift has split the club. Based on the known relations between the members we may want to predict their allegiance to two other members.

![[Pasted image 20230211152721.png]]

##### Edge level
We predict some property or the presence of edges in a graph.

![[Pasted image 20230211152940.png]]

All the below problems exists in these levels.

All of these problems levels can be seen in images. In this case **Graph level** problems are like image classification. **Node-level** problems are like image segmentation. **Edge prediction** could be image scene understanding.

### Challenges of Graphs in Machine Learning
Modern ML techinques like NNs treat data as grid and vectors so how can we represent graphs.

##### Nodes
These could be represented by a vector of features. With $m$ features and $n$ notes this would yield and $n\times m$ matrix.

##### Connectivity
This is more complicated. This could be represented as an adjacency matrix but the size grows quadratically with the number of nodes. This often gives sparse adjacency matrices which are inefficient.

Another problem is many matrices can give the same connectivity and there is no guarantee these graph would perform the same when passed through the network. This means they are not **permutation invariant**. For example all the bellow matrices give the same connectivity

![[Pasted image 20230211153639.png]]

An **adjacency list** is a more efficient way to store a graph. We store a edge as a 2-tuple. So $(i,j)$ means $n_i$ is adjacent to $n_j$. The number of tuples is always less than the $N^2$ size of the adjacency matrix. 

![[Pasted image 20230211154138.png]]

# Graph Neural Networks
The *adjacency lists* are **permutation invariant** now we need a NN that can operate on them. A GNN is an optimizable transformation on all attributes of the graph (nodes, edges, global-context) that preserves graph symmetries. GNNs uses a *graph-in-graph-out* architecture meaning that these model accept a graph as input and progressively change these embedding without changing the connectivity of the input graph.

### Simples GNN
For this architecture we will learn new embedding for all graph attributes (nodes, edges, global), but connectivity is ignored.

This GNN can use an MLP or any other differentiable model. It does this for each component of a graph. This is called a **GNN-layer**. each node vector, we apply the MLP and get back a learned node-vector. We can also do the same for edges (with edge vectors) and the same for any **global context vector**.

![[Pasted image 20230211155006.png]]

Like with many NN architectures these layers can be stacked together.

This gives the same number of feature vectors as the input but the imbedding will be updated. The GNN updates the embedding for each node, edge and global vector.

### GNN Predictions by Pooling Information
We now want to predict features of the different element of our graph to solve problems like those above. For example in binary classification we could apply a linear classifier to each embedding. 

![[Pasted image 20230211155409.png]]

However we may need information to predict something about the node that isn't stored in the nodes vector. It could be stored in edges for examples. This is done via **pooling**. There are two steps

1. For each item to be pooled **gather** each of their embedding and concatenate them into a matrix.
2. The gathered embeddings are then aggregated (usually via a sum operation).

This is usually represent with the letter $\rho$. We denote that we are gather information from edges to nodes as $p_{E_n}\to V_n$.

![[Pasted image 20230211155754.png]]

With this say if we only had edge features and we are trying to predict binary node information we can use pooling to **route** or **pass** information to where it is needed. The model could look like

![[Pasted image 20230211155928.png]]

With only node level feature predicting binary edge level information could be done as

![[Pasted image 20230211155959.png]]

**Global average pooling** - This is the special case where we only have node-level features and we need to predict a binary global property. This is called such as it is analogous to global average pooling in CNNs.

![[Pasted image 20230211160152.png]]

Note with all these the classification mode $c$ could be replaced with any differentiable model. Or it could be adapted to multi-class classification with a general linear model.

![[Pasted image 20230211160314.png]]

This approach is the most basic but doesn't use the **connectivity** of the graph at all.

### Passing Messages Between Parts of the Graph
A more sophisticated prediction could be allowed by using pooling in the GNN layer to allow the learned embedding to be aware of the graph's connectivity. This is done via **message passing** where neighboring nodes or edges exchange information and influence each other's embeddings. This happens in three steps.

1. For each node in the graph **gather** all the neighboring node embeddings which 
2. Aggregate all messages via an aggregation function (like sum)
3. All pooled messages are passed through an update function *usually learned neural network*

*Note:* The last two steps can be reversed if desired. 

This message passing can only occur between nodes or edges.

![[Pasted image 20230211161735.png]]

We can update the GNN diagram to show this new kind of layer.

![[Pasted image 20230211161909.png]]

This can move from nodes to nodes or edges to edges.

### Learning Edge Representations
Above we moved information from edges to nodes.  In a similar way messages from nodes can be passed onto edges. But the sizes of embeddings will be different. A linear mapping could be learned form edge to node embedding (or visa versa). They can also be concatenated before the update function.

![[Pasted image 20230211163505.png]]

How attributed are updated and in what order is a design decision. There are many different ways one is **weave fashion** where there are four updated representation that get combined into new node and edge representations.

1. Node to node (linear)
2. Edge to edge (linear)
3. Node to Edge (edge layer)
4. Edge to node (node layer)

![[Pasted image 20230211163836.png]]

### Adding Global Representations
The problem with the above description is far away nodes may find it hard to communicate. As we need $k$ layers to communicate $k$-steps away. Nodes could be able to pass information to any node. This is called **virtual edges** but this is infeasible for large graphs.

Another solution is the global representation of a graph (U) also called a **master node** or cortex vector. This si connected to all other nodes and edges in the network. So can conduct information between them.

![[Pasted image 20230211164431.png]]

In this view of graphs all attributes have a learned representation. We can leverage these representations during pooling by conditioning the information for some attribute on the rest. If we want to condition a nodes embedding on all of these different pieces we may want to concatenate them to pass them into a layer. We can also perform a feature-wise attention mechanism by mapping these embedding to our feature pace then using this a feature wise modulation.

### Empirical GNN Design Lessons
The combination of aggregation functions, message passing used and activations will depend on the data.

Generally more parameters give higher performance. But like with other NNs this has a decaying effect.

Generally increasing any imbedding di will improve model minimal performance. But the max values archived may occur ad smaller values.

A similar thing is true for the number of layers although even the peak in minimum performance may occur. This is general in GNNs which more layer having strong signals diluted with successive iterations. 

Generally **more** message passing can be seen to improve the performance of the network.

Generally aswell it pays to make the graph representation more powerful and incorporate more information into it.

### Into the Weeds
There are many other types of graphs but message passing gives enough flexibility to model them too. To adapt to these networks GNN information passing updates can be defined for these new graphs.

**Multi-graphs** - have multiple types of edges. This could for example show different kinds of information.

**Hypernodes** - are nodes that represent graphs. These allow nested structure. For example in chemical reactions we could have a chemical graph and a reaction graph working at different levels.

![[Pasted image 20230211172859.png]]

**Hypergraphs** - contain edges which can connect to more than two nodes. For example edges can connect communities of nodes together.

### Sampling Graphs and Batching in GNNs
Batching can be hard with GNNs as the node connectivity changes for each sample so changing the size of the tensors which need processing.

One way to get around this is to sample from the graph a constant part of it. We can then batch on these constant portions. If the subgraphs can maintain essential properties of the whole graph we can still learn on them. There are different ways to sample.

Like *random sampling*, random sampling with neighborhood, random walk, random walk with neighborhood or diffusion sampling.

![[Pasted image 20230211173616.png]]

### Inductive Biases
Many popular NN types take advantage of regularities in data and invariant properties. We want to build these into our GNNs aswell so simplifying learning and parameter usage.

GNNs already offer permutation invariance and can preserve explicit relations through their adjacency matrices.

### Comparing aggregation operations
We want to use a smooth aggregation operation that is invariant to node ordering and the number of nodes provided. Some simple ones are **max**, **mean** and **sum**.

![[Pasted image 20230211174244.png]]

Generally max can be useful when you want a highlight over salient features. Mean can be useful when node number are highly variable. While sum can give the best of both worlds.

### GCN as subgraph function approximators
Message Passing Neural Networks and Graph Convolution Networks of $k$-layers with degree 1 neighbor lookup can also be seen as neural networks that operate on learned embeddings of subgraphs of size $k$.

One nodes state after $k$ layers the representation has a limited viewpoint of all neighbors up to $k$-distance.

The graph is for each node taking the POV of the node. But it is more efficient as we perform all nodes at once.

![[Pasted image 20230211175006.png]]

### Edges and the Graph Dual
Edge and node prediction seem different but can be reduced to the same problem often. So an edge prediction task on a graph $G$ can be phrases as a node-level prediction on $G$'s dual.

To obtain this dual we can convert edges to nodes and nodes to edges. The same information is contained but expressed differently. Sometimes problems are easier in one representation or another.

### Graph Convolutions as matrix multiplications and matrix multiplication as walks on a graph
This goes over the implementation of message passing and the connection to matrix multiplication.

If we have an adjacency matrix $A$ ($n\times n$) and a node feature matrix $X$ ($n\times m$). Then the operation $$B=AX$$ operates a simple message passing with summation. Here the rows of $X$ are the node vectors. A 1 in $i,j$ row of $A$ will mean $j$th nodes message is passed to the $i$th. The $B_{ij}$ element will be $\langle A_{\text{row}i}X_{\text{column}j}\rangle$. For any 1 value sin the row $i$ will mean $i$  is adjacent to the node of that column. This is the $j$th entry of that $B$ and so the $j$ features of $X$ are used.

The benefit of adjacency lists is that all the summing of zero values is removed. We can also use operations other than sum. The traversal power of GNNs can also be seen when we take powers of the adjacency matrix.

### Graph Attention Networks
Attributes can also uses graph attention to communicate. We can consider performing a weighted sum of neighbors. But we need to do this in a **permutation invariant way**.

A **scalar scoring function** can be used that assigns a weights based on a function that takes in the two notes features. $$f(node_i,node_j)$$This measures how relevant some node is to the center node. This can be normalized with a SoftMax  is a weighted mean is desired. This is based on **Graph Attention Networks** and **Set Transformers**. Permutation invariance is preserved as this operation takes place over pairs of nodes.

![[Pasted image 20230211181606.png]]

In this view transformers can be seen as fully connected GNNs with a graph attention mechanism.

### Graph explanations and Attributes
Here we want to understand which parts of a graph are relevant to a decision. One way is to break a graph down into the most relevant parts.

![[Pasted image 20230211181934.png]]

### Generative Modeling
Here we also care about generating a graph model. We may want to complete a graph given a starting point for example.

One way it to model the graph as an adjacency matrix then an autoencoder could be used to complete some incoming graph.

Sequential alteration could also be performed adding parts one at a time and slowly building up a graph.
