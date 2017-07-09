import numpy as np
from random import randint


solid = np.array([0,0],[0,0])
vertical = np.array([1,0],[1,0])
horizontal = np.array([1,1],[0,0])
diagonal = np.array([1,0],[0,1])


def invert_1_0(number):
    if number == 1:
        number = 0
    elif number == 0:
        number = 1
    else:
        print('Number not in defined range') #not sure if it is a smart thing to print here, it could break stuff
        pass
    return number

# !!! ATTENTION !!! Wierd code ahead
#
# I use i and j to later finde the specific element of the array to be able to overwrite it
# thats why I have to use range(len(array) to first get the row
# and range(len(array[i]) to find the column
#
def invert_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i,j] = invert_1_0(array[i,j])
    return array

def generate_input_img():
    return np.array([randint(0,1),randint(0,1)],[randint(0,1),randint(0,1)])

class neuron():
    def __init__(self):
        self.w1 = random.uniform(-1,1)
        self.w2 = random.uniform(-1,1)
        self.w3 = random.uniform(-1,1)
        self.w4 = random.uniform(-1,1)

        self.array = np.array([self.w1],[self.w2],[self.w3],[self.w4])

#    def __sigmoid(self, x):
#        return 1 / (1 + exp(x))
# probably need this not here but elsewhere
#    def __sigmoid_derivative(self,x):
#        return x * (1 - x)

    def get_inputs(self,x,y,z,w):
        self.store = (x * self.w1) + (y * self.w2) + (self.w3 * z) + (self.w4 * w) #paranthesis just for readability

    def return_neuron_value(self):
        return 1 / (1 + np.exp(self.store))

    def array(self):
        return self.array

    def adjust_wheights(self,wheight, value):
        if wheight == w1:           # function to adjust the wheigts of the neuron
            self.w1 = value
        elif wheight == w2:
            self.w2 = value
        elif wheight == w3:
            self.w3 = value
        elif wheight == w4:
            self.w4 = value
        else:
            print('Wheight not in range for neuron') #again, probably a stupid idea

class input_vector()

    def __init__(self,v1,v2,v3,v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4


