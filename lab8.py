import matplotlib.pyplot as plt
import random

class Simulator:

    def __init__(self, base = 10, delta = 0.15):
        self.base = base
        self.delta = delta

    def generator_4(self, increment = True) -> float:
        if increment:
            self.base += random.gauss(0, 0.1) #self.delta
        else:
            self.base -= random.gauss(0, 0.1) #self.delta
        return self.base
        
number_of_values = 500 #random.randint(0,500)

test = Simulator(0) #Simulator(10, 0.15)    
y = [test.generator_4((x % 50) > 24) for x in range(number_of_values)]

plt.plot(y, 'g')

plt.show()