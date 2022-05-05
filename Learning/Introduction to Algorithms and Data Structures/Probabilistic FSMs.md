# Probabilistic FSMs
The Viterbi algorithm find the most likely route through a probabilistic FSM for a given output string.  A deterministic FSM has no choice in path, a non-deterministic FMS has choice or multiple possible paths for the same string and a probabilistic FSM has only chances of going to given states given an input value.

## Finite State Machines
There are [[Deterministic FSM]]s and [[Non-Deterministic FMS]]s to recap they have a set of states $Q$, an alphabet $\Sigma$, a distinguished start state $q_0$ and a subset $F\subseteq Q$ of accepting states. Then for **deterministic** FSMs there will be a transition function $\delta:Q\times \Sigma\to Q$. So the parts of a **deterministic** FSM are $M=\langle Q,\Sigma, q_0, F, \delta\rangle$ we can then test if a string is accepted by the FSM.

In a **non-deterministic** FSM the states ad the alphabet will be the same however there will be a transition function $\Delta:Q\times\Sigma\times Q$. Hence a **non-deterministic** FMS will be $M=\langle Q,\Sigma,q_0,F,\Delta\rangle$.

## Probabilistic FMSs
A **Probabilistic FSM** is a finite-state machine of the form $M=\langle Q,\Sigma,q_0,F,\Delta\rangle$ with $\Delta\subseteq Q\times\Sigma\times Q$, also with a probability label $p_{q,a,q'}\in[0,1]$ for every $(q,a,q')\in\Delta$ (so $a\in\Sigma$ and $q\in Q$). Not that the probability for reaching each $q'$ coming out of some $q$ will sum to 1.
$$
\sum_{q'\in Q, (q,a,q')\in\Delta}p_{q,a,q'}=1
$$
In this case the **probabilistic FSM** has a given change of accepting some string.

[[[Probabilistic FSMs and Viterbi Questions]]