# Interaction Diagrams
These describe the **dynamic** interactions between objects in the system. This would be the patter of messages being passed. They show how a system will accomplish a use case. They are useful when it is complex, there is no need to use when this isn't the case. There are two types of interaction diagrams **sequence** and **communication**.

When we say a message passed to an object $a$ this means an instance of $a$ has the function $a.f()$ called. We say a message is passed rom the object calling $f$ to $a$. The message is replied to when $f$ returns a value. The control flow is passed between the objects allowing them to update and execute code. calling $f$ passed the control flow to $a$. This is like passing a token.

## Developing an Interaction Diagram
We will decide what behavior we want to model. We need to check the system provides the behavior do we have the needed relationships between classes to accomplish the behavior. We need to name the objects involved. We need to identify the sequence of messages which the objects will have to send between each other. then we need to record this in the syntax of an interaction diagram.

We start with a **use case** -> We will know the **scope**, **primary actor** and a **description** telling us what the system is provided with and how behavior should function.
![[Pasted image 20220210124528.png]]
We can show the objects involved at the top (names optional) then we can show when they are alive (exist somewhere) with a dashed line. We when an object is awake calculating or awaiting reply. As bars going down. We then have shaded sections to show when an object has control flow. An object can also call a function on itself and we can give a different bar to show when this ends. Any of this which added extra clutter can be removed to simplify.
![[Pasted image 20220210124815.png]]
We can also show creation and deletion (or possibly lack of accessibility so garbage collection will destroy). Deletion when a function arrow goes to a cross ending the dashed line showing an object is alive. Then creation when an arrow goes to an object creating it and starting its dashed line.

## Conditional and Iterative Behavior
This will allow us to not only capture the primary sequence for a use case but possible paths. This isn't **implementation level** yet however. We will use **sequence frames** which are labeled (indicating the type of the frame) rectangles that capture some part of the sequence. There are two types **optional** and **alternative**. For **optional** if a guard condition isn't met then the control flow will pass over the frame. For **alternative** behavior there are multiple compartments. Depending on a condition control flow will be passed to each the compartments are separated by a dotted line. 

#### Opt (optional) Behavior
![[Pasted image 20220210125310.png]]
In this case the frame will only have control flow passed to it if the okToBorrow method returns true. The label is in the corner of the frame and the guard is in square brackets.

#### Alt (alternative) Behavior
![[Pasted image 20220210130206.png]]
Here we have a condition in square brackets labeling the condition for the first compartment. Then we have the second else compartment that will execute if the first condition is false. If we want further else we would use another frame within a compartment.

#### Loop (Iterative) Behavior
![[Pasted image 20220210130651.png]]
This captures the idea of looping and iteration. We have a frame labeled loop then we have instead of a guard an expression in square bracket that is a loop clause. The **loop clause** just describes what the loop should go over (*while* or *for* etc.).