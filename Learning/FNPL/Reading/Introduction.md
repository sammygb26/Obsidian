What is natural language processing? There are many facets to this area, it deals with how we get machines to understand natural language. We may want to build **conversational agents** than can communicate with us. We may want to **recognize speech** or **generate speech**. One area with vast implications is **language translation** which would allow us to bridge the gap between the different people of the earth.

### Knowledge in Speech and Language Processing
NLP system are define by their *knowledge of language* and it separates them from regular language processing. We can examine what a system might need. Take HAL from 2001: a space odyssey. It will require understanding of  **phonetics and phonology** in order to pronounce words and parse speech. Understanding words like "can't" and "isn't" requires an understanding of **morphology**. The order of words must be understood and the reasons for this are **syntax**.

If we want to give answers to questions we need to understand what is being asked. We would need an idea of **semantics**. Both **lexical semantics** (the meaning of words) and **compositional semantics** (how words come together to for a meaning e.g. "Western Europe" what is it how it is different from "Western" and "Europe", how is it the same).

Being an agent with language means understanding how to manipulate it. For example being *polite* "I'm sorry" or hiding behind language "I can't" vs "I won't". The use of the words here requires **pragmatic** or **dialogue** knowledge.

**Discourse** is also required where sentences refer to previous ones or ones not spoken by the current speaker. It must understand the different parts of the speech that go into how we understand the information format of language.

### Ambiguity
Most linguistic tasks can be viewed are resolving **ambiguity** (meaning there are multiple possible meanings). These meaning track down to the different variables we can use to the describe the world having multiple possibilities. For example **parts of speech tags** may have many possibilities for a word. Words may have many possible meanings. Then the different constituents in the sentences can be grouped together in different ways and their mapping to each other can be different.

### Models and Algorithms
Language can be modeled in many ways using **state machines**, **rule systems**, **logic**, **probabilistic models** and **vector-space models**. These models can be mastered with a small numbers of algorithms. Like **state space search** algorithms using DP techniques and machine learning algorithms like EM and classifiers. States evolving can be modeled by FSMs and FSTs.

There are also **declarative models** such as CFGs and regular grammars. Logics tools like **predicate calculus**, **FOL** and lambda calculus can be used.

Probabilistic modeling can also be done with **Markov models** and **Hidden Markov Models**.

### Language, Thought and Understanding
To actually solve this problem of NLP we will have to pass the **turing test** and create AI that can truly reason and interact with the world.