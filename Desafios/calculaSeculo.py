ano = int(input("Digite o ano: "))

def calcSec(ano):
  sec = (ano%100)
  if sec > 0:
    seculo=int((ano/100))+1
  else:
    seculo=int(ano/100)
  return seculo

seculo_int = calcSec(ano)

def seculo_romano(seculo_int):
  numeros = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
  romanos = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
  i = 12
  numero_romano = ''
  while seculo_int != 0:
    if numeros[i] <= seculo_int:
      numero_romano += romanos[i]
      seculo_int = seculo_int - numeros[i]
    else:
      i -= 1
  return numero_romano 

print("Século ",seculo_romano(seculo_int))
