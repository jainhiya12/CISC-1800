# Hiya Jain
# Lab 07: Neuro-OOP: Exploring Object-Oriented Programming through Neuroscience
# CISC 1800 - Introduction to Computer Programming

# Class I. neuron
class Neuron:
  def __init__(self, name, neuron_type, resting_potential):
    self.name = name
    self.neuron_type = neuron_type
    self.resting_potential = resting_potential
    self.potential_change = 0.0
    self.threshold = -55.0
    self.refractory_period = 5
    self.last_firing_time = 0

# set resting potential
  def set_resting_potential(self, resting_potential):
    self.resting_potential = resting_potential

# fire
  def fire(self, time):
    elapsed_time = time - self.last_firing_time
    if elapsed_time < self.refractory_period:
      self.potential_change = 0.0
      return
    if self.resting_potential >= self.threshold:
      if self.neuron_type == 'excitatory':
        self.potential_change = 15.0 
      elif self.neuron_type == 'inhibitory':
        self.potential_change = -10.0 
      else:
        self.potential_change = 0.0
    self.last_firing_time = time 
    return self.potential_change

# get potential change
  def get_potential_change (self):
    return self.potential_change

# set threshold
  def set_threshold (self, threshold):
    self.threshold = threshold

# set refractory period
  def set_refractory_period (self, refractory_period):
    self.refractory_period = refractory_period
    
# Class II. Sensory Neuron
class SensoryNeuron(Neuron):
  def __init__(self, name, neuron_type, resting_potential, sensitivity):
    super().__init__(name, neuron_type, resting_potential)
    self.sensitivity = sensitivity

# fire
  def fire (self, stimulus):
    potential_change = stimulus * 0.1 
    self.resting_potential += potential_change
    if self.resting_potential >= self.sensitivity:
      self.potential_change = potential_change
    else:
      self.potential_change = 0.0
    return self.potential_change

# Class III. Synapse
class Synapse:
    def __init__(self, pre_neuron, post_neuron, weight):
      self.pre_neuron = pre_neuron
      self.post_neuron = post_neuron
      self.weight = weight
      self.last_firing_time = -1

# fire
    def fire(self, firing_time):
      if self.last_firing_time < 0:
        self.last_firing_time = firing_time
        time_since_last_firing = firing_time - self.last_firing_time
        if time_since_last_firing >= self.pre_neuron.refractory_period:
          potential_change = self.pre_neuron.get_potential_change()
          new_resting_potential = self.post_neuron.resting_potential + (potential_change * self.weight)
          self.post_neuron.set_resting_potential(new_resting_potential)
          self.last_firing_time = firing_time
          return potential_change * self.weight
        else:
          return 0.0


# Create instances of the classes
n1 = Neuron("N1", "excitatory", -70.0)
n1.set_threshold(-60.0)
sn1 = SensoryNeuron("SN1", "excitatory", -70.0, -50.0)
synapse = Synapse(sn1, n1, 0.5)

#test
for time in range(10):
    sn1.fire(100.0)
    sn1.fire(time)
    potential_change = n1.fire(time)
    print(f"At time {time}, {n1.name}'s potential changed by {potential_change}.")
