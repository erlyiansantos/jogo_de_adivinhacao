alvo = 42
try:

  chute = int (input("Digite um número inteiro entre 0 e 100: "))

  if chute == alvo:
    print("Parabéns, você acertou!!")

  else:
    print ("Que pena, o número era "  + str(alvo))

except:

  print("valor informado não é um numero inteiro")