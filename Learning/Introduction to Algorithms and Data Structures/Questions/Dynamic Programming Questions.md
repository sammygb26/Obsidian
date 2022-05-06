What is dynamic-programming? #flashcard #IADS #DynamicProgramming
	It is a problem solving approach to designing algorithms. The idea is to break a problem into a recurrence relation and then find a way to store and order to calculate the subproblems to build up to the solution effectively.

---
What are the main steps to solve a problem dynamically? #flashcard #IADS #DynamicProgramming 
	To solve a problem dynamically we need to find a way to break it down into a recurrence problem. From this point we need to find some way of structuring the data such that.

---
How can Memoization and how can it be used? #flashcard #IADS #DynamicProgramming 
	Memoization is a technique to turn a recursive algorithm into a dynamic one. The idea is as we run a recursive algorithm we save the results in a lookup dictionary this way if we ever reuse some result we have already calculated we first look it up. When the recursive calls grow polynomial with the problem size otherwise the solution will be exponential as before.

---
What is the coin changing problem? #flashcard #IADS #DynamicProgramming 
	In this problem we are given some set of coin denominations and a total amount. We need to find the least number of coins to make the sum. We return a multiset of the original set of coins.

---
What insight allow a recursive relation and hence a dynamic solution to the coin change problem? #flashcard #IADS #DynamicProgramming 
	We know our solution will be another solution (down to 0) plus some coin. So we can loop through all coins and check if the subproblem for our value minus that coins value has the least number of coins. If it does then we add that coin onto the solution and we get our new solution.

---
How can the Fibonacci numbers be calculated dynamically? #flashcard #IADS #DynamicProgramming 
	For some $n$ Fibonacci number we make an array of size $n$ then in each $i$ spot we calculate $Fib(i)$. Since the Fibonacci relations is $Fib(i)=Fib(i-1)+Fib(i-2)$ we can just use the last part of the array.

---
What is seam carving? #flashcard #IADS #DynamicProgramming 
	A seam is a line of pixels running from the top to the bottom of an image. Each row has one pixels chosen and the distance from row to row only varies by 1. In seam carving we are given some score of a seam we need to maximize.

---
How can seam carving be implemented when minimizing a summed score for each pixel? #flashcard #IADS #DynamicProgramming 
	We can keep an array of the best seam up that end in some pixel. Then the best seam for any pixel will be the min of the best paths up to that pixel. So we can build the solution by summing over and over the edges.

---
What is edit distance? #flashcard #IADS #DynamicProgramming 
	Edit distance is a way of measuring the distance between two strings. We count an edit as adding, deleting or changing a character (substitution).

---
What is string alignment when it comes to edit distance? #flashcard #IADS #DynamicProgramming 
	Two strings can be merged by a number of edits (insert, delete, substitute). The optimal string alignment is the sequence of least edits merging the two strings.

---
How can edit distance be made into a recursive problem? #flashcard #IADS #DynamicProgramming 
	We can consider the edit distance between the substrings of a string as any edit with either end in the last character of both (if they are the same) and if they are different it could be an insert at the top, at the bottom or a substitution.

---
What is the all-pairs shortest path problem? #flashcard #IADS #DynamicProgramming 
	The all-pairs shortest path problem relates to a weighted graph. A path from $v$ node to $u$ is a series of vertices $[e_1...e_{|p|}]$ such that $e_1$ comes from $v$ and $e_{|p|}$ ends at $u$. We want to generate every path to every other node such that the sum weights over all these edges is minimized.

---
What is the main idea behind the Floyd Warshall algorithm? #flashcard #IADS #DynamicProgramming 
	The main idea is we only allow a restricted set of vertices to be used to find paths. We can then grow this set one at a time comparing the old path between two nodes with this new node in between or the old path without. Overtime this updates all the paths between any vertices to work with the most efficient one.

---
What four properties do we need to consider a dynamic solution to a problem? #flashcard #IADS #Graphs 
	1/2. We need to be able to break down a solution into smaller problems of the same type. We need a recurrence relation breaking larger instances in to smaller ones
	3. We need to be able to organize the results for the subproblems in a polynomial bounded amount of space
	4. We need an algorithm that controls the order of the subproblems solved such that we have computed many results we need in advance and so can take advantage of our recursion.

---
