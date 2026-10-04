name = input("Enter passenger name: ")
age = int(input("Enter age: "))

print("Destinations")
print("1. Chittagong - 500 Tk")
print("2. Sylhet - 400 Tk")
print("3. Rajshahi - 600 Tk")

choice = int(input("Choose destination (1-3): "))
tickets = int(input("Enter number of tickets: "))

if choice == 1:
    destination = "Chittagong"
    fare = 500
elif choice == 2:
    destination = "Sylhet"
    fare = 400
elif choice == 3:
    destination = "Rajshahi"
    fare = 600
else:
    print("Invalid destination")
    exit()

print("Passenger Types")
print("1. Adult")
print("2. Child")
print("3. Student")
print("4. Senior")

ptype = int(input("Choose passenger type (1-4): "))

if ptype == 1:
    passenger_type = "Adult"
    discount = 0
elif ptype == 2:
    passenger_type = "Child"
    discount = 50
elif ptype == 3:
    passenger_type = "Student"
    discount = 20
elif ptype == 4:
    passenger_type = "Senior"
    discount = 30
else:
    print("Invalid passenger type")
    exit()

total = fare * tickets
discount_amount = total * discount / 100
final_fare = total - discount_amount

print("Train Ticket")
print("Passenger:", name)
print("Age:", age)
print("Destination:", destination)
print("Passenger Type:", passenger_type)
print("Number of Tickets:", tickets)
print("Ticket Fare:", fare, "Tk")
print("Total Fare:", total, "Tk")
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount, "Tk")
print("Final Fare:", final_fare, "Tk")
