import json
import requests
import time
import math

#url = 'https://api.pi.delivery/v1/pi?start=0&numberOfDigits=5'

numberList = []
rangeMax = 999*999*999
end = False

'''

Para esta iteração, devemos perceber que ao criar o array, levamos em consideração que o último item de 9 dígitos que vamos analisar está
no índice [::-9], uma vez que não queremos itens com menos de 9 dígitos.

Já para o próximo bloco, a requisição será feita com step de 991 dígitos, para começar com o índice do último dígito do último item do último bloco +1.

Vejamos:    

    índice começa em 0;
    requisição do 0 ao 998
    primeiro item:  [0,8]
    último item:    [990,998]

    perceba que o indíce do primeiro algarismo do último item corresponde a [::-9]

    requisição do 991 ao  1989
    primeiro item:  [991,999]

    perceba que 991 = 990 + 1
        
'''
primesList = [2]

def isPrime(numberToCheck):
    isPrime = True
    found = False
    num = int(numberToCheck)
    numSqrtTop = math.floor(math.sqrt(num))+1
    for o in primesList:
        if o > numSqrtTop:
            isPrime = True
            found = True
            break

        if num%o == 0:
            isPrime = False
            break

    
    if isPrime and not found:
        beginIndex = primesList[(len(primesList)-1)]
        for i in range (beginIndex, numSqrtTop):
            addPrime = True
            if num%i == 0:
                isPrime = False
            
            for p in primesList:
                if i%p == 0:
                    addPrime = False
            
            if addPrime:
                primesList.append(i)
    
    return isPrime


print('=============================================================')
print('\n\n>>>Searching for first 9 digits palyndrome of pi...')

forTimeEnd      = 0
forTimeTotal    = 0
beginTime = time.perf_counter()

for start in range(0, rangeMax, 991):
    url = 'https://api.pi.delivery/v1/pi?start=' + str(start) + '&numberOfDigits=999'
    response = requests.get(url)
    string = json.loads(response.content)
    number = string['content']
    numberList = [number[i:i+9] for i in range(0, 991)]
    
    forTimeBegin = time.perf_counter()

    for item in numberList:
        if item == item[::-1]:
            print('checking {}...'.format(item))
            valid = isPrime(item)
            if valid:
                print('\n\n>>>{} is the first prime 9 digits palyndrome of pi!\n>index position at {}'.format(item, numberList.index(item) + 1 + start))
                end = True
                forTimeEnd = time.perf_counter()
                forTimeTotal += forTimeEnd - forTimeBegin
                break
            else:
                forTimeEnd = time.perf_counter()
                forTimeTotal += forTimeEnd - forTimeBegin

    
    if end:
        break

endTime = time.perf_counter()
totalTime = endTime - beginTime
print('\n>Execution time for palyndrome search: {}'.format(forTimeTotal))
print('\n>Total execution time: {}'.format(totalTime))