How does insert sort work? #flashcard #IADS #SortingAlgorithms
	This works by for each element in the array we compare it to every element to its left if it is smaller that the one to the left we swap them then move to the next value to the left. We do this until we have reached the end or we have a value that is smaller than our value. This builds up a sub list that is sorted one element at a time.

---
What is the asymptotic running time of insert sort? #flashcard #IADS #SortingAlgorithms 
	In the worst case it is O(n^2) and in the best case it is O(n) however in the average case it is also O(n^2)

---
How does merge sort work? #flashcard #IADS #SortingAlgorithms 
	Merge sort works by breaking down a list into sub lists of similar size these sub lists are sorted then we merge the two back together. The key idea is it is computationally more efficient to merge already sorted lists than unsorted lists.

---
What is the asymptotic running time of merge sort? #flashcard #IADS #SortingAlgorithms 
	In the best, worst and average case it will be O(n lg(n))

---
Is merge-sort in place? #flashcard #IADS #SortingAlgorithms 
	No it isn't. The merge step requires the creation of two extra arrays. To sort in place would require a more complicated merge function taking the time complexity to $O(n^2\cdot ln\hspace{3pt}n)$.

---
How does quick-sort work? #flashcard #IADS #Heap 
	Quick sort works by taking some pivot point then sorting an array of values into a section less and a section greater than the pivot. Each of the smaller sections can then be further quick sorted recursively.

---
How does the partition algorithm for quicksort work? #flashcard #IADS #Heap 
	The idea is we use two pointers to keep track of the end of the lesser values and the end of the greater values. Each time we move the greater one along and if the value is smaller we can move the lesser pointer along and swap. 

---
