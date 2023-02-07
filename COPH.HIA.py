#Código para exercício proposto pelo Curso de Introdução a Ciência da Computação da USP-Coursera. Tem como principal objetivo checar se um texto é uma cópia de outro.

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    ''' Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    posicao = 0
    soma_diferencas = 0
    similaridade = 0

    while posicao <= 5:
        soma_diferencas = soma_diferencas + abs(as_a[posicao] - as_b[posicao])
        posicao = posicao + 1
    similaridade = soma_diferencas/6

    return similaridade

def calcula_assinatura(texto):
    ''' Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    tamanho_medio_palavras = 0
    frases = []
    palavras = []
    s = 1
    p = 1
    t = 0
    sent = 0
    fra = 0
    
    
    soma_dos_tamanhos_das_palavras = 0

    frases = separa_frases(sentencas[0])
    
    while s < len(sentencas):
        frases += separa_frases(sentencas[s])
        s = s + 1

    palavras = separa_palavras(frases[0])

    while p < len(frases):   
        palavras += separa_palavras(frases[p])
        p = p + 1

    #já tenho total de palavras

    tamanho_das_palavras = 0

    while t < len(palavras):
         tamanho_das_palavras += len(palavras[t])
         t = t + 1
   #já tenho total de caracteres

    caracteres_por_sentenca = 0
    while sent < len(sentencas):
        caracteres_por_sentenca += len(sentencas[sent])
        sent = sent + 1

    caracteres_por_frase = 0
    while fra < len(frases):
        caracteres_por_frase += len(frases[fra])
        fra = fra + 1
    
    numero_total_palavras = len(palavras)
    total_palavras_diferentes = n_palavras_diferentes(palavras)
    palavras_unicas = n_palavras_unicas(palavras)
    numero_total_sentencas = len(sentencas)
    numero_total_frases = len(frases)
    
    

    tamanho_medio_palavras = tamanho_das_palavras / numero_total_palavras
    
    relacao_type_token = total_palavras_diferentes / numero_total_palavras

    razao_hapax_legomana = palavras_unicas / numero_total_palavras

    tamanho_medio_sentencas = caracteres_por_sentenca/numero_total_sentencas

    complexidade_sentencas = numero_total_frases / numero_total_sentencas

    tamanho_medio_frases = caracteres_por_frase / numero_total_frases

    
    return [tamanho_medio_palavras, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentencas, complexidade_sentencas, tamanho_medio_frases]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    #essa função que vai dar para a função de comparação a variavel ass_a. Ela vai receber os textos, aplicar a função calcula assinatura e armazenar o resultado como ass_a
    texto = 0
    item = 0
    grau = 1
    assinatura = 0
    resultado = 0
    
    assinaturas = []
    similaridades = []
    texto_auxiliar = 0

    while texto < len(textos):
        assinatura = calcula_assinatura(textos[texto])
        assinaturas.append(assinatura)
        texto = texto + 1

    while item < len(assinaturas):
        similaridades.append(compara_assinatura(assinaturas[item], ass_cp))
        item = item + 1

    posic = 0
    posicao = 0
    posicao += similaridades[0]

    while grau < len(similaridades):
        if posicao > (similaridades[grau]):
            posicao = (similaridades[grau])
            posic = grau
        grau = grau + 1

    posic += 1
    
    return posic

def inicializacao():
    ass_b = []
    ass_b = le_assinatura()
    posic = 0
    
    textos = []
    textos = le_textos()

    posic = avalia_textos(textos, ass_b)

    print("O autor do texto ",posic," está infectado com COH-PIAH")
inicializacao()
