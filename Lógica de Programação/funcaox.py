x = float(input("Digite um valor para X: "))

if (x <= 1):
    fx = 1
    print(fx)
elif (x >1) and (x<=2):
    fx = 2
    print(fx)
elif (x > 2) and (x <=3):
    fx = x ** 2
    print(fx)
else:
    fx = x**3

print("X: ", x)
print("f(x): {:.2f}".format(fx))
