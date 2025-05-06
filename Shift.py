import numpy as np
import matplotlib.pyplot as plt

class ShiftRegister:
    def __init__(self, size):
        self.size = size
        self.reg = np.zeros(size, dtype=float)  # Initialize register with floating-point values
        self.outputs = []  # Track serial outputs over time
    
    def shift(self, input_val):
        self.reg = np.roll(self.reg, 1)  # Shift right
        self.reg[0] = input_val          # Insert new value at left
        output = self.reg[-1]            # Rightmost value = output
        self.outputs.append(output)      # Save output for plotting
        return output

# Example Usage
if __name__ == "__main__":
    sr = ShiftRegister(size=3)  # 3-stage register
    input_sequence = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 2.5, 3.0]
    
    # Process input sequence
    for val in input_sequence:
        sr.shift(val)
    
    # Plot the serial output over clock cycles
    plt.figure(figsize=(10, 4))
    plt.plot(sr.outputs, marker='o', linestyle='-', color='b', label='Serial Output')
    plt.title("Shift Register Output Over Time")
    plt.xlabel("Clock Cycle")
    plt.ylabel("Output Value")
    plt.xticks(range(len(sr.outputs)), range(1, len(sr.outputs) + 1))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()