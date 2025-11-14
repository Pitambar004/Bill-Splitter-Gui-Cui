def split_bill():
    print("=" * 40)
    print("          BILL SPLITTER")
    print("=" * 40)

    while True:
        try:
            subtotal = float(input("\nEnter bill subtotal (before tax): $"))
            if subtotal <= 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            tax_percent = float(input("Enter tax percentage: "))
            if tax_percent < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    tax_amount = subtotal * (tax_percent / 100)
    total_bill = subtotal + tax_amount

    print(f"\nTotal bill with tax: ${total_bill:.2f}")

    has_vegetarians = input("\nAre there any vegetarians? (y/n): ").lower() == 'y'

    meat_total = 0
    if has_vegetarians:
        while True:
            try:
                meat_total = float(input("Enter total price of meat items: $"))
                if meat_total < 0:
                    print("Please enter a non-negative amount.")
                    continue
                if meat_total > subtotal:
                    print("Meat items cannot exceed subtotal.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

    while True:
        try:
            num_people = int(input("\nEnter number of people: "))
            if num_people <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    people = {}
    vegetarians = []
    non_vegetarians = []

    print("\nEnter details for each person:")
    for i in range(num_people):
        print(f"\nPerson {i+1}:")
        name = input("  Name: ").strip()
        while not name:
            print("  Name cannot be empty.")
            name = input("  Name: ").strip()

        is_veg = False
        if has_vegetarians:
            is_veg = input(f"  Is {name} vegetarian? (y/n): ").lower() == 'y'
            if is_veg:
                vegetarians.append(name)
            else:
                non_vegetarians.append(name)

        while True:
            try:
                prev_due = float(input(f"  Previous due for {name} (0 if none): $"))
                break
            except ValueError:
                print("  Please enter a valid number.")

        people[name] = {'is_vegetarian': is_veg, 'prev_due': prev_due}

    if has_vegetarians and meat_total > 0 and len(non_vegetarians) > 0:
        vegetarian_items = subtotal - meat_total
        meat_per_person = meat_total / len(non_vegetarians)
        veg_items_per_person = vegetarian_items / num_people
        tax_per_person = tax_amount / num_people

        print("\n" + "=" * 40)
        print("          RESULTS")
        print("=" * 40)
        print(f"Subtotal:             ${subtotal:.2f}")
        print(f"Tax ({tax_percent}%):             ${tax_amount:.2f}")
        print(f"Total Bill:           ${total_bill:.2f}")
        print(f"\nMeat items:           ${meat_total:.2f}")
        print(f"Vegetarian items:     ${vegetarian_items:.2f}")
        print("\n" + "-" * 40)
        print("Individual Amounts:")
        print("-" * 40)

        for name, info in people.items():
            if info['is_vegetarian']:
                current_share = veg_items_per_person + tax_per_person
                print(f"\n{name} (Vegetarian):")
                print(f"  Vegetarian items:   ${veg_items_per_person:.2f}")
            else:
                current_share = veg_items_per_person + meat_per_person + tax_per_person
                print(f"\n{name}:")
                print(f"  Vegetarian items:   ${veg_items_per_person:.2f}")
                print(f"  Meat items:         ${meat_per_person:.2f}")

            print(f"  Tax share:          ${tax_per_person:.2f}")
            print(f"  Current total:      ${current_share:.2f}")

            if info['prev_due'] > 0:
                print(f"  Previous due:       ${info['prev_due']:.2f}")

            total_owed = current_share + info['prev_due']
            print(f"  TOTAL TO PAY:       ${total_owed:.2f}")
    else:
        per_person = total_bill / num_people

        print("\n" + "=" * 40)
        print("          RESULTS")
        print("=" * 40)
        print(f"Subtotal:             ${subtotal:.2f}")
        print(f"Tax ({tax_percent}%):             ${tax_amount:.2f}")
        print(f"Total Bill:           ${total_bill:.2f}")
        print(f"Split {num_people} ways:         ${per_person:.2f} per person")
        print("\n" + "-" * 40)
        print("Individual Amounts:")
        print("-" * 40)

        for name, info in people.items():
            total_owed = per_person + info['prev_due']
            veg_label = " (Vegetarian)" if info['is_vegetarian'] else ""
            print(f"\n{name}{veg_label}:")
            print(f"  Current share:      ${per_person:.2f}")
            if info['prev_due'] > 0:
                print(f"  Previous due:       ${info['prev_due']:.2f}")
            print(f"  TOTAL TO PAY:       ${total_owed:.2f}")

    print("\n" + "=" * 40)

    again = input("\nSplit another bill? (y/n): ").lower()
    if again == 'y':
        print("\n")
        split_bill()
    else:
        print("\nThanks for using Bill Splitter! 👋")

if __name__ == "__main__":
    split_bill()
