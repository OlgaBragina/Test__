#Task1
#1.Определите является ли строка записью числа.
Weight = " 6. "
print(Weight.isdigit())
#2Посчитайте сколько у вас пробелов в строке.
print(Weight.count(" "))
#3Посчитайте сколько у вас символов точки "." в строке.
print(Weight.count("."))

#4Создайте строку "Homework" Преобразуйте её в строку длиной 100 символов,
#посередине которой исходное слово, а с обоих сторон строка заполнена
#пробелами. Выведите её на экран. Убедитесь, что у вас 100 символов
#(посчитайте длину).
#a="Homework"

#5.Сделайте первые буквы слов строки большими (upper case).
b="  cherry is a nice berry      "
print(b.title())

#6.Определите заканчивается ли ваша строка подстрокой “ing”.
#slice=b.rfind(str [start],[end])
#print(slice)
#7.Определите индекс первого вхождения символа “a” в вашей строке
index=b.find("a")
print(index)
#8.Разбейте строку на список подстрок по символу пробела.
listOFstr=b.split()
print(listOFstr)

#9.Пусть у вас строка имеет пробельные символы. Найдите метод, который удаляет
#пробельные символы вначале и в конце, но не посередине.
textWithoutSpaces=b.strip()
print(textWithoutSpaces)

#Task2
#
cars=['reno', 'opel', 'pejot', 'mazda', 'honda']

print(cars[-3])
print(cars[0])
cars.append('kia')
cars.insert(3, 'mersedes')

cars.remove('reno')
print(cars)

#Task4

market={'icecream_name':'berry','price':68,'Ingredients':['milk','jam']}
market['topping']='caramel'
market['price']=100
market['Ingredients'].append('nuts')
market.pop('icecream_name')
print(market)





