# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:39:09 2022

@author: Adrian
"""

import string 

alfabeto = list(string.ascii_lowercase)


def cifradoCesar(alfabeto,n,texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar >= 26:
                indice_cesar -= 26
            texto_cifrado += alfabeto[indice_cesar]
        else: 
            texto_cifrado += letra
    
    return texto_cifrado

frase = "hola a todos, este es un codigo de python"
frase_cifrada = cifradoCesar(alfabeto,3, frase)
print(frase_cifrada)

def decifrarCesar(alfabeto,n,texto):
    texto_decifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual - n
            if indice_cesar >= 26:
                indice_cesar -= 26
            texto_decifrado += alfabeto[indice_cesar]
        else: 
            texto_decifrado += letra
    
    return texto_decifrado

frase_decifrada = decifrarCesar(alfabeto, 3, frase_cifrada)
print(frase_decifrada)
