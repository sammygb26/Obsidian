# Array
An array is a reserved piece of memory split up into the elements of the array (which are of **fixed size**, but can be references to objects if we require that). The upside of this is if we know the start of the array and the size of the entries. Then for any index we can calculate the $i$ element by just multiplying this by the element size and using it as an offset from the start of the array.

**Get/Set Element** -> $O(1)$ time if we know the index of the element

The problem is if we run out of space and we want to make the array bigger we need to create a new array with extra space. Then we need to copy over all the new elements. If we just increase the size form $n-1$ to $n$ therefore we have to perform $n-1$ copy operations. So this would take $O(n)$ time.

**Append** -> O(n) time if we are adding a constant amount of memory at once.

## Extensible Array
An extensible array is like the example above where the size is fixed accept the extension is automatic we just treat it as a list and when it runs out of size all the moving is done automatically. Most of the time append will take $\Theta(1)$ time however when we have to do a extension it will take $\Theta(n)$ time. If we extend by a constant amount it will therefore take $\Theta(n)$ time asymptotically. There is a better version of a dynamic array that has an **amortized** runtime of $\Theta(1)$. But still $\Theta(n)$ in the worst case.