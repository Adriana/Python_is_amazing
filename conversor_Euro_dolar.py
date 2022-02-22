#programa que converte Euro --> Dólar  e Dólar --> Euro

#Recebe o input de Valor a ser convertido e input de opção para o tipo de conversão.
moeda = float(input('Entre com o valor para conversão : '))
escolha = input('Para qual moeda você quer converter? (1.Euros->Dolares ou 2. Dolares-> Euros) ') 

#Condição da opção escolhida pelo usuário
if escolha == "1" :
    cotacao_dolar = float(input('Entre com a cotação atual do Dólar: '))
    conversao_euro = moeda*cotacao_dolar
    print("$ {} Dólares  corresponde a €{} Euros".format(moeda, conversao_euro))
        
elif escolha != "1":
    cotacao_euro = float(input('Entre com a cotação atual do Euro: '))
    conversao_dolar= moeda*cotacao_euro
    print( "€ {} Euros  corresponde a $ {} Dólares".format(moeda, conversao_dolar))
        

    
    
