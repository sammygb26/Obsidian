# Resting Potential
All neurons have a resting potential that is maintained when the cell is at rest. The potential over the membrane is called the **membrane potential** and is there even when the cell is at rest.  This is a [[Voltage]] and is usually -70mV (always compared to some ground, *outside of the cell* in neuroscience). Either side of the **cell membrane** is mostly water with other stuff mixed in like **proteins**, **ions** and **sugars**. There are many **ions** like $\textrm{Mg}^{2+}$, protons, bicarbonate, phosphate, sulfate and proteins. We will focus for now on sodium, potassium, calcium and chloride all of which help with the resting potential.

## Difference Between Membrane and Resting Potential
**Membrane potential** -> The general term for voltage across the membrane at time point in time; the membrane of a neuron can be around -90mV to +60mV.
**Resting Potential** -> The membrane potential of a neuron that is "at rest", meaning it isn't sending or receiving any signals, usually from -70mV to -60mV

## Diffusion and Electrostatics
These coven the movement of ions around the cell and so the emergence of the **resting potential**. **Diffusion** is movement of particles governed by thermal motion of the particles being diffused. They spread out over time. Overall this means on average particles move from high concentration to low concentration. The **electro static** force is described by [[Voltage]], like charges attract and opposites repel. Diffusion is allowed through **ion selective channels** in the cell membrane that allow some ions to pass and not others.

## Potentials and Equilibrium
We can measure the [[Voltage]] from the outside (extracellular) to the inside (intracellular). This will give us our resting potential. The inside being more negative will make this voltage negative. In the bulk of the solution there is no charge since there is a negative for every positive overall. This doesn't matter however we care about an imbalance created very close the the membrane. This basically creates a **capacitor** over the cell membrane. If we have a bilayer with no openings it creates a barrier stopping flow of ions. 

The **voltage** is created by a concentration imbalance. Which causes charge to move form one side of the cell membrane to the other through **channels**. The charge difference created means only a small amount can come over before the electro static force prevents more and even then it is only very close to the cell membrane.  Only a very small amount of any ion actually moves from one side to the other around 1 in 100000 (since diffusion is weak compared to the electro static force). The **equilibrium potential** is the balancing point where voltage balances diffusion.

## Nernst Equation
The **Nernst Equation** is a equation used to find the equilibrium reached for an ion as it balanced out diffusive and electrostatic forces. This takes in the external and interval concentration of a single ion.
$$
E_{\textrm{ion}}=\frac{RT}{zF}ln\frac{\textrm{[ion]}_\textrm{extracellular}}{\textrm{[ion]}_\textrm{intracellular}}
$$
Here $E_\textrm{ion}$ is the **Nernst potential**, $R$ is the universal gas constant,$T$ is absolute temperature (in kelvin), $z$ is valence of the ion (*net charge in solution*), $F$ is faradays constant, and finally $\textrm{[ion]}_\textrm{extracellular}$  and $\textrm{[ion]}_\textrm{intracellular}$ are the concentrations of the ion outside and inside the cell respectively.

The Nernst potential can have different names. **Nernst Potential** means the balancing point between voltage and diffusion for a single ion, reached at equilibrium so also called **equilibrium potential**. **Reversal Potential** is the point at which ions switch direction from one to the other. Since it is relative temperature this means **Nernst Potential** doesn't change much in normal temperature ranges.

Many ions around the neuron have different Nernst potentials. One example is calcium which has very low concentration inside the cell. This is due to its importance in the signaling of the cell and so it is very controlled.

## Driving Force
**Driving force** is a measure of how much an ion wants to move across the membrane (in one way or the other).
$$
\textrm{Driving Force}=V_{\textrm{membrane}}-E_{\textrm{ion}}
$$
An example of how this works is a typical **resting potential** of -70mV is present across a cell. Calcium ions have a +125mV Nernst potential as there is a high concentration outside relative to the inside. So the positive calcium want to eliminate the negative membrane potential by moving into the cell. This driving force means they will rush in if given an opportunity.  This makes sense as calcium is used for many signaling cascades so it needs to be driven robustly and strongly.
![[Pasted image 20220126012434.png]]

