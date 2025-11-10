shopping_list = []
def add_item(shopping_list):
    name = input("Введіть назву товару: ")
    quantity = int(input("Введіть кількість: "))
    price = float(input("Введіть ціну за одиницю: "))
    
    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    
    shopping_list.append(item)
    
    print(f"✅ {name} додано до списку!")  # "✅ " + name + " додано до списку!"

def show_list(shopping_list):
    # shopping_list = [
    #     {"name": "Хліб", "quantity": 2,  "price": 25},
    #     {"name": "Хліб2", "quantity": 2,  "price": 25}
    #     ]
    # for i in range(len(shopping_list)):
    #     print(f"{i+1}. {shopping_list[i]["name"]} - {shopping_list[i]["quantity"]} x {shopping_list[i]["price"]}€")
    
    if not shopping_list:
        print("\nList is empty")
        return
    
    print("\nYour list: ")
    for i, item in enumerate(shopping_list, start=1): 
        # — enumerate() возвращает индекс (i) и элемент (item).
        # print(i, item)
        print(f"{i}. {item["name"]} - {item["quantity"]} x {item["price"]}€")

def count_total():
    total = 0
    for item in shopping_list:
    total += item["quantity"] * item["price"]
print(f"{total:.2f} €")
# print(f"{sum:.2f} €")  # вывод с двумя знаками после запятой

def save_to_file():
    pass

def load_from_file():
    pass

def main():
    print("🛒 Вітаю у менеджері покупок!")
    
    while True:
        print('''
Меню:
1. Додати покупку
2. Переглянути список
3. Порахувати загальну суму
4. Зберегти у файл
5. Завантажити з файлу
6. Вихід
            ''')
        try:
            choice = int(input("Ваш вибір: "))

            # if choice == 1:
            #     pass
            # elif choice == 2:
            #     pass
            match choice:
                case 1:
                    try:
                        add_item(shopping_list)
                    except:
                        print("Error!")
                case 2:
                    show_list(shopping_list)
                case 3:
                    count_total()
                case 4:
                    save_to_file()
                case 5:
                    load_from_file()
                case 6:
                    print("See you!!")
                    break
                case _:
                    print("Error! Enter number 1-6!")
                    
        except ValueError:
            print("Enter number 1-6!!")
main()