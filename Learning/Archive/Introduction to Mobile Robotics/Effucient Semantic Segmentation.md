Autonomy is moving into homes more and more. And this is largely driven by advancements driven by deep learning which revolutionized how image processing works. This comes at the cost of the workload required for these networks.

![[Pasted image 20221216130103.png]]

Since the advancement of hardware and the amount of compute required for the networks isn't scaling at the same rate this had driven the development of embedded ML. There are many requirements we have with robotic image processing

1. High accuracy
2. Low latency
3. Limited resources
4. Power/ payload constraints

Reducing the cost of our system can help in many regards therefore. At it improves user-experience, functionality by allow other tasks to run and safety as mission critical decisions can be made quickly.

### Approximation
Here we can make the network perform in a cheaper way by approximating the weights. Generally networks don't need all the parameters hence this can give good results with far less parameters. We can also perform model search which gives models that work well with less resources. Or we can train and then perform pruning on the network to work well with a given task. We can also approximate actual **outputs** as we may not need our entire in full output with all its precision.

### Approximation on Semantic Segmentation
This is a **dense** prediction task where each pixel need to be classified.

![[Pasted image 20221216131000.png]]

### Semantic Segmentation Approaches
SOTA SemSeg approaches are based on deep neural nets featuring impressive accuracy but large and excessive compute ad memory requirements. To get around limited data we use a pretrained image classification network and spread out its layers throughout a new CNN we use for semantic segmentation. There base classifier has already powerful feature extractors we then fine tune on our segmentation dataset. This is called **dilated residual networks**. Since we are downsampling the network there will be some positional information we cannot recover. We use **dilated/ attruse convolution** where we expand and pad our image our and pad it with zeros. This increases the receptive field after a number of conv layers. The problem is the computations resources needed explode becoming far larger. Hence we **need** to compress the network.

### Adaptive Inference
In **model cascades** have a dynamic network where we take a different amount of compute for each image which will be proportional to the difficulty of this classification. IF there is enough confidence we pass it through a better network (left). There are also **early exit models**. Where at many point we can check if we should exit or note (if we are confidence in an image). We continue progressing until we have achieved a good result. 

![[Pasted image 20221216132012.png]]

This models give good **throughput** but sometimes the **latency** can be worse. With **early exit models** we reuse our computation again and again hence we get better latency. This works well with **semantic segmentation** as it works out the works case with semantic segmentation which is the computational cost.

### Candidate Exit-points
One way is the generate candidate exit points for a number of places within the network. Deeper exits have much more overhead as the depth increases and so most of the computational load takes place towards the end. Each pixel at the beginning has a smaller receptive field and so the results may be worse. We give different architectures for each exit point as each exit will have a different output. For example earlier by require more upsampling.

### Training
We can train the network through many different nodes. We take a different loss on each network and so this gives conflicting gradients as each exit requires different computation from the network. This can cause the network to **not converge**.

We can also freeze and train the **backbone** then later only train the exits individually. Hence we ignore the backbone and train exits only. This is called **frozen backbone training** this gives no conflicting gradients as they are blocked form each other. However only a few weights are training so early exits aren't a good.

We can also train then only sample from the backbone and some random early exit at the beginning. This mainly trains the backbone but keeps it loose needing to conform to some exits. The exits are then trained as before.

![[Pasted image 20221216133416.png]]

### Inference
**Budgeted Inference**: here we extracting workload-lighter sub-models.
**Anytime Inference** we progressively refine over time. So time critical outputs can be given quickly.
**Input-Dependent Inference** here we dynamically follow a different path depending on the image.

### Search and Deploy
This call gives a massing configuration space. We can search through these estimation space. We can then find the network within this system that fits our requirements.

### Input dependent Inference
We make out network also output a confidence map. We cannot average this as with a lot of background confidence gives erroneous results. Can compare the percentage of our object that is low nonconfidence.

![[Pasted image 20221216134055.png]]

The edges will always be poor in confidence and so we can weight only the parts not on the edge to give better results.

![[Pasted image 20221216134141.png]]

As workload deceases we can get good results but we need to find a sweets spot to get good results with lower computation cost. The network 2.8x faster or we can improve performance by 5.33pp by spending out computation where it is needed.

Other research has exited on different pixels. But this latency doesn't improves with this as regularity of computation is reduced so the parallelism isn't exploited.

