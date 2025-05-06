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