"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
from collections import defaultdict


def load_data (file_csv):
    data=[]
    
    with open(file_csv, newline='') as csvfile:
        #read_csv = csv.reader(csvfile)
        
        for row in csvfile:
            row = row.strip().replace('\t',' ').split(' ')
            data.append(row)
                
    return data

data=(load_data('data.csv'))


def pregunta_01():

    data2=[]
    cont=0

    for element in data: 
        if len(element)>=4:
            data2.append(int(element[1]))

    for element in data2:
        cont+=element

    return cont

#Answer_1=print(pregunta_01(data))


def pregunta_02():

    data1=[]         #Pone en lista sólo las letras necesarias
    letters=[]       #Sólo pone una letra de cada una de las que aparece en data3
    cont=[]          #Contiene la cantidad de veces que se repite cada letra en el mismo orden de la lista letters

    for element in data: 
        data1.append(element[0])
    
    for element in data1:
        if element not in letters: 
            letters.append(element)

    letters=sorted(letters)    #Organiza las letras en orden alfabético

    for element in letters: 
        cont.append(data1.count(element))
    
    A2=list(zip(letters,cont))

    return A2

#Answer_2=print(pregunta_02(data))


def pregunta_03():
    
    data1=[]  
    data2=[]
    sum=[]

    for element in data: 
        data1.append(element[0:2])
        if element[0] not in data2:
            data2.append(element[0])
    
    data2=sorted(data2)
    
    for element in data2:
        cont=0
        numbers=[tuple[1] for tuple in data1 if tuple[0]==element]
        for element in numbers:
            cont+=int(element)
        sum.append(cont)
    
    A3=list(zip(data2,sum))

    return A3

#Answer_3=print(pregunta_03(data))


def pregunta_04():
    
    data1=[]      #Lista con todas las fechas completas
    months=[]     #Lista con todos los meses
    months2=[]    #Lista con los meses sólo una vez
    cont=[]       #Lista con los conteos por mes
    
    for element in data: 
        data1.append(element[2])
    
    for element in data1:
        lista = list(element.split('-'))
        months.append(lista[1])

    for element in months:
        if element not in months2:
            months2.append(element)
    
    months2=sorted(months2)       #Lista organizada de menor a mayor 

    for element in months2: 
        cont.append(months.count(element))
    
    A4=list(zip(months2,cont))
    
    return A4

#Answer_4=print(pregunta_04(data))


def pregunta_05():
    
    data1=[]       #Datos con letra y número
    data2=[]       #Sólo letra
    minimum=[]     #Contiene todos los mínimos
    maximum=[]     #Contiene todos los máximos

    for element in data: 
        data1.append(element[0:2])
        if element[0] not in data2:
            data2.append(element[0])
    
    data2=sorted(data2)    #Letras organizadas alfabéticamente
    
    for element in data2:
        numbers=[tuple[1] for tuple in data1 if tuple[0]==element]
        minimum.append(int(min(numbers)))
        maximum.append(int(max(numbers)))
    
    A5=list(zip(data2,maximum,minimum))

    return A5

#Answer_5=print(pregunta_05(data))

def pregunta_06():
    
    data1=[]
    dic={} 
    results=[]
    
    for element in data: 
        data1.append(element[-1].split(','))

    for element in data1:
        for i in element:
            key,value=i.split(':')       #Procesar cada par de clave y valor
            value=int(value)

            if key not in dic:
                dic[key]={'min':value,'max':value}            #Si es la primera vez que se encuentra la clave
            else:
                dic[key]['min']=min(dic[key]['min'],value)    #Si la clave ya está, se actualiza el mínimo y el máximo
                dic[key]['max']=max(dic[key]['max'],value)
    
    for key, values in sorted(dic.items()):                   #Para ordenar el elemento a imprimir
        key=str(key)
        minimum=values['min']
        maximum=values['max']
        A6='("{}", {}, {})'.format(key,minimum,maximum)
              
        results.append(eval(A6))

    return results
    
#Answer_6=print(pregunta_06(data))


def pregunta_07():

    letters_values=defaultdict(list)      #Almacena las listas de letras por cada valor de la columna 1

    for element in data: 
        letters=element[0]
        numbers=int(element[1])
        letters_values[numbers].append(letters)
    
    A7=sorted(letters_values.items())     #Ordena los elementos de la lista de acuerdo al valor de la columna 1.
    return A7
    
#Answer_7=print(pregunta_07(data))


def pregunta_08():

    letters_values=defaultdict(set)     

    for element in data: 
        letters=element[0]
        numbers=int(element[1])
        letters_values[numbers].add (letters)
    
    A8=sorted ((numbers, sorted(letters)) for numbers, letters in letters_values.items())     #Convierte los conjuntos de letras en listas ordenadas y sin duplicados
    return A8

#Answer_8=print(pregunta_08(data))


def pregunta_09():

    keys_count=defaultdict(int)

    for element in data:
            text=element[-1]
            couple=text.split(',')

            for i in couple:
                key, _ = i.split(':')
                keys_count[key] += 1
    
    A9=dict(keys_count)
    A9=dict(sorted(A9.items()))

    return A9

#Answer_9=print(pregunta_09(data))
    

def pregunta_10():
    
    data1=[]

    for element in data:
        letter=element[0]
        count_col3=len(element[3].split(','))
        count_col4=len(element[4].split(','))

        A10='("{}", {}, {})'.format(letter,count_col3,count_col4)
        data1.append(eval(A10))

    return data1

#Answer_10=print(pregunta_10(data))


def pregunta_11():
    
    summation=defaultdict(int)             #Diccionario para acumular las sumas por cada letra de la columna 4. 

    for element in data:
        number=int(element[1])
        letters=element[3].split(',')

        for i in letters:
            summation[i]+=number
    
    A11=dict(sorted(summation.items()))   #Ordena alfabéticamente las letras de la columna 4.
    
    return A11

#Answer_11=print(pregunta_11(data))


def pregunta_12():

    summ_key={}

    for element in data:
        letter=element[0]
        couple=element[-1].split(',')

        for i in couple:
            key,value = i.split(':')
            value=int(value)
            
            if letter in summ_key:
                summ_key[letter]+=value
            else:
                summ_key[letter]=value
    
    A12=dict(sorted(summ_key.items()))   #Ordena alfabéticamente las letras de la columna 1.
   
    return A12

#Answer_12=print(pregunta_12(data))