import Galya
from Galya import galya_afin_code, galya_afin_decode,galya_afin_rec_dencode,galya_afin_rec_encode

# поле Гаула для 27 символов и другие константы

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
alph_len = len(alphabet)

p_marks = [' ', '.', ',', '-', '"', "'", '!', '?', '(', ')', '_', '{', '}', '[', ']', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '%', '‘', '’']

def evklid_first(alpha, beta):
    if alpha > beta:
        a = alph_len
        b = beta
    else:
        a = alph_len
        b = alpha

    y2 = 0
    y1 = 1
    r = 100
    while r != 0:
        q = a // b
        r = a % b
        y = y2 - q * y1
        a = b
        b = r
        y2 = y1
        y1 = y
    if y2 < 0:
        return alph_len + y2
    else:
        return y2
def evklid_second_2(a, b):
    y2 = 0
    y1 = 1
    r = 100
    while r != 0:
        q = a // b
        r = a % b
        y = y2 - q * y1
        a = b
        b = r
        y2 = y1
        y1 = y
    if y2 < 0:
        return alph_len + y2
    else:
        return y2

def simple_code(text, change, uniq_letters):
    ch_text = text.upper()
    # uniq_letters = uniq_letters.split(' ')
    change = change.split(' ')
    result = list(ch_text)
    for i in range(len(result)):
        if result[i] in p_marks:
            result[i] = result[i]
        else:
            pos = uniq_letters.index(result[i])
            result[i] = change[pos]   
       
    return ''.join(result)
def simple_decode(text, key2, key1): #key1 - Alfavit
    result = list(text)
    for i in range(len(result)):
        if result[i] not in p_marks:
            pos = key2.index(result[i])
            result[i] = key1[pos]
        else:
            result[i] = result[i]

    return(''.join(result))

def afin_code(alpha, beta,text):

    if (alpha % beta != 0 and beta % alpha != 0 and alpha < alph_len and beta < alph_len):
        
        cypher = ''
        for i in text:
            if i not in p_marks:
                cypher += alphabet[(alpha * int(alphabet.index(i)) + beta) % alph_len]
            else:
                cypher+=i
        return cypher
    else:
        print("Выберите другие значенмия alpha и beta")
def afin_decode(alpha, beta,text):

    # obr_a = evklid_first(alpha,beta)
    obr_a = evklid_first(26, alpha)

    de_cypher = ''
    for i in text:
        if i not in p_marks:
            de_cypher += alphabet[(obr_a*(alphabet.index(i)-beta))%alph_len]
        if i in p_marks:
            de_cypher += i 
    return de_cypher

def rec_afin_encode(alpha1, beta1, alpha2, beta2,text):
    cypher = ''
    alpha_array = []
    beta_array = []
    if (alph_len % beta1 != 0 and alph_len % alpha1 != 0 and alph_len % alpha2 != 0 and alph_len %beta2  != 0 and alpha1 < alph_len and beta1 < alph_len and alpha2 < alph_len and beta2 < alph_len):
        if text[0] not in p_marks:
            cypher += alphabet[(alpha1 * int(alphabet.index(text[0])) + beta1) % alph_len]
        else:
            cypher+=text[0]
        if text[1] not in p_marks:
            cypher += alphabet[(alpha2 * int(alphabet.index(text[1])) + beta2) % alph_len]
        else:
            cypher+=text[1]
        alpha_array.append(alpha1)
        alpha_array.append(alpha2)
        beta_array.append(beta1)
        beta_array.append(beta2)
        for i in range(2,len(text)):
            if text[i] not in p_marks:

                alpha_i = (int(alpha_array[i-2]) * int(alpha_array[i-1])) % alph_len
                beta_i = (int(beta_array[i-2]) + int(beta_array[i-1])) % alph_len
                alpha_array.append(alpha_i)
                beta_array.append(beta_i)
                cypher+= alphabet[((alpha_i * int(alphabet.index(text[i]))) + beta_i) % alph_len]
            else:
                cypher+=text[i]
                alpha_array.append(alpha_i)
                beta_array.append(beta_i)
        return cypher

    else:
        print("Выберите другие значения alpha и beta")
def rec_afin_dencode(alpha1, beta1, alpha2, beta2,text):
    de_cypher = ''

    alpha_array = []
    beta_array = []
    obr_a_array = []

    obr_a1 = evklid_first(26, alpha1)
    obr_a2 = evklid_first(26, alpha2)
    if text[0] not in p_marks:
        de_cypher += alphabet[(obr_a1*(alphabet.index(text[0])-beta1))% alph_len]
    else:
        de_cypher += text[0]
    if text[1] not in p_marks:
        de_cypher += alphabet[(obr_a2*(alphabet.index(text[1])-beta2))% alph_len]
    else:
        de_cypher += text[1]

    alpha_array.append(alpha1)
    alpha_array.append(alpha2)

    beta_array.append(beta1)
    beta_array.append(beta2)

    obr_a_array.append(obr_a2)
    obr_a_array.append(obr_a1)
    for i in range(2,len(text)):
        if text[i] not in p_marks:
            alpha_i = (int(alpha_array[i - 2]) * int(alpha_array[i - 1])) % alph_len
            beta_i = (int(beta_array[i - 2]) + int(beta_array[i - 1])) % alph_len

            obr_a_i = evklid_second_2(alph_len,alpha_i)

            de_cypher += alphabet[(obr_a_i*(alphabet.index(text[i])-beta_i))% alph_len]

            alpha_array.append(alpha_i)
            beta_array.append(beta_i)
            obr_a_array.append(obr_a_i)
        else:
            de_cypher+=text[i]
            alpha_array.append(alpha_i)
            beta_array.append(beta_i)
            obr_a_array.append(obr_a_i)
    return(de_cypher)

