idade = int(input("Idade:"))
obeso = False
peso = float(input("Peso:"))
altura = float(input("Altura:"))
sexo = input("Sexo:")        
imc = peso / (altura * altura)

def abaixo():      
    print("Você está abaixo do peso")
def ideal():
    print("Você está com o peso ideal")
def pouco():
    print("Você está um pouco acima do peso")
def acima():
    print("Você está acima do peso")
def obeso():
    print("Você está com obesidade")
    obeso = True
    
def switch(case):
    if case == 'f' or case == 'F':
      if imc < 19.1:
        return abaixo
      elif imc < 25.8:
        return ideal
      elif imc < 27.3:
        return pouco
      elif imc < 31.1:
        return acima
      elif imc > 31.1:
        return obeso

    elif case == 'm' or case == 'M':
      if imc < 20.7:
        return abaixo
      elif imc < 26.4: 
        return ideal
      elif imc < 27.8: 
        return pouco;
      elif imc < 33.3: 
        return acima;
      elif imc > 33.3:
        return obeso

    else:
        return default

function = switch(sexo)
function()

if obeso and idade <= 12:
    print("Você também possui obesidade infantil")
