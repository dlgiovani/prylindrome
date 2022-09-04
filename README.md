# prylindrome
A code to get the first prime 9 digits palyndrome sequence of numbers from pi.

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