## GHK Equation
We now have the driving force for all the ions, together they can form a stable **steady state**. The **resting potential** is an example of this. We can note when we are in a **steady state** the ions aren't necessarily at their equilibrium potentials described by the Nernst Equation but instead all the different flows controlled by the concentrations and **permeability** of the membrane cancel out and the membrane potential remains stable. The **GHK Equation** is like an expanded version of the Nernst Equation. It takes into account different Ions, their concentrations as well as their **permeabilities**. 

**Permeability** -> This is the ease with which an ion flows across the cell membrane. An ion with a high permeability will more easily be able to flow into and out of the cell. The more permeable a cell membrane it to a given ion the greater effect it will have on the steady state of the cell.

Take for example a cell that is only permeable to potassium, what will happen in this case is that no matter what the Equilibrium Potentials of the other ions are they will not move across the cell membrane hence they will not effect the potential overall of the cell. Potassium on the other hand will diffuse out and be pushed back in by the electrostatic force this will create. But it is only created by potassium hence this potential will just be potassium's equilibrium. Its easy to see how in this case suddenly changing the permeability of a selected ion can cause the membrane potential to rapidly change.

The **GHK** equation therefore has the form of a weighted Nernst Equations. As a log is used the fraction gets split between the sum, the concentration in and out are also flipped depending on the charge of the ion (hence shy Cl is reversed), we get the following equation
$$
V_m=\frac{RT}{F}ln\frac{P_k[k]_o+P_{Na}[Na]_o+P_{Cl}[Cl]_i}{P_k[k]_i+P_{Na}[Na]_i+P_{Cl}[Cl]_o}
$$
So $P_{ion}$ is the permeability for a given ion (1 if completely permeable 0 if impermeable). Then $[ion]_o$ is the centration of the ion outside the cell and $[ion]_i$ is the concentration inside the cell. $R$ is the universal gas constant. $F$ is Faraday's constant and $T$ is the temperature in kelvin.

The idea that **permeability** can be used to control the membrane potential is the key to how neurons change their potential so quickly. It is far easier to change permeability than resting potential.

#### Hyperpolarization and Depolarization
These are two terms the describe changes in the membrane potential of a cell. **Depolarization** means the membrane potential becomes more positive (usually this would mean a less extreme voltage as the potential is usually negative hence the de). **Hyperpolarization** this means the membrane potential gets more negative (and so more extremely negative if its already negative hence the hyper).

## Ion Filters
In order for there to be different permeabilities between ions protein membrane channels have to select which ion passes through but if the ions have the same charge and are only slightly different sizes how is this done. The key is that *water* is polarized. The means one side is more negative than the other. So a stable arrangement of water around an ion would have for a positive ion the negative O in the water facing it this is called a **solvation shell**. For each ion there is a different optimal configuration of water around the ion where all the competing where the different changes in the water and the ion all reach a minimum. This optimal configuration is them simulated by the channel with a **selectivity filter**. 

So despite the small size difference the channel exploits the fact water is everywhere to select for ions. This type of channel that just allows ions to flow down their concentration gradient are called **leakage channels** (as they are passive). There are large amount of passive potassium channels and small amount of sodium and chloride passive selective channels hence the difference in permeability.

## Sodium Potassium Pump
If there are channels for both sodium and potassium that means the concentration will slowly change without creating a voltage to counteract. There is a perfect exchange that can happen where the concentrations get to change but the voltage doesn't. Hence the concentrations would quickly evaporate and any potential created along with it. The **sodium potassium pump** pumps two potassium into the cell and removes 3 sodium each time. This keeps the concentration gradient but it comes at a cost. Up to a third of all energy you eat goes to this one pump, ATP is used to fuel the pump.

[[Resting Potential Questions]]