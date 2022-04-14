# Context-free languages and Grammars
This is part of **language processing** which can be either processing **artificial languages** (like Java, Python etc.) or **natural languages** like English, Greek etc. For artificial languages we are converting a text file into actual code we can execute. For natural languages it can go from generating language from a computer, parsing requests form a person or translating languages. Despite these differences both do have similarities. One part of this is **generative grammar**. This field was brought into the modern world by Noam Chomsky. We will cover a theory called **context-free grammars**.

## Syntax Trees
A syntax tree displays the grammar based structure of a text. For example take the structure of the python statements x2=-x1 and the English sentence The sun shone
![[Pasted image 20220203131948.png]]
Constructing these trees that explain the meaning of the sentences is important for many tasks. For example to process the python we will need to evaluate the expression. A **grammar** for a language are the rules that describe the possible syntax trees. Constructing the tree from the sentence is called parsing.

There are two types of symbols in a tree the **leaves** and the **branches**. The leaves make up the actual language and cannot be divided further they are called **terminals**. Then the branches in the internal nodes which describe the structure are called **non-terminals**.

## Arithmetic Expressions
We can make a small example with arithmetic expressions. Some examples of this language will be
![[Pasted image 20220203132641.png]]
To define a language we need a list of all the **terminals** and **non-terminals** then we need rules to describe the tree structure.

**Terminals** -> +,* , (,), x, y, 0, … 9
**Non-terminals** -> Exp, Var, Num
We also need to designate the **non-terminal** Exp as the **start symbol**.
**Rules**: 
	Exp -> Exp + Exp
	Exp -> Exp * Exp
	Exp -> Var | Num | (Exp)
	Var -> x | y | z
	Num -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

The rules describe what the children of a *non-terminal* can be.
![[Pasted image 20220203133146.png]]
We need to have all **non-terminals** expanded to **terminals** to have a correct expression. The above expression would be $5*(x+3)$ which can be found by reading along the border of the tree. We can generate infinitely many trees by making difference choices for the **non-terminal's** children. All the possible strings defined are called the **language** of the grammar. Another way of doing this is expanding the **non-terminals** written down.
![[Pasted image 20220203133621.png]]

## Structural Ambiguity
We can generate the same text from multiple trees. Take $1+2+3$ we can generate it multiple ways
![[Pasted image 20220203133744.png]]
This can actual matter if you take more complex instructions like $1+2*3$ giving us either $7$ or $9$. A **grammar** is **ambiguous** if we these types of trees exits. In computer languages, we take care to make sure there isn't structural ambiguity by enforcing rules. For example in computer languages we follow BODMAS rules for example. But in **natural** languages we cannot enforce these rules. Take *"I saw a man with a telescope"* does the man have the telescope or are we looking at him through a telescope. The way we get around this is we take the most probable solution.

## Comma Separated lists
Take the following language with characters followed by commas in lists.
![[Pasted image 20220203134357.png]]
We use $\epsilon$ to mean no string it isn't actually part of the language. We would have the terminals $\epsilon|a...z$ and the non-terminals List, Char, Tail with List being the start symbol. Then Char goes to a character $a|...|z$. Then we have the rules 
![[Pasted image 20220203134703.png]]
The difference here is we can have lists and tails with nothing as its child. For example we could have
![[Pasted image 20220203134745.png]]
The Tail symbol has no child.

## Mathematical Definition
![[Pasted image 20220203134852.png]]
Disjoint means there can be no terminal that is a non-terminal. The rules are called **productions** and take a symbol from the **non-terminals** and produce something from either the **terminals** or **non-terminals** or nothing ($\epsilon$).

A **sentential form** is any sequence of terminals and non-terminals that can appear in a derivation starting from the start symbol. This is the set derivable from $G$ is the smallest set $S(G)\subseteq (N\cup\Sigma)^*$. The **language** associated with grammar is the set of sentential forms that contain only **terminals**. A language is **context-free** if there exist some CFG such that $L=L(G)$. A language is **context-free** if the rules apply no matter where $X$ occurs. But **context-sensitive** grammars expansion rules depend on the locations of the $X$. CFGs allow arbitrarily deep nesting.
![[Pasted image 20220203135756.png]]
Languages like this can often be used to describe languages. This is often called BNF (Backus-Naur Form).

## Natural Languages
![[Pasted image 20220203140028.png]]
These might be the 'parts of speech'  of English this could give the sentences
![[Pasted image 20220203140231.png]]

[[Context-free Languages and Grammars Questions]]