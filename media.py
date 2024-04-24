# exercicio para resolver media de notas 

nota_1 = float(input("DIGITE A NOTA 1"))
nota_2 = float(input("DIGITE A NOTA 2"))

media = (nota_1 + nota_2) / 2

print(f" A NOTA FINAL É: {media} ")



#VERIFICAR SE A NOTA DO ALUNO E APROVADA OU REPROVADO COM A MEDIA MAIOR QUE 7

if media >= 7:
    print("VOCE FOI APROVADO")
else:
    print("VOCE FOI REPROVADO")