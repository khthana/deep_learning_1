import numpy as np

weights = np.array([0.1, 0.2, 0])

def ele_mul(number, vector):
    output = [0,0,0]
    assert(len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output

def nueral_network(input, weights):
    prediction = ele_mul(input, weights)
    return prediction

wlrec = [0.65, 0.8, 9.8, 0.9]
input = wlrec[0]
pred = nueral_network(input, weights)
print(pred) 