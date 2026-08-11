print ("====There is the python challenge====")

print ('Days\tTopics\tExercises')
print('1\t5\t5')
print('2\t6\t20')
print('3\t5\t23')
print('4\t1\t35')

print('===Unpacking of name :eliphaz ====')
name ='eliphaz'
a,b,c,d,e,f,g = name
for letter in name: 
    print (letter)

first_4 = name [0:4]
last_5 = name [-5:]
print(f"the first 4 letters of the name are : {first_4}" )
print(f"the first 5 letters of the name are : {last_5}" )



name = 'sem'

for i in range (0,len(name)): 
 print (name[i]) 

last_letter = name[-1]
penultimate_letter = name[-2]
fist_letter = name[0]
print (f'the last letter of your name is: {last_letter}')
print (f'the penultimate letter of your name is: {penultimate_letter}')
print (f'the first letter of your name is: {fist_letter}')


#inversion d'un chaine de caractère 

print (" \t===inversion d'une chaine de charactère===")
greeting = 'Hello, World!'
print(greeting)
print(greeting[::-1]) # !dlroW ,olleH

# saut de charactère lors du découpage 

language = 'Python'
cut  = language[::2] 
print (language)
print (cut) 

print ("====Méthode de chaine ======") 

phrase ='thirty\tdays\tof\tpython'

print (phrase.capitalize())
print ("le nombre de 't' dans la phrase est :",phrase.count('t',0,20))
print ("la phrase se termine par les lettres :'on'?\n ",phrase.endswith('on'))
print ("la phrase se termine t'elle par les lettres 'ssu'?\n ",phrase.endswith('ssu'))
print (phrase.capitalize().expandtabs(10))

print (f'''le premier "o" se trouve a  l'indice N°{phrase.find('o')}''') 
print (f'''Le premier "th" se trouve à l'indice N°{phrase.find('th')}''')
print (f'''le dernier 'th' se trouve à l'indice N°{phrase.rfind('th')}''')

#formatage de chaine 
print ('{n} is the fucking {g}'.format(n='Sem' ,g= 'GOAT'))
sub_string = 'ty'
print ("le terme 'ty' se trouve a l'indice {n}".format(n=str( phrase.index(sub_string))))

print (" \n=====les méthode de verification booléene====\n ")

print (f"est ce que  'ThirtyDaysofpython' contient des espace? :\n{'ThirtyDaysofpython'.isalnum()} ")
print (f"est ce que 'ThirtyDaysofpython' contient des lettres ?:\n{'ThirtyDaysofpython'.isalpha()} " )
print ( f"est ce que '12324' sont des chiffre ?:\n {'1234'.isdecimal()}")
print (f"est ce que '30' est un digit?:\n{'30'.isdigit()} ")
print (f"est ce que 'thirty_days_of_python' est un bon nom de variable ?\n {'thirty_days_of_python' .isidentifier()} ")
print (f"le terme ' THIRTY DAYS ' est il en majuscule ? :\n {'THIRTY DAYS'.isupper()} ")


# assemblage et separation de chaine 


web_tech = ['HTML', 'CSS', 'JavaScript']
print(' '.join(web_tech))    # 'HTML CSS JavaScript'
print('-'.join(web_tech))    # 'HTML-CSS-JavaScript'
print('_'.join(web_tech))    # 'HTML_CSS_JavaScript'


# split , replace , and strip 

print ('  thirty days  '.strip())               # 'thirty days'  → enlève espaces début/fin
print('thirty days of python'.replace('python', 'coding') ) # remplace une sous-chaîne
print ('thirty days of python'.split())         # ['thirty', 'days', 'of', 'python']  → coupe sur les espaces par défaut
print ('a, b, c'.split(', ') )                  # ['a', 'b', 'c']  → coupe sur un séparateur précis


print('thirty days'.title())      # 'Thirty Days'  → majuscule à chaque mot
print('Thirty Days'.swapcase() )  # 'tHIRTY dAYS'  → inverse chaque casse
print('thirty days'.startswith('thirty'))  # True pour savoir si la structure de chaine commence par la sous chaine demandé 
