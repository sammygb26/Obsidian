What is a major problem with standard PCFG syntax parsing? #flashcard #FNLP #DependencyParsing
	In standard PCFG syntax parsing we loose the word meaning after the first layers as POS tags preside over many words. This means when parsing no information about the words is used to change the likelihood of different parsing. But this *isn't how humans parse* as words are used to resolve ambiguity in the syntax tree.

---
What is lexical head form? #flashcard #FNLP #DependencyParsing 
	In lexical head form for each non-terminal we augment with the **head word** which is considered to lead the phrase. This brings up the most important element of the phrase to be used for probabilistically parsing.

---
What are some issues with lexicalizing? #flashcard #FNLP #DependencyParsing 
	The problem is we have **category-splitting** and the size of our grammar explodes. This leads to very sparse data.

---
What techniques can be applied to overcome the issues with lexicalization? #flashcard #FNLP #DependencyParsing 
	We can apply complex smoothing techniques to improve the quality of the counts. Then we can also learn subcategories so avoid using all possible subcategories.

---
Can you give an example moving from a lexicalized constituent tree to a dependency tree? #flashcard #FNLP #DependencyParsing 
	If we start with a constituency tree we can first remove all the phrase tags. Then we remove duplicates (unary extensions $S\to S$). We even do this if the tree splits. This means every word is given only once and the relations denote words in the category that aren't the head word.

---
What does a dependency parse capture? #flashcard #FNLP #DependencyParsing 
	A dependency parse gives the direct relations between word without worrying about the grammatical structure that would generate those words. It can also capture relations between words.

---
In a dependency parse what is the different between using content heads or functional heads? #flashcard #FNLP #DependencyParsing 
	When **content heads** are used the head word becomes the content words (open class). Then when functional heads are used functional words becomes the head (closed class).

---
What is the difference between content words and functional words? #flashcard #FNLP #DependencyParsing 
	Content words generally have a lot of semantic meaning like of Nouns and Verbs but functional words convey grammatical meaning for example Determiners and Conjunctives.

---
How are edge labeles used in dependency parsing? #flashcard #FNLP #DependencyParsing 
	Edge labeles are uses to specify the relationship the head word holds to the dependents. For example direct objects, preposition etc.

---
How is a dependency parse defined as a graph? #flashcard #FNLP #DependencyParsing 
	We define a dependency parse as a graph $G=(V,A)$ where $V$ is the set of words (possibly containing punctuation or *morphemes*) then $A$ is the set of arcs pairs of elements in $V$.

---
In a dependency tree what properties are upheld on the graph which defines that specific parse? #flashcard #FNLP #DependencyParsing
	For a dependency graph the tree must 1) Have a single root node with no incoming arcs 2) With the exception of the root node each vertex has exactly one incoming arc. 3) There is a unique path from the root node to each vertex in $V$.

---
What is a dependency path between two words when it comes to informational extraction? #flashcard #FNLP #DependencyParsing 
	When it comes to informational extraction a dependency path is the sequences of words connecting two words in the dependency parses graph. This is useful for extracting semantic meaning between words.

---
When is a dependency parse arc projective? #flashcard #FNLP #DependencyParsing 
	A dependency parse arc is projective when there is a path from the head to every word between the dependent and the head. This is the case when no arc crosses this arc. This would give an island of words which cannot be reached from the head.

---
When is a dependency parse projective? #flashcard #FNLP #DependencyParsing 
	A dependency parse is projective if all arcs in it are projective. That is it can be written with no arcs crossing.

---
What are the rules called which describe which word is nominated to label a phrase? #flashcard #FNLP #DependencyParsing 
	These are called **head rules**.

---
How do head rules define a conversion from a constituency tree to a dependency tree? #flashcard #FNLP #DependencyParsing 
	Head rules define which daughter is selected to be the head for a given phrase. That is as in the **lexical head**. Once lexical head are given the phrase categories can be removed and the words collapsed to give a dependency tree.

---
How is a head rule defined? #flashcard #FNLP #DependencyParsing 
	A head rule is defined for a production rule in our grammar. For example $VP\to V\space NN$ could have a head rule $VP\to\underline V\space NN$ which would mean the head of $V$ becomes the head of $VP$.

---
How does CYK work out when it is applied to direct parsing? #flashcard #FNLP #DependencyParsing 
	When CYK is applied to direct parsing the runtime generally gets worse. This has the step of making a while constituency tree in the middle. However instead we can perform **direct parsing** to get the dependency parse first without the constituency tree.

---
What is the idea behind a shift-reduce parses for dependency parses? #flashcard #FNLP #DependencyParsing
	Shift-reduce is algorithm originally created for parsing programming languages. In general a stack is grown from a buffer with *shift* then we perform *reduce* operations to consume the stack and we emit relationships between the elements we are combining. But the relationships can be dependency relationships and we can consume a sentence.

---
What is the architecture of transition based parsing? #flashcard #FNLP #DependencyParsing
	We will have an **input** buffer and a **stack** these make up our *configuration*. The parser's job is to consult an **oracle** which decides which operation to perform to navigate between configurations.

---
What are the operations given for transition based parsing (arc standard)? #flashcard #FNLP #DependencyParsing 
	We have **left arc** which removes $s_2$ and makes add as arc $s_1\to s_2$. Then we have **right arc** which removes $s_1$ and makes an arc $s_2\to s_1$. Finally we have **shift** which adds a new element from the buffer to the stack. 

---
What constraints exist on when shift-reduce operations can be performed when performing transition based parsing? #flashcard #FNLP #DependencyParsing 
	When we perform transition based parsing the constraints will be that an Left arc cannot be made into the root then the parser must end with an empty stack and buffer.

---
What is a limitation in the type of dependency structure a transition based parser can produce? #flashcard #FNLP #DependencyParsing 
	One limitation is an **arc standard** transition based parser can only generate projective dependency parses. Ones with more operations can operate on the "stack" in more complicated ways allow non-projective parses.

---
What is the runtime of transition parsing and why isn't it exponential? #flashcard #FNLP #DependencyParsing 
	In transition parsing we have an "oracle" which gives hopefully the best choice at each time step. The oracle may not always give the best action and there may be multiple actions but we do not worry about this and simply perform a **greedy** optimization.

---
What is graph based dependency parsing? #flashcard #FNLP #DependencyParsing 
	In graph based dependency parsing we consider all the possible edges between nodes and select the best ones to form our tree. The runtime can generally be around $O(n^2)$.

---
How is the oracle trained for dependency parsing for a transition parsing approach? #flashcard #FNLP #DependencyParsing 
	Generally we can train the oracle via supervised learning which then gives a good performance.

---
