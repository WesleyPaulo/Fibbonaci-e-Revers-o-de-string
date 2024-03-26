
 # defino a função
def Fibonacci(valor):
    #inicia as duas primeiras variáveis da sequência de Fibonacci
    a = 0
    b = 1
    
    # Inicia a variável soma para armazenar o próximo número da sequência de Fibonacci e o contador para acompanhar a posição na sequência.
    soma = 0
    contador = 2
    
    while True:
        
        # Calcula o próximo número da sequência de Fibonacci 
        soma = a + b
        
        # Incremena o contador
        contador += 1
        
        # Atualiza os valores das variáveis a e b para os próximos cálculos
        a = b
        b = soma
        
        
        # Verifica se o número da sequência excede o valor dado, se sim impreme que não pertence e retorna 0
        if(soma > valor):
            print("Valor não pertence a Fibonacci")
            return 0
        
        # Verifica se o número da sequência é igual o valor dado, se sim impreme que pertence, diz em que posição ele é e retorna o valor dele
        elif(soma == valor):
            print(soma, " é o ", contador ,"º número de fibonacci")
            return


valor = input("Digite um inteiro: ")
Fibonacci(int(valor))

    
    