age = input("Введите ваш возраст: ")
if int(age) >= 18:
    print("Добро пожаловать!")
else:
    print("Доступ запрещён.")
name = input("Введите имя: ")
a1 = "Верно!" if name == "Олег" else "Вы не Олег!"
print(a1)
