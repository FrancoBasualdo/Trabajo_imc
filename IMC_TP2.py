peso = float(input("Ingrese su peso en kg:  "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso /(altura * altura)
print(f'Su indice de masa corporal es:\n{imc}')

if (imc < 18.5):
 print("Tiene peso bajo de lo normal¡¡")
elif( imc > 18.6 and imc < 24.9):

    print("Tiene peso normal¡¡")

elif( imc > 25.0 and imc < 29.0):
 print("Tiene exceso de Peso¡¡")
elif(imc > 30.0):{
    print("Tiene obesidad¡¡")
}