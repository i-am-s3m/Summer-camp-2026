
#déclaration d'une liste 

fruits  = ['banane','fraise',' orange ','pastèque','citron','framboise','fraise']


print (f"nous avons dans notre boutique {len(fruits)}  types de fruits dont les suivants : \n ",fruits)
print(f" '{fruits[0]}' est le premier type de fruits ")
print(f"'{fruits[len(fruits)-1]}' est le dernier type de fruits de la liste")
print (f"'{fruits[-2]}' est l'avant dernier type de fruit de la boutique  ")


#dépaquetage de la liste 
participants = ['Hamed','diallo','zié','malick','moko']
first_p, second_p, *rest , last_p= participants
print ('voici les resultats de la course:\n')
print(first_p,"est le premier ")
print(second_p,"est le second")
print(f"voici les exaequo:\n{rest}")
print(last_p,"est le dernier")


# exo de fins 

it_companies= ['Google','amazon','spotify','instagram', 'facebook','IBM','Apple']

print ( f'pendant notre enquête nous avons pu répertorier que {len(it_companies)} entreprises\n',f" { it_companies[0:3]} sont les 3 premières entreprises visitées\n",
       f"{it_companies[::2]} sont celles qui nous ont le plus marqué \n",
       f' nous donnerons nos avis dans l\'ordre suivant:\n \t {it_companies[::-1]} \n',
      )


# moification des certains elément de la listes
print (f'voici les entrprises:\n {it_companies}')


it_companies[2] ='tiktok'
print ( f"voici la mise a jours de la liste :\n {it_companies}" )

enterprise = str(input ( 'entrer le nom de l\'entreprise que vous rechercher:\n'))
       
print(enterprise in it_companies)

if enterprise in it_companies :
    print ('trouvé' )
else : 
    print ("désolé elle n'est pas dans notre base de donné")
    

# ajouter un elément à la liste 
Socity = str(input ( 'entrer le nom de l\'entreprise que vous vouler ajouter:\n'))
it_companies.append(Socity)
print(it_companies)
# inserer un élément dans la liste 
squat_cpnie = str(input ( 'entrer le nom de l\'entreprise que vous vouler inserer:\n'))
it_companies.insert(3,squat_cpnie)
print(it_companies)

# suppression des élément de la liste

print ("voici la liste final des enterprises :\n",it_companies) 

it_companies.remove('amazon')
it_companies.pop(-2)
del it_companies[3]

print(f'Après concertation nous avons retenu les entreprises suivantes: {it_companies}')


# concaténation des listes 

companies_and_fruits = it_companies + fruits 
print(companies_and_fruits) 
#  ou bien : 
it_companies.extend(fruits)
print (it_companies)
print (f" nous avons {fruits.count('fraise')} fois le fruit fraise  dans notre liste")


ages = [19, 22, 19, 24,19, 20, 25, 26, 24, 25, 24,26]

print(ages)
ages.sort()
print(ages)

print (f" le plus petits age est:{ages[0]} ans")

ages.sort(reverse=True)
print (f"le plus agé à {ages[0]} ans")

f_index = int (len (ages)//2) 
s_index = int (len (ages)//2) + 1
med = (ages[f_index] + ages[s_index] )/2
moy = sum (ages) / len (ages)
etendu = ages[len(ages)-1] - ages[0]
print (f'l\'age médiant est de {float (med)} ans\n',f'{float(moy)} ans est l\'age moyen\n et l\'etendu de {etendu}')


if abs (min(ages)-moy) == abs(max(ages)-moy) : 
    print("ecrat pareil")
else : 
    print('écart différent')


print( abs (min(ages)-moy) == abs(max(ages)-moy))