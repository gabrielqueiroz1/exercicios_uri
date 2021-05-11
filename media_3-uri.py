N1, N2, N3, N4 = map(float, input().split())

media = (N1*2+N2*3+N3*4+N4*1)/10
print('Media: {:.1f}'.format(media))
if media >= 7:
    print('Aluno aprovado.')

elif media < 5:
    print('Aluno reprovado.')

elif 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: {:.1f}'.format(nota_exame))
    media2 = (nota_exame + media)/2
    if media2 >= 5.0:
        print('Aluno aprovado.')

    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media2))
