from gettext import translation


#%%diccionario desde el principio hecho

beatles = {
    "bass":"Paul",
    "guitar":"George",
    "vocals":"John",
    "drums":"Ringo",
    "members": 4,
    "are_they_cool": True
}

print(beatles["members"])

#iterar sobre diccionario
for key in beatles:
    print(key) #imprime la clave
    print(beatles[key])#imprime el valor
    
#%%diccionario creado de cero
empty_dict={}
empty_dict["beatle1"]="Paul"
#print(empty_dict["beatle1"])


#%%para updatear un valor en el diccionario sobreescribimos y ya
empty_dict["beatle1"]="Clara"
#print(empty_dict["beatle1"])

#%%para quitar un valor en el diccionario usamos pop
#beatles.pop("beatle1")

#%%lista
vegetables=["potato", "tomato"]
#print(vegetables[1])

for vegetable in vegetables:
    #print(vegetable)

	index=0
while(index<len(vegetables)):
    #print(vegetables[index])
    index=index+1