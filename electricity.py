import sys

if len(sys.argv) == 2:
    units = float(sys.argv[1])
else:
    print("No units entered. Using default units...")
    units = 200   

bill = units * 5

print("Electricity Bill: ₹", bill)
