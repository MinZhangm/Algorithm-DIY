import numpy as np

def convolution():
    input_h = 5
    input_w = 5
    input_channel = 3
    output_channel = 2
    kernel_size = 3
    stride = 1
    padding = 1

    kernel = [np.ones((1, input_channel, kernel_size, kernel_size)) for _ in range(output_channel)]
    input_img = np.ones((1, input_channel, input_h, input_w)) * 2
    padding_img = np.zeros((1, input_channel, input_h + padding*2, input_w + 2*padding))
    padding_img[:, :, padding:-padding, padding:-padding] = input_img

    output_h = int((input_h - kernel_size + 2*padding + 1) / stride)
    output_w = int((input_w - kernel_size + 2*padding + 1) / stride)
    output = np.zeros((1, output_channel, output_h, output_w))

    for k in range(output_channel):
        for i in range(0, input_h + padding*2-kernel_size+1, stride):
            for j in range(0, input_w + 2*padding-kernel_size+1, stride):
                output[:, k, i, j] = np.sum(kernel[k] * padding_img[:, :, i:i+kernel_size, j:j+kernel_size])
    return output


if __name__=='__main__':
    convolution()
