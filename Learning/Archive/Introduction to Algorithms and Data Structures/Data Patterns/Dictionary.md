# Dictionary
A **Dictionary** is a common pattern where a collection of elements that aren't organized by some order but instead can be referenced by another element called a key. The dictionary given a key will return an element.

## [[List]] implementation
If we implement a dictionary as a list we will have to check over all the elements until we find a matching key this will take on average $O(n)$ time. This can be reduced in our list is sorted as we can do a binary search taking $O(ln(n))$ time.

## [[Hash-Table]]s
The idea behind hash tables is we would like to have a fixed array the length of the number of possible keys for a dictionary. But this space is far to large. We use a **hash function** which breaks a key into a value that varies over a much smaller range possible of our choosing. We then have a list in each of these **bins** that allows us to store multiple actual key pairs.

[[Dictionary Questions]]