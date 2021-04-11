#!/usr/bin/env python
# coding: utf-8

# # Steps:

# # 1) Importing all modules from qiskit.

# In[1]:


from qiskit import *


# # 2) Creating 3 qubits and 3 classical bits for the circuit.

# In[2]:


circuit = QuantumCircuit(3,3)


# # 3) Including the matplotlib types of graphs in the notebook.

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# # 4) Output Status

# In[4]:


circuit.draw(output='mpl')


# # 5) Adding the X gate on qubit(0) with a barrier for clear visualization.

# In[5]:


circuit.x(0)
circuit.barrier()


# # 6) Output Status.

# In[6]:


circuit.draw(output='mpl')


# # 7) Adding a Hadamard Gate on qubit(1) and a Controlled X gate between qubit 1 and qubit(2).

# In[7]:


circuit.h(1)
circuit.cx(1,2)


# # 8) Output Status.

# In[8]:


circuit.draw(output='mpl')


# # 9) Adding a Controlled X gate between qubit 0 and qubit 1 and a Hadamard Gate on qubit(0).

# In[9]:


circuit.cx(0,1)
circuit.h(0)


# # 10) Output Status.

# In[10]:


circuit.draw(output='mpl')


# # 11) Adding a barrier for clear visualization.

# In[11]:


circuit.barrier()


# # 12) Adding measurement from qubit(0) to classical bit(0) and qubit(1) to classical bit(1).

# In[12]:


circuit.measure([0,1], [0,1])


# # 13) Output Status.

# In[13]:


circuit.draw(output='mpl')


# # 14) Adding a barrier for clear visualization.

# In[14]:


circuit.barrier()


# # 15) Adding a Controlled X gate between qubit(1) and qubit(2) and a Controlled Z gate between qubit(0) and qubit(2).

# In[15]:


circuit.cx(1,2)
circuit.cz(0,2)


# # 16) Output Status.

# In[16]:


circuit.draw(output='mpl')


# # 17) Adding measurement from qubit(2) to classical bit(2).

# In[17]:


circuit.measure(2,2)


# # 18) Output Status.

# In[18]:


circuit.draw(output='mpl')


# # 19) Simulating/Running the circuit with QASM Simulator.

# In[19]:


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1024).result()
counts = result.get_counts()


# # 20) Plotting the final result with the help of a histogram.

# In[20]:


from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)


# In[ ]:




