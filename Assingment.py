########################################
### written by... : Eriberto
### date written  : May 17 2025
### Purpuse.....  : Assignment
########################################

def main():
    name = input("What is your first name? ")

    last_name = input("What is your last name ? ")

    weight= float(input("What is your weight ? "))

    height = float(input("What is your height ? "))

    days = int(input("how many days have you gone running? "))

    weight_lost = 0.5 * days

    new_weight = weight - weight_lost

    new_height = height + 4.5 + 6.8

    print(f"Hello {name} {last_name}!")
    print(f"You weight {weight}")
    print(f"You are {height} feet tall")
    print(f"You ran {days} days")

    print(f"Based on your exercise you now weight {new_weight}")
    print(f"if you stood in  3 stools and 2 chairs you would be {new_height}")


main()


