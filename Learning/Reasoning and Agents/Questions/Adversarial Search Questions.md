What problem does adversarial search solve? #flashcard #RA #AdverserialSearch
	Adversarial Search solves the problem of opponent based multi-agent systems. We cannot build a complete set of actions that will beat an opponent as we do not know what the opponent will do they are unpredictable. Instead we need a way of finding the best solution to what the opponent does.
	
---

What is the idea behind the minimax algorithm? #flashcard #RA #AdverserialSearch 
	The idea is we know our opponent will try to pick the best choice of action every move. So we should assume they are picking the best move and chose the move that ensures we give them the worst options of moves.

---
What is the minimax utility function of a state? #flashcard #RA #AdverserialSearch 
	Each node in our search tree is either a MAX node or a MIN node. These are the two hypothetical perfect agents each trying to minimize or maximize the utility function respectively. So we a MAX node will have the max utility of the minimax value of the actions MAX can take at that node. Then for a MIN node it will be the opposite. Then the minimax value of a Terminal State will simply be the utility of that state.

---
How does the minimax algorithm work? #flashcard  #RA #AdverserialSearch
	The minimax algorithm works by having us choose the action leading the the node with the best minimax utility. So we split the search space into layers of MIN and MAX nodes. The search then involves backpropagating up all the values from the terminal states to help either MIN or MAX understand what the best move to make is.

---
What are the properties of the minimax algorithm? #flashcard #RA #AdverserialSearch 
	It is complete since if the tree is finite it will always pick the best action. It has time complexity $O(b^m)$ for each move since it has to explore all the way to the bottom of the tree. But it does have space complexity $O(bm)$ since we can use a depth first approach.  It is also optimal since with a perfect opponent we will always pick the best moves.

---
What is the idea behind alpha-beta pruning? #flashcard #RA #AdverserialSearch 
	While exploring node we can keep track of the best action to far we have found. Then if we pass this on to our child nodes they will know if they are ever going to return a value that will be less that this (as perhaps Min has found a value smaller) then we can stop knowing this value will never matter as we ill never go down this path. Since even if we don't find any better paths we already have one so will never choose a path leading to this choice. The same is done for min and max values giving us $\alpha$ and $\beta$.

---
How does the minimax algorithm deal with limited resources? #flashcard  #RA #AdverserialSearch
	We use alpha beta pruning along with only going to a certain depth then from this depth we estimate the utility with an evaluation function. 

---
What is the standard form of an evaluation function? #flashcard  #RA #AdverserialSearch
	 The standard for of an evaluation function is a weighted sum of given features of the state. This assumes all the features are independent in value however doesn't take into account that pieces might be more valuable at different points in the game.

---
What is the **horizon effect**? #flashcard  #RA #AdverserialSearch
	This is the idea that a minimax plater will attempt to just delay bad outcomes as if it pushes them over the horizon of vision into the heuristic realm then it wont have to deal with them. This is a flaw in their reasoning.

---
What are some optimizations that can be made to adversarial search? #flashcard #RA #AdverserialSearch
	The main one is **alpha-beta** pruning. Another way is storing transpositions in a transposition table so if we run across the same move we can use the minimax move we have already looked up.

---
How does **alpha-beta** pruning interact with iterative deepening search for greater performance? #flashcard #RA #AdverserialSearch
	Alpha-beta pruning works best when we pick the best outcomes first, this way the most pruning is done. With iterative deepening the previous best choices according to minimax can be used to guide alpha-beta pruning this takes away the blunt cost of doing alpha beta pruning.

---


---
