speed1 = float(input("Введите скорость первой машины (км/ч): "))
speed2 = float(input("Введите скорость второй машины (км/ч): "))
distance = float(input("Введите расстояние между машинами (км): "))

time = distance / (speed1 + speed2)

print(f"Через {time} часов машины окажутся рядом.")