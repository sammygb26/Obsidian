What is a knowledge base? #flashcard #RA #LogicalAgents
	 A knowledge base is a collection of knowledge our agent has acquired about the world. It can use this to infer new knowledge about the world and selection actions to take.

---
What are the key features of a knowledge based agent? #flashcard #RA #LogicalAgents
	A knowledge based agent needs to be able to represent the environment stats in some way this is in order to have a representation of the environment. It need to be able to incorporate new information it has perceived into its representation of the world. It needs to be able to deduce hidden properties of the world. It also need to be able to deduce appropriate actions form the representation it has.

---
What are logics and how are they used for knowledge based agents? #flashcard #RA #LogicalAgents
	Logics are formal languages that the agent can use to represent information it has gleamed about the world. Syntax defined the sentences we can make and semantics define what this actually means for our world. So we can use Logics to represent our knowledge of the world.

---

What is entailment? #flashcard #RA #LogicalAgents
	Entailment is when we have a knowledge base we can deduce some statement to be true since in every possible environment for which our knowledge base is true this sentence must also be true.

---

What are models? #flashcard #RA #LogicalAgents
	Models are representation of the state of our environment. A model can either be true of false. Meaning it is either a correct representation of our environment or it isn't there is no middle ground.

---

How can we build up a better and better model of the world? #flashcard #RA #LogicalAgents
	If a model can either be true of false in a world. Then models either have the possibility of being true given our knowledge or they are always false. So as we continue to update our knowledge base we add more logical sentences to it restricting models that are valid. The ones that are left have more detail are are so more useful to us.

---

What is the model of a knowledge base or sentence? #flashcard #RA #LogicalAgents
	The model of a knowledge base/sentence is the set of models that can be true in which that sentence is also true.

---

How can we use models to see of a knowledge base entails some sentence? #flashcard #RA #LogicalAgents 
	If the model of our knowledge base is completely a subset of the model of a sentence then that sentence must be true in our knowledge base. That is since for all possible models given our knowledge base the sentence is already true. Then if it isn't true for one of them then it might not necessarily be true for the true model the environment.

---


What is an inference procedure? #flashcard #RA #LogicalAgents
	An inference procedure is a way of finding/deriving new logical sentences given our knowledge base.

---

What does it mean for an inference procedure to be sound? #flashcard #RA #LogicalAgents
	 An inference procedure is sound of all the sentences it infers from a knowledge base are also entailed by that knowledge base.

---

What does it mean for a inference procedure to be complete? #flashcard #RA #LogicalAgents
	This means that for every sentence that can be entailed form a knowledge base it will also be inferred by our inference procedure.

---

How can propositional logic be used as a logic? #flashcard #RA #LogicalAgents
	We can use propositional variables to represent details about our environment. Then our knowledge base will be the conjunction of all the sentences we have perceived or inferred.  We can do a check through all the possible combination of the symbols and check if our knowledge base being true infers said sentence. If so we know our knowledge base entails it and we can infer it.

---
What is a valid sentence? #flashcard #RA #LogicalAgents
	A sentence is valid if it is true in all models.

---

What is a satisfiable and unsatisfiable sentence? #flashcard #RA #LogicalAgents
	 A sentence is unsatisfiable if is is true in no models and satisfiable if it is true in some models.

---

How is satisfiability related to inference? #flashcard #RA #LogicalAgents
	If the sentence that the knowledge base is true and the a sentence is not true is unsatisfiable. This means it can never be true hence if our knowledge base is true this sentence must also be true.

---
