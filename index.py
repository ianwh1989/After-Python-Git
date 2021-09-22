# Repaso de listas
names = ['Marcos', 'Pedro', 'Cristian', 'Leandro', 'Adam', 'Darwin']

# Que tipo de dato esto mostrando (type())
print(type(names)) #printeo de que tipo es names

# Slicing
print(names[::2]) # muestro los nombres cada 2
print(names[3::]) # muestra del terce elemento hasta el final

# Mostrame los nombres usando for
for i in names: # declaro una variable (i) que recorra todos los elementos (lista de nombres) y los vaya mostrando (print())
    print(i)

# Instertar elemento en una lista (2 formas)
# 1- A travves de indices
names.insert(2, 'Franco') # llamo a la lista, indicandole que inserte en la posicion 2 a 'Franco'
print('\n\n', names)

# 2- Insertando a lo ultimo
names.append('Alejandro') # llamo a la lista, indicandole que inserte al final a 'Alejandro'
print('\n\n', names)

# Eliminar un elemento de la lista (2 formas)
# 1- Remove
names.remove('Franco')
print('\n\n', names)

# 2- pop
deleted = names.pop() # pop siempre elimina el ultimo elemento
print('Elemento eliminado (ultimo)', deleted)
print('\n\n', names)