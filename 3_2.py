# A simple nueral network making a prediction
# multiple input

weights = [0.1, 0.2, 0]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        local_prediction = a[i] * b[i]
        print(round(local_prediction,2))
        output += local_prediction
    return output

def nueral_network(input, weights):
    print('======== Local Prediction ========')
    prediction = w_sum(input, weights)
    return prediction

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 9.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]
pred = nueral_network(input, weights)
print('======== Final Prediction ========')
print(round(pred,2))