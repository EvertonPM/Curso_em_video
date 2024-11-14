numeros=('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
x=int(input("digite um numero entre 0 e 20: "))
while x<0 or x>20:
    x = int(input("Tente dnv, digite um numero entre 0 e 20: "))
print(f"Voce digitou o numero {numeros[x-1]}")