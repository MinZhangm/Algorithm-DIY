import numpy as np

def softmax():
    h = 10
    img = np.linspace(0, 10, h)

    output = np.zeros(h)
    tmp = 0
    for i in range(h):
        output[i] = np.exp(img[i])
        tmp += output[i]
    tmp = tmp * np.ones((h))
    output = output / tmp
    return output


if __name__=='__main__':
    softmax()
