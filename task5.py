products = {
    "Запчасть 1": ["Описание 1", 100, 5],
    "Запчасть 2": ["Описание 2", 200, 3],
    "Запчасть 3": ["Описание 3", 300, 10]
}

def show_description():
    for product, details in products.items():
        print(f"{product}: {details[0]}")

def show_price():
    for product, details in products.items():
        print(f"{product}: Цена - {details[1]}")

def show_quantity():
    for product, details in products.items():
        print(f"{product}: Количество - {details[2]}")

def show_all_info():
    for product, details in products.items():
        print(f"{product}")
        print(f"Описание: {details[0]}")
        print(f"Цена: {details[1]}")
        print(f"Количество: {details[2]}\n")

def make_purchase():
    total_price = 0
    while True:
        product = input("Введите название продукции или '0' для выхода: ").capitalize()
        if product == '0':
            break
        if product in products:
            quantity = int(input("Введите количество: "))
            if quantity <= products[product][2]:
                price = products[product][1] * quantity
                total_price += price
                products[product][2] -= quantity
                print(f"Вы купили {quantity} шт. {product} за {price} руб.")
            else:
                print("Такого количества нет в наличии.")
        else:
            print("Такой продукции не существует.")
    print(f"Общая стоимость покупки: {total_price} руб.")
    print("Оставшееся количество товаров:")
    show_quantity()

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            show_description()
        elif choice == "2":
            show_price()
        elif choice == "3":
            show_quantity()
        elif choice == "4":
            show_all_info()
        elif choice == "5":
            make_purchase()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

main_menu()
