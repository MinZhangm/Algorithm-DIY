import numpy as np

def main():
    kernel_size = 3
    in_channel = 3
    out_channel = 1
    stride = 1
    padding = 1
    kernel = [np.ones((1, in_channel, kernel_size, kernel_size)) for _ in range(k)]
    
    h = 3
    w = 3
    img = np.ones((1, 3, h, w)) * 2
    input = np.zeros((1, in_channel, h+2*padding, w+2*padding))
    input[:, :, padding:-padding, padding:-padding] = img
    
    output_h = int((h + 2 * padding - kernel_size) / stride)
    output_w = int((w + 2 * padding - kernel_size) / stride)
    output = np.zeros((1, out_channel, output_h, output_w))
    for k in range(out_channel):
      for i in range(0, h+2*padding - kernel_size+1, stride):
          for j in range(0, w+2*padding - kernel_size+1, stride):
              output[:, k, i, j] = np.sum(kernel[l]*input[:, :, i:i+kernel_size, j:j+kernel_size])
    return output

if __name__ == '__main__':
    main()
