# Software Engineering for Data Science
We are going to go over software engineering for data science. One of the key ideas is **reproducible research**. The idea here is if researchers in the future wanted to test if our research still held up. All the code and experimentation and data should give us the same result in the future. It can be quite hard to keep code updated and understand how it functioned in the past in order to get the same results again.

![[Pasted image 20220214091503.png]]

There are three things we need for **reproducible research**

1. **Data** -> the actual figures we used to produce our results
2. **Code** -> the actual machine we use to get our result
3. **Documentation** -> instructions on how the code functions and how to use it

**Data and Barriers** -> One of the main problems is when you want o reproduce data you need to obtain the data. It actually isn't common to keep data or share it at least in the past. So it can be really hard to find data. A lot of data will get lost if it sits on legacy systems over time. We need to make sure to back up data and share to ensure it isn't lost.

**Facilitators of Reproducible Research** -> There are data repositories that keep a copy of data they can be run by Universities, Governments, Science Communities and International Communities.

**Barriers to Reproducible Research with Code** -> Code isn't share so this is the same result as with data. Then code may not run or run badly or have errors. Code may be errors that only the researchers knew how to use. Code may not be **tested on a clean system** or might run on a **different operating system** or have **bugs**. Programming languages can also change which can make code no longer work.

**Facilitators of Reproducible Research with Code** -> There are tools like GitHub. **Unit tests** can also work to ensure some package is working correctly. There is **continuous integration** that checks the code every time the code is updated and shows what tests have failed. There are also code checking groups that will go over different research and check it. We can use Virtual Machines or Environments to make sure code is running in the same place.

**Barriers and Facilitators of Reproducible Research Documentation** -> We can open up data and have no idea what it actual means. For example data might not be explained for example what the columns mean and how it was collected. A simple way to do this is a **read me** file.

## Notebooks vs Programs
**Notebooks** are a type of interface for example with **Jupyter**. We combine text and computation math to give a paper that is alive an would reproduce the same result over and over again. Another concept is **literal programing** which is a type of programming where you have lots of text along with a program as you write it to help write it. In **notebooks** the text is there just to explain what the program is doing to help understand some data. **Jupyter** is a opensource version of **Mathematica**. **Jupyter** runs **python** as well as other languages making it very extendible. 

**Notebooks** help with reproducible code as they will be able to run the same code twice and if we make sure the notebook runs someone else can reproduce the data. Many **packages** have python interfaces so many things can be **embedded** within the analysis. **Jupyter** can also be used on a remote server which is useful for records that can't be used like health records.

**Problems** -> Notebooks can be copied for different data sets which can cause code repetition when copying notebooks. This can cause problems when we try to edit one we have to make sure to edit them all. But if we wanted to do the same thing many times we should make an actual program or set of functions etc.

Another problem is **inconsistent states** if we edit code it wont update our code in order. This causes code to run in a strange way. We can **restart the kernel** and **run all cells** to check this. **Collaboration** is also hard with notebooks with very large notebooks it makes sense to use version control and code bases. 

We also tend to write in an **functional** style and note use classes. But classes can be useful in some circumstances.

Notebooks are still **considerably better** than fragments of code and truly help out science. To get the best of both worlds we can combine python notebooks with **modules**. We can put complex reused code in a module.

## Data and Code Management
We can use **version control** for maintaining code in small text files. Does it make sense for **data** they don't work well **version control** isn't suited to this. The first key thing is to **save raw data** so that any processing can be redone and reproduce out results from the ground up. We should **protect our data** to make sure it isn't accessed sand kept static. We should if downloading data maintain a **record** of how we obtained it and if from a database what version. We should also **back up data** to make sure it isn't lost.

We should **save and share a clean version of the data** that is a version we have cleaned up with our code. This should be saved in an open data formal like CSV or JSON. It should be understandable with meaningful names. We should include metadata about the meaning of the data (like a read me file). We should keep data in a **tidy** format with one observation by row and one feature per column. We should also **separate** out our data and make sure it is at a granular scale without composite features like "cat with black fur" instead "cat" and "black fur". **Metadata** should also be in a separate column like units. Each observation should have a **unique id** to help with merging later. We can share all this in a **repository** to help share it. There are issues with this depending on the laws around the data.

**Code** can be maintained by **version control** (like **git**).  Code should also be **documented** so it is understandable. We should also specify **versions** of the packages we are using so the parts of code not included that are in packages can be reused. We can include descriptions of this like **.req** files. Only problem with **jupyer notebooks** is they are written in JSON. So the difference between two notebooks are also their JSON part so version control will tell lots of differences easily. A workaround for jupyer that allows for cleaner diffs is **nbdime**.