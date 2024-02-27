with open('C5.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    numbers = line.strip().split(',')
    sum = 0
    count = 0
    for number in numbers:
        sum += int(number)
        count += 1
    average = sum / count
    print("Среднее арифметическое в колонке:", average)