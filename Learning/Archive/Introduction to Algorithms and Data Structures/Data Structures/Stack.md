# Stack
A stack is similar to a list but has restricted operations. We can only **pop** and **push**. When we **push** we add something to the top of the stack. Then when we **pop** we remove and return something from the stack in the order what was last added first. So we get a Last in First out type of behavior.  The benefit is restricting the behavior lets us make these operations run fast. We have the basic structure be that of a linked list where each stack element points to the one added before it. But the stack object keeps pointing to the last added element. So it will take constant time to find and remove it.

**Pop** -> Takes $O(1)$ time for an element to be removed from the top of the stack.

It will also take constant time to create a new element and assign its next to the current stack top. Then just reassign the stack top to this new element.

**Push** -> Take $O(1)$ time for an element to be added to the stack.
