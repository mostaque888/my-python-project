animals.sort()  # Ensure the list is sorted for binary search

animalToFind = input("What animal would you like to find? ").lower()

validAnimal = False
start = 0
finish = len(animals) - 1

while not validAnimal and start <= finish:
    mid = (start + finish) // 2
    if animals[mid] == animalToFind:
        validAnimal = True
    elif animalToFind > animals[mid]:
        start = mid + 1
    else:
        finish = mid - 1

print(validAnimal)
print(mostaque ahmed)