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
