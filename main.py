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
        # print(i, item)
        print(f"{i}. {item["name"]} - {item["quantity"]} x {item["price"]}€")

def count_total(shopping_list):
    total = 0
    for item in shopping_list:
        total += item["quantity"] * item["price"]
    print(f"Total price: {total:.2f}€")

def save_to_file(shopping_list):
    # "w" - перезаписує файл якщо той є або створює новий, якщо немає
    # "a" - дописує (за замовчуванням у кінці файлу) у існуючий файл, якщо файлу немає - помилка
    # file = open("text.txt", "w", encoding="utf-8")
    # file.write("Ok")
    # file.write("2 line")
    # file.write("new_line")
    # file.close()
    # with open("text.txt", "w", encoding="utf-8") as f:
    #     f.write("Ok")
    #     f.write("2 line")
    #     f.write("new_line")
    with open("text.txt", "w", encoding="utf-8") as f:
        for item in shopping_list:
            # Запис у форматі key=value
            f.write(f"name:{item['name']} quantity:{item['quantity']} price:{item['price']}\n")
    print("✅ Shopping_list saved to text.txt")

def load_from_file():
    shopping_list = []
    with open("text.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            data = {}
            for part in parts:
                if ":" in part:                # пропускаємо слова без ":" (частини назви)
                    key, value = part.split(":", 1)
                    data[key] = value
            item = {
                "name": data["name"],
                "quantity": int(data["quantity"]),
                "price": float(data["price"])
            }
            shopping_list.append(item)
    print("✅ Shopping_list loaded from text.txt")
    return shopping_list
        

def main():
    print("🛒 Вітаю у менеджері покупок!")
    shopping_list = []
    
    while True:
     # Нескінченний цикл   
        print("------------------------------")
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
        except ValueError:
         # Спрацьовує, якщо користувач ввів не число і int() не може виконати перетворення
            print("Enter number 1-6!!")
            continue
        match choice:
            case 1:
                try:
                    add_item(shopping_list)
                except  Exception as e:
                # Перехоплює будь-який інший виняток і зберігає його в змінній e
                    print(f"Error!:  {e}" )
            case 2:
                show_list(shopping_list)
            case 3:
                count_total(shopping_list)
            case 4:
                save_to_file(shopping_list)
            case 5:
                try:
                    shopping_list = load_from_file()
                except FileNotFoundError:
                # Спрацьовує, якщо файл не знайдено за вказаним шляхом
                    print("File not found!")
            case 6:
                print("See you!!")
                break
            case _:
                print("Error! Enter number 1-6!")
if __name__ == "__main__":
    main()
    