def main():
    print('Выберите действие:\n1) выполнить шифрование с помощью простой замены\n2) выполнить дешифрование с помощью простой замены\n3) Выполнить зашифрование с помощью Афинного шифра \n4) Выполнить расшифрование с помощью Афинного шифра \n5) Выполнить зашифрование с помощью Афинного реккурентного шифра \n6) Выполнить расшифрование с помощью Афинного реккурентного шифра \n7) Тестирование программы и всех ее функций')
    choice = input()
    if choice == '1':
        print('Введите шифруемый текст:')
        text = input()
        # uniq_letters = []
        # ch_text = text.upper()
        # for i in ch_text:
        #     if i not in uniq_letters and i not in p_marks:
        #         uniq_letters.append(i)

        print('Уникальные символы в вашем тексте: (Алфавит)')
        uniq_letters = input().split(' ')
        print('Введите символы замены(через ПРОБЕЛ!):')
        change = input()
        print('Шифрованный текст ' + simple_code(text, change, uniq_letters))
    if choice == '2':
        print('Введите зашифрованный текст:')
        text = input()
        print('введите замененные буквы: ')
        key2 = input().split(' ')
        print('Введите изначальные буквы:')
        key1 = input().split(' ')
        print('Расшифрованный текст' + simple_decode(text,key2,key1))
    if choice == '3':
        print('введите alpha')
        alpha = int(input())
        print('введите beta')
        beta = int(input())
        print('Введите открытый текст:')
        text = input().upper()
        print('Шифрованный текст ' + afin_code(alpha, beta, text))
    if choice == '4':
        print('введите alpha')
        alpha = int(input())
        print('введите beta')
        beta = int(input())
        print('введите зашифрованный текст')
        text = input()
        print('Расшифрованный текст - ' + afin_decode(alpha, beta,text))
    if choice == '5':
        print('введите alpha 1')
        alpha1 = int(input())
        print('введите alpha 2')
        alpha2 = int(input())
        print('введите beta 1')
        beta1 = int(input())
        print('введите beta 2')
        beta2 = int(input())
        print('введите открытый текст')
        text = input()
        print('Зашифрованный текст - ' + rec_afin_encode(alpha1, beta1, alpha2, beta2,text))
    if choice == '6':
        print('введите alpha 1')
        alpha1 = int(input())
        print('введите alpha 2')
        alpha2 = int(input())
        print('введите beta 1')
        beta1 = int(input())
        print('введите beta 2')
        beta2 = int(input())
        print('введите зашифрованный текст')
        text = input()
        print('Открытый текст - ' + rec_afin_dencode(alpha1, beta1, alpha2, beta2,text))
    if choice == '7':
        print('Шифрование фразы - L0ND0N 1S TH3 CAP1TAL 0F GR3AT BR1TA1N')
        print('I) Перестановочный:\n1) перестановочные символы - L N D S T H C A P F G R B\n2) символы на которые переставляем - g H f a s D e R T y u I o \n3) ответ - ' + simple_code("L0ND0N 1S TH3 CAP1TAL 0F GR3AT BR1TA1N","g H f a s D e R T y u I o", "L N D S T H C A P F G R B".split(" ")))
        print('II) Аффинный шифр:\n1) Альфа - 5 \n2) бета - 7 \n3) зашифрованный текст - ' + afin_code(5,7,'L0ND0N 1S TH3 CAP1TAL 0F GR3AT BR1TA1N'))
        print('III) Аффинный рекурентный шифр:\n1) Альфа1 - 5, Альфа2 - 3 \n2) Бета1 - 7, Бета2 - 9\n3) Зашифрованный текст - ' + rec_afin_encode(5, 7, 3, 9, 'L0ND0N 1S TH3 CAP1TAL 0F GR3AT BR1TA1N'))
        print('Расшифрование:')
        print('I) Перстановочный - ' + simple_decode("g0Hf0H 1a sD3 eRT1sRg 0y uI3Rs oI1sR1H", "g H f a s D e R T y u I o","L N D S T H C A P F G R B"))
        print('II) Аффиный шифр - ' + afin_decode(5,7, 'K0UW0U 1T YQ3 RHE1YHK 0G LO3HY MO1YH1U'))
        print('II) Аффиный рекурентный шифр - ' + rec_afin_dencode(5, 7, 3, 9, 'K0DE0L 1C XV3 EQH1DCX 0D CL3OB RP1PU1B'))
  
main()

# print(crypto_first_analyz(text))
