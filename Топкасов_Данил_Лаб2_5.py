
'''На квадратной доске расставлены целые неотрицательные числа. 
Черепашка, находящаяся в левом верхнем углу, мечтает попасть в 
правый нижний. При этом она может переползать только в клетку 
справа или снизу и хочет, чтобы сумма всех чисел, оказавшихся 
у нее на пути, была бы максимальной.
Напишите программу, которая определяет эту сумму.
Указания.
1). Используйте метод динамического программирования
2). Размер доски и числа на доске считывайте из файла'''

a = []
with open("num5.txt") as f:
    for line in f:
        a.append([int(x) for x in line.split()])
for i in range (len(a)):
    print(a[i])
width = len(a[0])
height = len(a)
print("width = " + str(width) + "  " + "height = " + str(height))
for y in range(1, width): 
    a[0][y] = a[0][y] + a[0][y-1]
for x in range(1, height):
    a[x][0] = a[x][0] + a[x-1][0]
for x in range(1, height):
    for y in range(1, width):
        a[x][y] = a[x][y] + max(a[x-1][y], a[x][y-1])
for i in range (len(a)):
    print(a[i])
print(a[height-1][width-1])