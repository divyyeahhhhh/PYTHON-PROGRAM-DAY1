NumList = []
Even_Sum = 0
Odd_Sum = 0

Number = int(input("ENTER THE NUMBER OF ELEMENTS: "))
for i in range(1, Number + 1):
    value = int(input("ENTER THE %d ELEMENT : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]

print("\nTHE SUM OF ODD NUMBERS IN THE GIVEN LIST =  ", Even_Sum)
print("THE SUM OF EVEN NUMBER IN THE GIVEN LIST=  ",Odd_Sum)
