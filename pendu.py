
word = input('Entrez le mot à trouver: ')


word = word.replace('é', 'e')
word = word.replace("à", 'a')
word = word.replace("è", 'e')
word = word.replace("ê", 'e')
word = word.replace("ë", 'e')


affichage  = ""
for i in word:
    affichage = affichage + '_ '

good_letter = ""
wrong_letter = 0
tentative = 0
while True:
    if '_' not in affichage:
        print('Mot trouvé')
        break
    if tentative == 7:
        print("C'est lose !")
        break
    print('Mot à deviner : \n'
          '' + affichage)
    while True:
        test_lettre = input('Entrez une lettre: ')
        if len(test_lettre) > 1:
            print("Entrez qu'une seule lettre")
        else:
            break
    if test_lettre in word:
        good_letter = good_letter + test_lettre

    elif not test_lettre in word:
        print('Pas de cette lettre')
        tentative += 1

    affichage = ''
    for i in word:
        if i in good_letter:
            affichage += i + " "
        else:
            affichage += '_ '



