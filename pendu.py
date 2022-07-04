
word = input('ENtrez le mot à trouver: ')
word = word.replace('é', 'e')
affichage = ""
for i in word:
    affichage = affichage + '_ '

print('Mot à deviner : \n'
      '' + affichage)

good_letter = ""
wrong_letter = 0
while True:

    test_lettre = input('Entrez une lettre: ')
    if test_lettre in word:
        good_letter += test_lettre

        print('Vous avez trouvé les lettres : ' + str(good_letter))
    else:
        print('Pas de cette lettre')

