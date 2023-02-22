# Hiya Jain
# Lab 04: Tower of Hanoi
# CISC 1800 - Introduction to Computer Programming

def tower_of_hanoi(n, source, auxiliary, target):
  if n == 1:
    print("move disc top from", source, "to", target)
    return
  else:
    tower_of_hanoi(n-1, source, target, auxiliary)
    print("move disc", n, "from", source, "to", target)
    tower_of_hanoi(n-1, auxiliary, source, target)

n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
