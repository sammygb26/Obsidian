What is the main purpose of balance trees? #flashcard #IADS #BalanceTrees
	Balance trees allows for efficient indexing of items within the tree. That is a matching element can be easily found within the tree.

---
For balance trees to yield a good asymptotic runtime on searching for an element what kind of state must they be in? #flashcard #IADS #SortingAlgorithms 
	The tree must be balanced meaning there is a similar amount of elements in each subtree for any node.

---
How does insert work in a standard binary tree? #flashcard #IADS #SortingAlgorithms 
	To perform an insert we navigate the tree as usual looking for a where our new node would be in the tree. We keep doing this until we find a null spot (as we will tree values exactly the same as if they were greater or smaller). At this point we can place our insert in place of the null child.

---
How does delete work in a standard binary tree? #flashcard #IADS #SortingAlgorithms 
	Delete can simply delete a node if that node has no children. If the node has a single child we can slide that child up in place of the deleted node. The final case is there are two children of the deleted node. The idea here is the find the greatest node in the lesser branch then transplant it in place of the deleted node. Of course since it is the greatest it can only have a lesser subtree so we just slide that in place (if it exists).

---
What is a red-black tree? #flashcard #IADS #SortingAlgorithms 
	A red-black tree is a type of balanced tree that colors it's nodes red or black in order to maintain a invariant ensuring the tree remains balanced.

---
How is a red-black tree defined to ensure it remains balanced? #flashcard #IADS #SortingAlgorithms 
	In a red-black tree all the nodes must be either black or red. A red node cannot have any red chidden. Any path to a null subtree will pass through the same number of black nodes. This all ensures in the worst case  the depth of a leaf (null node) is never more than twice the best case.

---
What is the height of a balanced tree? #flashcard #IADS #SortingAlgorithms 
	The height of a balanced tree is how deep the tree is at the most. For example the greatest number of children of children for any node. The height in this way describes the worst case time it would take to find some key value.

---
What is the height of a red black tree guaranteed to be in the worst case? #flashcard #IADS #SortingAlgorithms 
	When the red-black properties are satisfied the height will be at most $2lg(n+1)$

---
Describe how and why rotations are possible within a binary tree? #flashcard #IADS #SortingAlgorithms 
	The key idea behind rotations is that all subtrees and their parents can be seen in a sorted order when considered all in a line. This means that we can shift this order over by swapping a child node with a parent node. The child will keep the parent in the opposite place the parent kept the child so this can be used to rebalance two trees.

---
Describe how insert work with a red-black balanced tree? #flashcard #IADS #SortingAlgorithms 
	We can insert a node like usual and make it red. This problem is the the parent we inserted under is blacks with will break our RB-properties. We then need to perform a fix-up to overcome this.

---
How is a insert fix-up performed in a red-black balanced tree? #flashcard #IADS #SortingAlgorithms 
	The fix up is triggered with we have a red node with a red parent. A simple case is when our red parent also has a red brother. Their parent must be black so we can turn it red and make both parent and brother black. As we have remove a black and added a black to each subtree the number of blacks to the leaves hasn't changed. This may lead to another fixup if our grandparent's parent is also red. This rule can be applied over and over again until we either solve the problem or have a red parent with no red brother. In this case we can us a rotation to fix the tree.

---
Describe how delete works with red-black trees? #flashcard #IADS #SortingAlgorithms 
	We can delete a node like usual sliding nodes into its place. if we do this any we remove a black node however we need to perform a fixup to restores the RB properties.

---
