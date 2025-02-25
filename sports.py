import datetime

def sportdata():
    while True:
        l = [101, 102, 103, 104, 105]
        print("1.101\n2.102\n3.103\n4.104\n5.105\n")
        a = int(input("Enter equipment ID: "))
        
        if a in l:
            print("Equipment found:", a)
        else:
            print("No equipment found in the list.")
        
        print("\nEquipments available:")
        print("1.Bat\n2.Ball\n3.Basketball\n4.Football\n5.Volleyball\n6.Tennis\n7.Racket\n8.Cock\n")

        s = {
            1: 'Bat',
            2: 'Ball',
            3: 'Basketball',
            4: 'Football',
            5: 'Volleyball',
            6: 'Tennis',
            7: 'Racket',
            8: 'Cock'
        }
        
        n = int(input("Enter the equipment number: "))
        if n in s:
            print("Equipment found:", s[n])
        else:
            print("Equipment not found.")
        
        print("\nCondition of equipment items:")
        print("1.Good\n2.Average\n3.Bad")
        
        t = ['Good', 'Average', 'Bad']
        b = int(input("Enter equipment condition (1-3): "))
        
        if 1 <= b <= 3:
            print("Condition of equipment:", t[b - 1])
        else:
            print("Invalid condition input.")
        
        print("\nEnter Borrower Details:")
        n = input("Enter Name: ")
        u = input("Enter USN: ")
        b = input("Enter Branch: ")
        eid = int(input("Enter Equipment ID: "))
        
        tob_current_datetime = datetime.datetime.now()
        print("\nCurrent date and time:", tob_current_datetime)
        print("Name:", n)
        print("USN:", u)
        print("Branch:", b)
        print("Equipment ID:", eid)

        # Set return date (borrow date + 7 days)
        date_of_return = tob_current_datetime + datetime.timedelta(days=7)
        print("Expected Date of Return:", date_of_return.strftime("%Y-%m-%d"))

        tor_current_datetime = datetime.datetime.now()
        print("Time of borrowing:", tor_current_datetime)

        # Returning equipment
        l = int(input("\nEnter the same Equipment ID for returning: "))
        if l == eid:
            tor_return_datetime = datetime.datetime.now()
            print("\nEquipment returned successfully!")
            print("Returned Date and Time:", tor_return_datetime)
            print("Expected Date of Return:", date_of_return.strftime("%Y-%m-%d"))
        else:
            print("Equipment not returned, please return it.")

        return n, u, b, eid, tob_current_datetime, date_of_return

sportdata()
