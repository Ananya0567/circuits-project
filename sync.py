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