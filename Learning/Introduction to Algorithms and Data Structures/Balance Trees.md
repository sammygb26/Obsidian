# Balance Trees
Balance trees are a special kind of [[Data Structures]] based on the **Tree** data structure. In a *tree* we have each node have two *children* which are also nodes. We can then have some rule that describes the relation between the parent and its chidden. In a basic *binary search tree* we will have a left and a right subtree. We say that all the children in the left three are greater than the parent and all the children in the right are smaller. This is called the **binary-search-tree property** and can be anything we desire.

![[Pasted image 20220224101741.png]]

The benefit here is that if we want to find any particular item we only have to turn left or right at each node until we find the value we are looking for. If our *tree* is **balanced** this will mean that we more or less have even amounts in any given subtree. This means each time we make a decision the size we have left to explore halves. This means to find some element it will take $O(lg(n))$ time. Unlike in a liked list or array where it will take $O(n)$ time. The problem with an **unbalanced** tree is that our worst case time will have us searching through what amounts to a linked list so no better than before taking $O(n)$ time. In a **balanced** tree we take measures to ensure the depth of the tree doesn't becomes the worst case and so we keep the worst case time for many operations to be $O(lg(n))$.

## Search
Search in a binary tree is quite simple. We reach a node and we check if it is the one we are looking for if not we go into the subtree that is in the right *direction* to find out answer.

![[Pasted image 20220224103154.png]]

This will take $O(lg(n))$ in the average case and $O(n)$ in the worst unbalanced case.

## Minimum and Maximum
These are also simple algorithms we just turn right at every node for a max and turn left for a min until we find we can keep turning.

![[Pasted image 20220224103344.png]]

![[Pasted image 20220224103401.png]]

## Insert
To **insert** into a binary tree all we have to do is explore until we find the slot where the subtree is more extreme and the current node is less extreme. We can then make a new node  and more the child nodes to a subtree if there are any.

![[Pasted image 20220224103614.png]]

This again will run in $O(lg(n))$ in the average case and $O(n)$ in the worst case.

## Delete
To **delete** a node can be a bit more tricky. If we are deleting a node with no children we can just delete it and if we are deleting a node with 1 child we can just slide it in. If we have two children we want to either find the minimum in the greater subtree or maximum in the smaller subtree. We can then delete this value and re-insert it in place of the node we are deleting.

![[Pasted image 20220224104226.png]]

We need this helper function **transplant** that takes two nodes $u$ and $v$ and replaces $u$ with the subtree with root $v$. So we check if $u$ has some predecessor, if it does then we set $v$ to be the correct child which would have previously been set to $u$ then we set $v$'s predecessor to be $u$'s.

![[Pasted image 20220224104642.png]]

Again this takes time proportional to the height of the tree so will take $O(lg(n))$ on average but $O(n)$ in the worst case.

## Balanced Trees
So solve the problem of unbalanced trees we have to ensure that the height of the trees doesn't becomes to far form the best possible $lg(n)$ height. That is we keep it tight bound to this $lg(n)$. But we need our procedure for balancing to take only $O(lg(n))$ time hence we maintain $O(lg(n))$ time for all operations.

# Red-black trees
In a **red-black tree** we store an extra piece of information in each node that its its color which is either *red* or *black*. We use this to enforce restrictions on the total height as we must maintain **red-black properties**. We also keep track of leaf nodes here which are always considered black.

![[Pasted image 20220224105947.png]]

This gives a tree with a structure like that bellow although leaf nodes can be omitted.

![[Pasted image 20220224110037.png]]

The tree must have a height of at most 2lg(n+1). A node can't have a black node in a subtree if it has a Nil child. As if it did then there would be a difference in the number of blacks to a left in the subtree. But if it isn't black then it must be red. This means the next nodes must be black. Hence in the worst case we have some subtree that it completely black. then some other subtree alternates black then red but has the same number of black nodes $b$. So either we alternate giving us $2\cdot lg(n)$ or we have just black perfectly balanced tree with $lg(n)$ height. But we never have a subtree with $n$ height or an proportion of it.

## Rotations
We can run usual **Insert** and **Delete** operations in a **RB tree** but we will have to take care afterward to ensure the **RB properties** are maintained. We will have to change some color and also change the structure of the tree. This is done through **rotations**, which are local operations. There are two kinds **left** and **right** rotations. We assume for left rotations we assume the right child isn't Nil and visa versa for right rotations. Here is the pseudo code for $Left-Rotate$ 

![[Pasted image 20220224111514.png]]

The idea is basically that we are altering the structure as to bring up $y$ into $x$'s place. Then we move around the subtrees to preserve the **binary structure**.

![[Pasted image 20220224111814.png]]

![[Pasted image 20220224111848.png]]

## RB Insert
We will use a modified regular **insert** procedure to ensure **RB properties** are maintained over an insert. We find a leaf node and we insert out new node into it. If the parent to the left it black we can just color this red and we are done. If the parent is red adding a red node would break our **RB properties** hence we need to fix the tree.

There are some difference cases for this. If we run into a problem but the sibling to the parent is also red like the parent. Then the grandparent will be black hence we have make both siblings black moving the black down. This doesn't change the number of black to the leaves as we take away one black from each node completely. But this can also lead to a problem if the grandparents parent is also read. But we can recursively apply these rules. We apply this rule as many times as we have so this can be at most the height of the tree hence this is **O(lg(n))** time. After this we will be in one of three situations.

1. The most recent red has a black parent as we have a **legal** **RB** tree.
2. We have pushed the red to the **root**. Here we just make the root black.
3. We need to **rebalance** the tree. For example the sibling to the parent is black. Here we apply a corresponding rotation.

![[Pasted image 20220224113814.png]]

![[Pasted image 20220224113849.png]]

We apply this algorithm and then do an **insert fixup**.

![[Pasted image 20220224113918.png]]

The end-game scenarios take $O(1)$ time hence overall it will take $O(lg(n))$ time.

## Delete
The problem is if we remove a black node then we have to add the blackness black into some node. We can move the black up if we can remove some level of black form the sibling. We can for example make it red if its children are black.

![[Pasted image 20220224114937.png]]

This again can continue reclusively if the parent is black. Then the blackness can't settle. This can at most take $O(lg(n))$ time again since it can at most done for the whole height of the tree. This again will leave us in endgame scenarios where we have constant amount of work to do.

![[Pasted image 20220224115734.png]]

![[Pasted image 20220224115750.png]]

![[Pasted image 20220224115812.png]]
