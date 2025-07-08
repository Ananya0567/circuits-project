#shift register

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


#Multiplexer

import matplotlib.pyplot as plt

class Mux4to1:
    def __init__(self, inputs=None):
        self.inputs = inputs if inputs is not None else [0.8, 0.6, 0.4, 0.2]
    
    def select(self, sel):
        return self.inputs[sel]

# Initialize MUX
mux = Mux4to1()

# --- CMD OUTPUT ---
print("4:1 Multiplexer States:")
print("-----------------------")
print(f"Inputs: {mux.inputs}")
print("Possible selections: 0, 1, 2, 3\n")

# Select ONE output (e.g., sel=2 → 0.4)
selected_sel = 2
selected_output = mux.select(selected_sel)

# Print current state to CMD
print(f"Current selection: sel={selected_sel}")
print(f"Current output: {selected_output}\n")

# --- GRAPH ---
plt.figure(figsize=(6, 4))
plt.stem([selected_sel], [selected_output],
         basefmt=" ", linefmt="blue", markerfmt="bo",
         label=f"sel={selected_sel}, out={selected_output:.2f}")
plt.title("Single Multiplexer Output")
plt.xlabel("Selection (sel)")
plt.ylabel("Output Value")
plt.xticks(range(4))
plt.legend()
plt.grid(True)
plt.show()

#Synchronous Counter

import matplotlib.pyplot as plt

class SyncCounter:
    def __init__(self, bits=2):
        self.bits = bits
        self.max = (1 << bits) - 1  # Equivalent to 2**bits - 1
        self.count = 0  # Initialize count here
    
    def increment(self, enable=True):
        if enable:
            self.count = (self.count + 1) & self.max
        return self.count
    
    def reset(self):
        self.count = 0

# Testbench
counter = SyncCounter()
states = []
print("\nMod-4 Counter Simulation:")
for _ in range(6):  # Count for 6 cycles
    states.append(counter.increment())
    print(f"Count: {bin(states[-1])[2:].zfill(2)} ({states[-1]})")

plt.figure(figsize=(8, 4))
plt.step(range(len(states)), states, where='post', label='Count')
plt.title("Synchronous Counter States")
plt.xlabel("Clock Cycle")
plt.ylabel("Count Value")
plt.yticks(range(4), [f"{i:02b}" for i in range(4)])  # Binary labels
plt.legend()
plt.grid(True)
plt.show() 