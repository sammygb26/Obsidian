# Queue
A queue is a restricted data type based on a linked list. It only has two main operations **enqueue** and **dequeue**. The way it works is we can enqueue elements one by one. Then when we dequeue we remove and return the elements in the order they were added. This gives First in First out behavior. The implementation is similar to a linked list except an element need only keep a reference to the next item added after it. Our queue as a whole can then just keep a reference to the first element added and the last one for adding new ones.

So to **enqueue** we just look up the reference to the last element. Create our new queue element assign the last one's next element to be this new one. An replace our reference with the new one.

**Enqueue** -> Takes $O(1)$ time to add a new element to the queue

Then to **dequeue** we just look up our first added element, then replace that reference with its next element. Then return the first one.

**Dequeue** -> Takes $O(1)$ time to remove an element from the beginning of the queue.

## Alternative Implementation
We can also implement a queue as an array of fixed size which is the max length of the queue. We can then just keep two indexes to the first and last element of the queue. When we dequeue we just move the first forward one and return the old first. Then for enqueue we just increase the last pointer by one and write our new value or a reference to it.