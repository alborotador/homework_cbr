# Problem #4. Сессия и редбулл
# В первый день сессии студент с 1 курса выпил редбулл (250 мл).
# Однако на следующий день он понял, что такого количества не хватает
# для освоения микроэкономики и питона, и стал пить ежедневно на 150 мл больше.
# На какой день студент выпьет больше, чем литр? Сколько миллилитров он выпьет
# за это время? Подсказка: нужно изначально сделать две переменных-счетчика


V = 250  # The volume of the drink
days = 1  # Amount of days
drink = 150  # Drink another 150 ml per day
total = 0  # Total drunk

while V <= 1000:
    total = total + V
    V = V + drink
    
    days += 1
    
       
print(days)
print(total)
