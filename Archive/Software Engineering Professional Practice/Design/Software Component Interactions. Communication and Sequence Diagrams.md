# Software Component Interactions
We have looked at a **static** structure in [[Detailed Design, Software Design Principles]] we will now look at more **dynamic** structure with interactions. We can look at in in two ways
1. inter-object behavior -> Who sends which message to whom 
2. intra-object behavior -> what state changes does an object undergo and how do objects affect this.

We will focus on inter-object behavior. But this is described in [[State Diagrams]]. The structure will depend on the use cases but it is good to use few objects for each use case and try not to duplicate functionality. This can all get complicated when several objects start collaborating, one way to fix this is with [[CRC Cards]].

## Interaction Diagrams
These describe the **dynamic** interactions between objects in the system. This would be the patter of messages being passed. They show how a system will accomplish a use case. They are useful when it is complex, there is no need to use when this isn't the case. This is covered in [[ Interaction Diagrams]].

## Deciding on the Interaction Patters
We have seen an interaction patter in a sequence and communication diagram. But we need to consider further things in the design.

**Conceptual Coherence** -> Does it make sense for this class to have that operation?
**Maintainability** -> Which aspects might change and how hard will it be to change interaction accordingly.
**Performance** -> Are the things we are doing necessary is there a more efficient way to do it.

Take the example below
![[Pasted image 20220210153504.png]]
We have a Job needing to get its controller but it does this through the Everything Controller. This is convoluted and doesn't make much sense so why is it done this way. Its due to **navigability** it is easier to give the job one function to call one one object that to store many Job controller and keeping a job updated. This has low **conceptual coherence** since the job would logically be in the job controller. This makes is harder to **maintain** and **understand**.

## Reduce Longer Range Coupling
We have the **law of Demeter** design principle which recommends that in response to a message m an object O should send messages only to the following objects
1. O itself
2. Objects which are sent as arguments to the message m
3. Objects which O creates as part of its reaction to m
4. Objects which are directly accessible from O, that is using values of attributes of O

![[Pasted image 20220210155454.png]]
In this example an A operation needing to access parts of data in C. We could have A pass a message to B that returns C this would allow A to access C and send messages to it however (this would increase **coupling**). Instead we have a function in B that retrieves only the data C wants (reduces **coupling**). So with the **Law of Demeter** we would only pass messages to an object one step ahead and not two steps away.