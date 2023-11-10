from PIL import Image
import numpy as np


def convolve2D(image, kernel, padding=0, strides=1):
    # Do convolution instead of Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    kernel_x_shape = kernel.shape[0]
    kernel_left = kernel_x_shape // 2
    # since slicing end is exclusive, uneven kernel shapes would be too small
    kernel_right = int(np.around(kernel_x_shape / 2.))

    kernel_y_shape = kernel.shape[1]
    kernel_up = kernel_y_shape // 2
    kernel_down = int(np.around(kernel_y_shape / 2.))

    image_x_shape = image.shape[1]
    image_y_shape = image.shape[0]  

    # Shape of Output Convolution
    # The analytical formula for the output shape of the convolution is given by:
    # floor[(n_x - k_x + p_x + s_x) / s_x] x floor[(n_y - k_y + p_y + s_y) / s_y]
    # where n_x and n_y are the dimensions of the input image, k_x and k_y are the
    # dimensions of the kernel, p_x and p_y are the padding sizes, and s_x and s_y
    # are the strides in the x and y directions respectively.
    
    output_x_shape = int(np.floor((image_x_shape - kernel_x_shape + 2 * padding + strides) / strides))
    output_y_shape = int(np.floor((image_y_shape - kernel_y_shape + 2 * padding + strides) / strides))
    output = np.zeros((output_y_shape, output_x_shape))
    
    # Apply Equal Padding to All Sides
    if padding != 0:
        image_padded = np.pad(image, pad_width=padding, mode='edge')
    else:
        image_padded = image

    # Indices for output image
    x_out = y_out = -1
    # Iterate through image
    for y in range(kernel_up, image_padded.shape[0], strides):
        # Exit Convolution before y is out of bounds
        if y > image_padded.shape[0] - kernel_down:
            break
        
        y_out += 1

        # iterate over columns and perform convolution
        # position the center of the kernel at x,y
        # and save the sum of the elementwise multiplication
        # to the corresponding pixel in the output image
        for x in range(kernel_left, image_padded.shape[1], strides):
            # Exit Convolution before x is out of bounds
            if x > image_padded.shape[1] - kernel_right:
                break
            
            # increment x_out
            x_out += 1

            # Convolution
            # elementwise multiplication of the kernel and the image
            # and summing the result
            output[y_out, x_out] = (kernel * image_padded[y - kernel_up:y + kernel_down,
                                                        x - kernel_left:x + kernel_right]).sum()
        # Reset the x_out index
        x_out = -1
    return output


def main():
    # Grayscale Image
    image = np.array(Image.open("image.png").convert('L'))

    # Edge Detection Kernel
    kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    # Convolve and Save Output
    output = convolve2D(image, kernel, padding=2, strides=2)
    Image.fromarray(output).convert('L').save("convolution_output.png")


if __name__ == '__main__':
    main()
