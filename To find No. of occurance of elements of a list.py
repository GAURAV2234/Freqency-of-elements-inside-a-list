##count the number of occurance of each element in a list

a=[]
b=int(input("Enter the No. of elements you want to put in list:"))
for i in range(b):
    b=int(input("Enter element"))
    a.append(b)

print("\nList you entered:",a)


element_counts = {}

for i in a:
    if i in element_counts:
        element_counts[i] += 1
    else:
        element_counts[i] = 1
print("\n\nCout of No. of occurance of elements are:\n")
for i,count in element_counts.items():
    print(f"{i}: {count}")
