# Passive Membrane Properties
We have seen the membrane potential before and it will be modulated to send signals. Before this will will have to expand on the *steady state* [[Resting Potential]] that is achieved if we allow the system to run until there is no longer a change in state. We will first need to look at the passive properties of the membrane.

## Resistance and Conductance
This describes how much a conductor resists a flow of charge (current $I$). Conductance is the inverse of this so a low resistance wire has a high conductance. Resistance is measured in OHMs $\Omega$. The ion channels in a membrane have their own resistance that is lower with more channel permeability and number of channels. Resistance in neuroscience is usually measures in $\Omega/mm$. We can also talk about the resistance of the cytoplasm in between cells. 

There are two quantities we care about when it comes to resistance. **Membrane resistance** the resistance to the flow of ions across the membrane. **Axial resistance** the resistance to the flow of ions down the axon.

## Capacitance
We have seen in a neuron that a layer of insulator separates on one side negative and on the other positive charges. This arrangement is the same as a capacitor in electronics. There are two conductors which are separated by a insulator called a dialectic. A capacitor works to store charge. The capacitor itself builds up a voltage across it opposite to that applied to it this takes some time and when the charge is released it slowly returns to normal. The capacitor buffers the change in voltage.

The capacitance refers to the ability of some capacitor to store change. There is also how thick the insulator is which describes how quickly the charges will build up. So thicker is slower hence thicker membrane would make for a slower buildup and release of charges.

## Current and Ohm's law
This describes the relationship between voltage, resistance and current. It is $$
I=\frac VR$$That is current equals voltage over resistance. This means the voltage is linearly related to current. This all comes to matter when we consider the the rate at which the membrane potential changes will depend on how quickly charge is flowing or how much current there is. In the same way it is inversely related to resistance. Current itself is just a change in charge over time so $\frac{dC}{dt}$

In a real cell we want to think about two resistances to understand how current flows. The flow across the membrane and the flow along the axon to send signals. These are controlled by their respective resistances $R_{\text{membrane}}$ and $R_{\text{axial}}$.

![[Pasted image 20220511184450.png]]

We have thought about membrane potential as being the same everywhere in the neuron and this is true more or less for a neuron at rest. To induce a current however the potential shifts along the axon. 


We can first think about what a single change in voltage at a point would to a neuron. The whole neuron is electrically connected so a change in one place will affect the others. 
![[Pasted image 20220511185457.png]]
This is described by the *length constant* which is around where 36% of the potential is lost. $$\lambda=\sqrt{\frac{R_{\text{membrane}}}{R_{\text{axial}}}}$$We can think of the voltage leaking out when there is high membrane potential and being resisted when there is high axial potential forcing it to take the membrane way out instead. This makes sense when we consider voltage is like charge pressure.

![[Pasted image 20220511185840.png]]

## Capacitance and Myelin
Capacitance describes how much charge a capacitor can store. With more capacitance therefore our membrane potential changes slower. That is with low capacitance our potential becomes more responsive and fast while with high capacitance it is more sluggish. The capacitance itself depends on the material of the diametric in this case the material of the cell membrane. The material (membrane) with a high dielectric constant (todo with how easily the material is polarized) with have a higher capacitance. The thickness of the dielectric layer will also affect capacitance. A thicker layer will have lower capacitance. To increase capacitance and therefore responsiveness some axons develop a layer of Myelin that decreases capacitance.

Just as we have defined the length constant we can also define the time constant $\tau$. This is the time taken to charge a membrane to around 63% of its final value.$$\tau=R_{mem}C_{mem}$$

[[Passive Membrane Properties Questions]]