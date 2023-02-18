This gives a hierarch of *turing machines*. We are ranking these machines on what sort of algorithm we can count. For example we might ask if machines can work in a maximum part of RAM. Or are there special cases for memory that can only be able to work at the top level of a stack. Or at the most extreme no memory is needed at all. In general this hierarchy was given by looking at different levels of complexity in grammars for generating languages. Another important things is [[Deterministic FSM]]

In general there are 4 types given as:

1. **Type 0** is known as unrestricted grammar (Recognized by Turing Machine). These are completely unrestricted and cannot be described by natural languages or grammars.
2. **Type 2** is context sensitive grammar (accepted by linear bound automata, meaning bounded memory needed). Here rules have the form $\alpha A\beta\to \alpha\gamma\beta$ with $A$ as a non-terminal and $\alpha,\beta,\gamma$ as strings of terminals and non-terminals. Stings $\alpha\beta$ may be empty but $\gamma$ must be nonempty.
3. **Type-2** Context free Grammar (Accepted by Push down automata, stack of memory). Probable the most important category where rules take the form $A\to\beta$, where $A$ is a single non-terminal symbol and $\beta$ is a string of symbols.
4. **Type-3** regular grammars (accepted by finite automata). These must have a single non-terminal on the LHS and a RHS consisting of a single terminal or single terminal followed by a single non-terminal.

![[7090.1571152901.jpg]]

### Languages
A language (which this hierarch is based around the parsing of) is medium for communication. It has two basic element **syntax** (grammatical rules) and **semantics** (meaning). Some languages also take into account a third factor which is *context of usage*. The complexity in the grammar of the language defines its place in the Chomsky hierarchy.

![[Pasted image 20230217224010.png]]

### Type 3: Regular Languages
These cannot handle entire languages as the production rule are too restrictive. Constructs describable by REJEX exits here.

These languages can be parsed by FSMs. These don't require any memory to parse their actions. Their current state is all that matters previous states don't.

### Type 2: Context-Free
These can handle **nested dependencies** like for example in English having if then statements.

These can be parsed by **push-down automata** that is a one ended memory stack is required to parse all cases. For example this may consist of a map of the depth within the language we reside.

### Type 1: Context Sensitive
Here the production rules cares about context. These rely on a context around some non-terminal to expand lower. Hence these allow a replacement if some set of previous actions in memory is reached.

A **Linear-Bounded Automata** is a form or restricted Turing machine which instead of being unlimited is bounded by some computable linear function. These have an upper limit on RAM usage making them interesting to talk about.

### Type 0: Unrestricted Grammar
Type-0 grammar include all formal grammar. These languages are recognized by turing machines and are know as the **Recursively Enumerable Languages**. If we have a set of variables $V$ and a set of terminals $T$.

These may be incomputable but can still be represented in a turing machine. That is control may be finite even if data is infinite.

