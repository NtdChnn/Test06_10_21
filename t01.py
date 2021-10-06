weight, height = input(" *** BMI ***\nEnter your weight(kg) and height(m) : ").split(' ')
BMI = float(weight)/(float(height)*float(height))
print('Your status is : ',end='')
if BMI < 18.5:
    print('Below normal weight.')
elif BMI < 25:
    print('Normal weight.')
elif BMI < 30:
    print('Overweight.')
elif BMI < 35:
    print('Case I Obesity.')
elif BMI < 40:
    print('Case II Obesity.')
else:
    print('Case III Obesity.')