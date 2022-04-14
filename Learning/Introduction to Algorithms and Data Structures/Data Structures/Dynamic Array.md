# Dynamic Array
A dynamic array is an alteration to the extensible array where instead of extending by some fixed amount we extend by a fraction of our array. This will have an **amortized** cost of $O(1)$ much better than the $O(n)$ for a regular fixed size extensible array. We can also reduce the size when the number of used elements is a fixed fraction of the main array.
