This is an important part of using CNN like architecture for generating images. There are many options

### Predefined options

1. **Nearest Neighbors** here we just upscale the output then select the values to be the nearest in image space compared to the original image

![[Pasted image 20221115185747.png]]

2. **Bi-Linear Interpolation** here for each pixel we take the 4 nearest pixels and perform a **weighted average** to get our output. The weights are based on the distance to the original values.

![[Pasted image 20221115185907.png]]

3. **Bed Of Nails** here we copy each value over to the new image for the same corresponding place for each original pixel. The other values are filled with zeros.

![[Pasted image 20221115190139.png]]

4. **Max-Unpooling** the **max-pooling** layer in a CNN takes the max value from a pooled section defined for each output pixel. It returns the max for this section and no other values. If we perform this up-sampling in reverse we can use the indices of the max found to unsampled filling the remaining values with 0s.

![[Pasted image 20221115190335.png]]

The options are predefined, not depending on the data, this makes then task specific. They don't learn from the data and aren't generalizable.

### Transposed Convolutions
These are used to unsampled the input feature map to a desired output feature map using **learnable parameters**. Here are the steps

1. We consider our feature map input and a **kernel** that we will perform the transpose convolution with.

![[Pasted image 20221115194920.png]]



2. Now for each input cell we can compute the kernel times this value, it is then placed a spot in the input map corresponding to the place of the input kernel

![[Pasted image 20221115195102.png]]

3. This is repeated for all elements of the input array

![[Pasted image 20221115195250.png]]

4. The elements in these parts are overlapping to solve this we just add them together

![[Pasted image 20221115195330.png]]

