import numpy as np
import matplotlib.pyplot as plt

class ShiftRegister:
    def __init__(self, size=4):
        self.size = size
        self.reg = np.zeros(size, dtype=int)  # Initialize register here
    
    def shift(self, data_in, shift_enable=True):
        if shift_enable:
            self.reg = np.roll(self.reg, 1)
            self.reg[0] = data_in
        return self.reg[-1]  # Serial output
    
    def reset(self):
        self.reg = np.zeros(self.size, dtype=int)

# Testbench
sr = ShiftRegister()
inputs = [1, 0, 1, 0]  # Test sequence
outputs = []

print("Shift Register Simulation:")
for bit in inputs:
    outputs.append(sr.shift(bit))
    print(f"Input: {bit}, State: {sr.reg}, Output: {outputs[-1]}")

# Plot
plt.figure(figsize=(8, 4))
plt.step(range(len(outputs)), outputs, where='post', label='Serial Output')
plt.title("Shift Register Output")
plt.xlabel("Clock Cycle")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
