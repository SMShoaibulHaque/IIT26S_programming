print("Program starting.")
print("Estimate how many minutes you spent on programming...")
print()

A1_T1 = int(input("A1_T1: "))
A1_T2 = int(input("A1_T2: "))
A1_T3 = int(input("A1_T3: "))
A1_T4 = int(input("A1_T4: "))
A1_T5 = int(input("A1_T5: "))
A1_T6 = int(input("A1_T6: "))
A1_T7 = int(input("A1_T7: "))

print()

total = A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7

average = total / 7
average_rounded = int(round(average, 0))

print("In total you spent", total, "minutes on programming.")
print("Average per task was", format(average, ".2f"), "min and same rounded to the nearest integer", average_rounded, "min.")
print()
print("Program ending.")