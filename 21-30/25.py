from util.fibs import fibs

lb = 10 ** 999

for index, value in enumerate(fibs(), 1):
    if value >= lb:
        print(index)
        break