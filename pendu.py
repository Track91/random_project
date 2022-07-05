
word = input('ENtrez le mot à trouver: ')
word = word.replace('é', 'e')
affichage = ""
for i in word:
    affichage = affichage + '_ '



good_letter = ""
wrong_letter = 0
while True:
    print('Mot à deviner : \n'
          '' + affichage)

    test_lettre = input('Entrez une lettre: ')[0:1].lower()

    if test_lettre in word:
        good_letter = good_letter + test_lettre

    elif not test_lettre in word:
        print('Pas de cette lettre')

    if good_letter in word:
        print('Mot trouvé')
    affichage = ''
    for i in word:
        if i in good_letter:
            affichage += i + " "
        else:
            affichage += '_ '


