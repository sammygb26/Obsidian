What is the goal of LL(1) Predictive Parsing? #flashcard #IADS #LL1PredictiveParsing
	The idea is to have a $O(n)$ way of paring a sequence for its grammar tree (instead of $n^3$ which may take far too long). This could be for parsing a program for example.

---
What do we do in predictive parsing using a leftmost derivation? #flashcard #IADS #LL1PredictiveParsing 
	We know what symbol our expansion starts with. We are trying to just by looking at that guess how it fits into a grammar tree. We build a prediction of the remaining statement (sentential form it must fit into). This also gives us the current non-terminal we are in an expansion of.

---
What makes a language an LL(1) language? #flashcard #IADS #LL1PredictiveParsing 
	This is when we can guess the correct grammar for the rest of a the sentence given only the current node and the non-terminal we are currently expanding.

---
What is a parse table? #flashcard #IADS #LL1PredictiveParsing 
	This is a description of what expansion to perform given the current non-terminal being expanded and the next terminal in the sequence. Without this we cannot use LL1_Parse.


---
How does the LL1_Parse algorithm work? #flashcard #IADS #LL1PredictiveParsing 
	We always keep a stack of the remaining non-terminals that need to be expanded and terminals that need to match our tree. Then whenever we find a terminal we match it with the next element in our phrase (if it doesn't match we have an error), we can not move to the next character in our phrase. If we have a non-terminal we need to look up its expansion in the parse table and then add this expansion to our stack (if there is no expansion we also have an error). By the end the stack should be empty and we should match the empty string to the final non-terminal.

---
