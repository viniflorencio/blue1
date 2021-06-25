def valores (num1,num2):
    if num1 < num2:
        return num1
    elif num1 > num2:
        return num2
    else:
        return num1,num2

resp1 = float(input('escolha um numero: '))
resp2 = float(input('escolha outro numero: '))

final = valores(resp1,resp2)

print(final)
