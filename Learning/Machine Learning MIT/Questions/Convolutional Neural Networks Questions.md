What is the key role of convolutional neural networks? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	The key role of convolutional neural networks is to build hierarchies of features from data to build a compressed representation of the data's key features. This can then be used for a variety of downstream tasks.

---
How can we represent an image in a neural network? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	We can for an image of size $W\times H$ have a network layer that is $WH$ in size (times the number of color channels we have). This we can think of a simply a matrix of numbers each number is the brightness of a pixel in a certain channel.

---
What are two main tasks that computer vision needs to perform? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	Computer vision needs to perform **classification** and **regression**. *Classification* is where we generate a probability distribution of possible labels for an image out output is the probability an image belongs to each class. In *regression* our output is some continuous value describing some feature in the image.

---
What makes classification and image analysis hard overall and how can deep learning solve this? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	The problem is we need to pick out features of the image however it is very hard for humans to describe this to machines. We are trying to apply our domain knowledge but there are so many variations of each feature we cannot describe them in any robust of efficient way. The deep learning approach is to just describe the truth to out network and allow it to figure out what is true and false on its own.

---
	What is a convolution? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks
		A convolution is a mathematical operation between two matrices. The idea is we have some image network and we march a smaller convolution matrix over our image. Each different position we can place the convolution matrix is a different pixel in the output and the value is the sum of the point wise multiplication of the two values.

---
What is a problem with just feeding an image into a dense layer of a network? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	When we do this we loos all locality in our image. That is there is no special relation between pixels that are close together they might aswell be far away. This can be solved by convolutions which work to have perceptron with only inputs from a patch of pixels.

---
What kind of effects can a basic convolution perform? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	It can perform a blur or sharpen or detect edges.

---
What makes  up a basic convolution layer in network? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	There will be some input to a convolution layer. When a convolution is applied it will generate a new image with. We want to extract many features so we will have $d$ different feature matrices used to perform convolutions. We will apply a bias to each pixel and a nonlinearity. Each output image can be pooled in order to reduce the size. Here a section of the output is taken together and some operation performed over it like max. This will all give us a feature volume which can be the input to the next layer of th network.

---
What is the receptive field of a feature cell? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	The receptive field of a feature cell is the area in the previous image that the summation and point wise product with the convolution matrix took place over (is therefore the size of the matrix).

---
How do the convolutional layers in a network combine? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	Over time they reduce the size of their output to get a smaller and smaller feature volume. This will leave us with a low dimensional part we can feed into a dense layer of a network or any other detail.

---
What are he different forms of object classification and what makes some harder? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	We have pure labeling which takes the whole image. We also have the task of finding a bounding box but this can also be quite simple. The hardest version is detecting and labeling multiple elements in an image. As there are many candidates we will have to access for this.

---
How does a faster R-CNN label images? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	The idea is we generate our feature volume first use this to generate proposed object placements before finally filtering through these comparing them to out features.

---
What is semantic segmentation? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	This is another task that can be done by CNNs where we break down an image into sections that have different labels. That is every pixel has a different color or label that describes what is underneath.

---
How is continuous control achieved by a CNN? #flashcard #MachineLeanringMIT #ConvolutionalNeuralNetworks 
	Continuous control can be achieved by outputting a continuous distribution over all possible command. So in the case of a car this will be a distribution of all the possible steering command describes which ones most like the training set.

---
