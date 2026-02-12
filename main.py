from utils import *

def main():
    data = load_data()

    while True:
        print("=== Expense Tracker ===")
        print("1. Ko‘rish")
        print("2. Qo‘shish")
        print("3. Kategoriya bo‘yicha")
        print("0. Chiqish")

        choice = input("Tanla: ")

        if choice == "1":
            show_expenses(data)

        elif choice == "2":
            title = input("Nomi: ")
            amount = float(input("Summa: "))
            category = input("Kategoriya: ")
            add_expense(data, title, amount, category)

        elif choice == "3":
            by_category(data)

        elif choice == "0":
            break

        else:
            print("Xato tanlov")

if __name__ == "__main__":
    main()
