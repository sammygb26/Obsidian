# Small Circuits
We have seen how information travels from the *dendrites* to the *soma* where it is integrated finally down the *axon* if an output is decided to be sent. This is called the **neuron doctrine**. On its own a neuron cannot function however. Instead our nervous system work by having neuron *interconnected* with each other and not in *isolation*. There are many types of these circuits and they can be *small* or *large*, have types like sensory or motor, peripheral and central. They also have many specific function like fear or memory. Each circuits functions in the same way a neuron does in the neuron doctrine listening, integrating and deciding to act or not. The types of input matter a lot (excitatory or inhibitory), the *location* of the signal (distance form the soma). It also matters the *proximity and frequency* for signals as closer more frequency excitatory signals will increase the change of an action potential being fired. Signals can also be *blocked* by inhibitory signals.

### Information Processing
Single neurons rarely take in only a single type synapse as we have explored in [[Fundamentals of Neuroscience/Excitation and Inhibition]] and [[The Synapse]]. Instead many neurons are interconnected taking many *excitatory* and *inhibitory* inputs form many neurons. Generally **excitatory** synapses occur on the *dendritic spines* while **inhibitory synapses** exist on the *dendritic shafts*, *soma* and *axon initial segment*.

![[Pasted image 20220528123917.png]]

Each neuron can take in many *thousands* of synaptic signals and has to integrate them all. But what rules govern how these signals are integrated. At this point five different factors have been found to influence this.

### Synaptic Efficacy and Distance
Here we will look at a key factor in the efficacy of a synapse in influencing the firing of an action potential: the **distance** between the synapse and the cell body. We say in [[Passive Membrane Properties]] the *length constant*. Where $\lambda=\sqrt{\frac{R_{membrane}}{R_{axial}}}$. Where the top is $\Omega\cdot mm$ and the bottom is $\Omega/mm$.

![[Pasted image 20220528125515.png]]

The more **length constants** away a signal is the weaker the PSP will be. The creator the $R_{axial}$ resistance is (which is how much the cytoplasm resists current). The more will be lost on the way to the *soma*. The $R_{membrane}$ describes how hard it is for current to move across the membrane so the greater this is the less will be lost on the way to the *soma*. So the closer EPSP will have traversed less  $\lambda$s hence is greater. Another reason for the effect is the **shape** of the neuron. The processes further away are usually smaller than those closer just like branches of a tree. But a thinner process has a greater $R_{axial}$ hence the reduction is even greater than expected.

All other things being equal the further away a EPSP is from the *soma* the less of an effect it will have on the firing of an action potential.

### Synaptic Summation
When we stimulate two excitatory synapses equally far from the cell body and with the same shape of dendrite. 

![[Pasted image 20220528132245.png]]

The EPSPs generated will stimulate the same response in the potential at the soma. When we stimulate them *together however* we will see **synaptic summation** where the signal seen is larger than the two individual EPSPs. However its isn't strictly double instead it is a *non-linear summation*. There are many possible causes for this:

1. *Driving Force* - this is as we know driving force is affected by the membrane potential. Hence if some other EPSP is changing the membrane potential this will change the driving force and so the difference ions will change the membrane potential differently creating a sub-linear effect.
2. *Dendritic Action Potentials* - It has been found that voltage-gated channels and even action potential in dendrites might exist. This can create a wide array of non-linearities.
3. *Action Potential Back propagation* - The soma can have current conducted back from an action potential up to the dendrites thereby affecting signals coming in.

### Synaptic Inhibition
In the previous example both signals for excitation and inhibition were used. But as noted in [[Fundamentals of Neuroscience/Excitation and Inhibition]] both *excitation* and *inhibition* are important for brain function. So how does inhibitory signals affect brain function.

![[Pasted image 20220528133807.png]]

If we trigger an action potential at the *green* excitatory synapse we will see the familiar spike at the soma caused by the EPSP. But the *purple* inhibitory neuron will have no clearly visible effect on the soma membrane potential. This is due to *inhibition* being performed by opening *chloring channels*. Chlorine's **Nernst Potential** is close to the **resting potential** therefore only a small effect or no effect can be seen. When both are stimulated together no change is observed. They both produced the same changes in *membrane conductance* but any effect from the excitatory neuron is canceled out by the inhibitory one. This is **shunting** as described in [[Fundamentals of Neuroscience/Excitation and Inhibition]]. It is another example of of a non-linear summation.

The placement of an inhibitory synapse is also important for signal processing. An IPSP on the soma will have *wide ranging* inhibitory affects on all EPSPs arriving at the cell. While an IPSP on  the dendritic branch will only shunt EPSPs *upstream* in the dendritic arbor while leaving downstream potentials.

### Synaptic Temporal Summation
We have looked at what happens when different synapses are stimulated at the same time. But what about if a synapse is stimulated many times in rapid succession. Here we will get **Synaptic Temporal Summation**. When a single EPSP is triggered from a synapse it will have the same effect as before. But if multiple are triggered in closer succession they will sum up in a similar way to in regular **summation**. This can even trigger an *action potential* all on its own. The summation is caused by the same signal piggybacking of the still activated receptors allowing for the effect to be larger as more receptors are active.

### Synaptic Temporal Inhibition
This is the effect of the **shunting** from IPSPs when we look over time. We can see that *shunting* works to reduce any signal to resting that it can inhibit while acting. This way even two signal happening together can be canceled out and the effect of *temporal summation* is canceled out as inhibition happens in between excitation.

### Convergence, Divergence and Recurrence
We have looked at the factors that affect the strength of the interactions between synapses on the dendritic arbor of a post synaptic neuron. But *why* do we want all these inputs coming into one neuron at once. This is still being explored but there are common **motifs**. Three of the basic principles are:

1. **Convergence** - This is when multiple potentially disparate inputs come to just one downstream neuron. This happens through much f the nervous system. This makes sense we being together many scraps of information and we synthesis them into a whole. This is important to sensing danger like combining seeing a movement with rustling.

	![[Pasted image 20220528141859.png]]

2. **Divergence** - This is when from one place a signal can spread out to many parts of the body and brain. Again when we sense danger as an example we many need to flee. Hence many parts of out brain will be activated to move, plan and balance.

The tall grass example take in many neurons and doesn't truly converge to one place. Instead we could consider a classic example the **stretch reflex** or the **myotatic or tap reflex**. This is where the doctor taps your knee and in response our leg kicks out. The stretching of muscles sends out signals into the spinal chord where it converges to a single motor neuron. This Then causes a divergent to activate one muscle and relax another causing your leg to kick out.

### Central Pattern Generators
3. **Recurrence** - This describes the situation where some chain of connected neuron loops back on itself. This can also be called *feedback*. To A may connect to B and B back to A. These connections can be excitatory and inhibitory and a wide range of computations can be done by this. A common small circuit motif that uses recurrence is **Central Pattern Generator** (CPG). These can create rhythmic patterns of output even without sensory input. Like the swimming of a fish.![[Pasted image 20220528143056.png]] Many seemingly complex actions we take like waling are performed by CPGs outside of the brain. In humans this can be done in the spinal chord alone. There are many ways this can happen in *nature* for example some neurons have properties making them fire rhythmically. But **recurrence** is a key feature to many of these systems. In the simples cast A connects to B and B to A. But A may take some time to activate B as the signal travels down the axon. The same happens to A so over time with proper tuning this cycle can repeat indefinitely. So from this we can generate almost any pattern. We may also *modulate* this patter from outside sources. Slowing it or speeding it via modulators or stopping and starting it (stop and start running).

[[Small Circuits Questions]]

