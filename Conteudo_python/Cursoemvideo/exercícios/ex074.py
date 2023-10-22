import random

print("Os números sorteados são:", end=" ")
for c in range(0, 5):
    a = random.randint(1, 10)
    print(a, end=" ")
