# Lab8
# group_3_data_generator.py
import matplotlib.pyplot as plt
import random

class Simulator:

    def __init__(self, base, delta):
        self.base = base
        self.delta = delta

    def generator_4(self, increment = True) -> float:
        if increment:
            self.base += random.gauss(0, 0.1) #self.delta
        else:
            self.base -= random.gauss(0, 0.1) #self.delta
        return self.base
    def generator_1(self) -> float:
        return random.gauss(self.base, self.delta)
    def generate_outliner(self) -> float:
        return random.uniform(-self.base, self.base)
        
#number_of_values = 500 #random.randint(0,500)

# test = Simulator(10,2) #Simulator(10, 0.15)    
#y = [test.generator_4((x % 50) > 24) for x in range(number_of_values)]

#plt.plot(y, 'g')