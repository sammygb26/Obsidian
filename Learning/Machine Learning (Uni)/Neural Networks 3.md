Neural networks became more popular as multi-layer training was solved. But **overfitting** and poor **generalization** lead to slow progress. Problems:

1. **Computationally very expensive** (weeks of training)
2. **Slow convergence** vanishing gradients from many layers does improve after a certain point.
3. **Difficulty to find optimal network topology**
4. Poor **generalization**, very good performance on training set and poor on test set.

### Overfitting and Generalization
We may have some function we fit and we may use different degrees of polynomials to 'fit' it. But as we use higher and higher polynomial we will get less error but it will be very different from our underlying model or world model.

![[Pasted image 20221017152000.png]]

The problem here is the model is **memorizing** the training data and so doesn't work well in the actual test.

We often split our data into two datasets. A **training** and **test/validation** dataset. We can compare the errors on the different sets. If the training set has much lower errors we have **overfit** to the training set. **Overtraining** (overfitting) happens when a network function is too closely fit to the training set. **Undertraining** happens when a network function isn't fit well to the training set. These correspond to too little and too much overfitting. To control this different techniques are used like **early stopping** and **regularization**.

##### Early Stopping
Here we compare the validation and training error and we stop when the validation error gets too low. That is we have stopped improving on data we haven't trained on.

![[Pasted image 20221017152503.png]]

##### Regularization
Here we penalize complexity by ensuring our weights are within a range for example by using a **weight decay function**. We change our loss/error function to include this: $$E(w)=\frac12\sum_{n=1}^N||\hat y_n-y_n||^2\to E(w)=\frac12\sum_{n=1}^N||\hat y_n-y_n||^2+\frac\beta2\sum||w||^2$$We restrict the values our weights can have and so restrict the model. This makes it **less-flexible**.

![[Pasted image 20221017152849.png]]

### Breakthrough
After a long time of believing neural networks wouldn't be useful many breakthrough came leading to a resurgence. The reasons for the comeback:

1. **Pretraining** - with a large neural network we don't retrain from scratch but we can training parts piecemeal and then finetuning to our network. For example we can increase the size over time.
2. **Fine tuning**
3. **Dropout**
4. **GPU**
5. **Convolutional Neural Network**, **LSTM**
6. **ReLU**

### Speech Recognition
This is one of the tasks neural networks have revolutionized (red).

![[Pasted image 20221017153340.png]]

### Dropout
This is a technique for **regularization**. During the training we remove some weights and nodes by setting them to 0. This forces the network to be robust.

![[Pasted image 20221017153510.png]]

### Convolution
[[Convolutional Neural Networks]] where a major breakthrough in neural networks. The convolution filters are learned from the data. Through training the optimal filters are found. The filters are also called **kernels**. **Stride** describes how far we move the filter between each output pixel. **Padding** allows us to move the filter outside of the image slightly to allow edge values to still be used.

**Pooling** also allows us to scale back the output to a smaller scale by moving a 'pool' about the image and taking the maximum values. We can also perform *average pooling*. This helps make the network smore robust to small shifts.

![[Pasted image 20221017154725.png]]

Convolutions can take place in 1D or 2D.

![[Pasted image 20221017154243.png]]

### Normalization
**Batch Normalization** is often used to make the values into a layer have a normal distribution. Hence meaning the network has more usual values between samples.

### Other Neural Networks
![[Pasted image 20221017155059.png]]

![[Pasted image 20221017155118.png]]

![[Pasted image 20221017155143.png]]

![[Pasted image 20221017155157.png]]

![[Pasted image 20221017155919.png]]

[[Neural Networks 3 Questions]]
