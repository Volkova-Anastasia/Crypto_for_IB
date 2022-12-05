from Cipher_all import afin_decode
from math import log10
from bigrams import bigramms_count, bigramms_frequency, bigramms_count_freq
import regex as re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
alphabetlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_len = len(alphabet)
symbols_occurrence = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 6.33, 9.06, 2.76,0.98, 2.36,0.15, 1.97, 0.05]
p_marks = [' ', '.', ',', '-', '"', "'", '!', '?', '(', ')', '_', '{', '}', '[', ']', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '%', '‘', '’']
alfa_massive = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] # 12
cipher_text = 'HQSHUNTJFURTQFNHOJNFTUNTHGTGTJPOMFUZFUAGXOXUZTQOFWTJAHUJKPMMCTGTFJHLUXNLXUTWWTNMWXGAPKOFNCTHOMCJTGSFNTJVFMCRHUBCXJAFMHOJJMGPZZOFUZMXNXATVFMCHUHZFUZAXAPOHNTRHUBNXPUMGFTJTUIXBMCTKTUTWFMJXWWGTTXGJPKJFQFJTQUHMFXUHOAPKOFNCTHOMCJTGSFNTJCXVTSTGMCTGTHGTJXRTVFMCFUJTUFXGCTHOMCRHUHZTRTUMVCXNOHFRMCHMJPNCAGXSFJFXUVFOOKTNXRTPUJPJMHFUHKOTHUQFWFGROBHZGTTMCHMNCHUZTJUTTQMXKTRHQTFUXGQTGMXGTWOTNMMCFJNCHUZFUZGTHOFMBQTJAFMTMCTUXMFXUMCHMCTHOMCNHGTJCXPOQKTWGTTJPNCNHGTFJAGTQXRFUHUMOBWPUQTQKBMCTMHYAHBTGMXZFSTHJATNFWFNTYHRAOTHGTNTUMGTAXGMFURBNXPUMGBTJMHKOFJCTQMCHMHORXJMXWMCTUHMFXUJMHYJATUQFUZFJQFJMGFKPMTQMXCTHOMCNHGTHUQJXRTXWMCHMWFZPGTFJGTJTGSTQWXGMGTHMFUZMCTTOQTGOBMCFJFJHQFJAGXAXGMFXUHMTHRXPUMXWRXUTBVCFNCCHJZGTHMOBFUNGTHJTQMCTKPGQTUXUMCTJMHMTHUQTYFJMFUZWPUQFUZFJUXOXUZTGJPWWFNFTUMMXRTTMMCTJTUTTQJMCFJFUMPGUFRAHNMJXUMCTJMHUQHGQXWNHGTMCHMNHUKTAGXSFQTQHJJCXVUKBUPRTGXPJUTZHMFSTRTQFHGTAXGMJHKXPMMCTNXUQFMFXUJWXGKXMCJMHWWHUQAHMFTUMJFWVTVHUMDPHOFMBCTHOMCNHGTMCTUNOTHGOBMCFJWFUHUNFHOKPGQTUUTTQJMXKTHOOTSFHMTQXUTVHBMXQXJXVXPOQKTMXFUNGTHJTMCTNXUMGFKPMFXUJRHQTKBNFMFETUJMCGXPZCFUNGTHJTQMHYHMFXUHOMTGUHMFSTOBZXSTGURTUMJNXPOQTUNXPGHZTMCXJTVCXNHUHWWXGQFMMXMHLTPAAGFSHMTCTHOMCNHGTHGGHUZTRTUMJKBJVFMNCFUZMXHAGFSHMTRXQTOMCTVTOOXWWNHUHWWXGQHCFZCTGDPHOFMBXWNHGTVCFOTHMMCTJHRTGTOFTSFUZAGTJJPGTXUAPKOFNJTGSFNTJWXGMCXJTVCXQXUXMCHSTMCTRTHUJMXZXAGFSHMTXUTMCFUZFJWXGNTGMHFUHUHZTFUZAXAPOHMFXUCHJFUNGTHJTQMCTAGTJJPGTXUTYFJMFUZCTHOMCAGXSFJFXUFWVTHGTZXFUZMXRHFUMHFUMCTJMHUQHGQJXWCTHOMCNHGTMCHMVTHGTPJTQMXRXGTWPUQFUZUTTQJMXKTWXPUQTFMCTGMCGXPZCMHYHMFXUHUQHOMTGUHMFSTWXGRJXWAGXSFJFXUJCXPOQKTNXUJFQTGTQXMCTGVFJTJMHUQHGQJVFOOWHOOHUQATXAOTJOFSTJVFOOKTAPMHMGFJL'

# def Caesar(cipher_text, beta):
#     final = ''
#     for p in cipher_text:
#         place = alphabetlist.find(p)
#         new_place = (place + beta) % 26
#         if p in alphabet:
#             final += alphabetlist[new_place]
#         else:
#             final += p
#     return final

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

def afin_decode(alpha, beta, text):
    obr_a = evklid_first(26, alpha)
    de_cypher = ''
    for i in text:
            de_cypher += alphabet[(obr_a*(alphabet.index(i)-beta)) % alph_len]
    return de_cypher

#Считаем рейтинг биграмм для шифртекста
for i in range(1, len(cipher_text)): #Считаю количество различных биграмм в своем шифртексте
    bigramms_count[cipher_text[i-1] + cipher_text[i]] = bigramms_count[cipher_text[i-1] + cipher_text[i]] + 1
for q, j in bigramms_count.items(): # Считаю частоту встречаемости каждой биграммы в тексте
    bigramms_count[q] = bigramms_count[q] / len(cipher_text)

Count_rating_bigramm = 0
for k, i in bigramms_count.items(): # Считаю рейтинг биграмм для Шифртекста (1)
    if bigramms_count[k] != 0:
        Count_rating_bigramm = Count_rating_bigramm + log10(bigramms_count[k])
    else:
        Count_rating_bigramm = Count_rating_bigramm + log10(0.001)

for i in range(1, len(cipher_text)): #Считаю количество различных биграмм в своем шифртексте
    bigramms_count[cipher_text[i-1] + cipher_text[i]] = 0
# for q, j in bigramms_count.items(): # Считаю частоту встречаемости каждой биграммы в тексте
#     bigramms_count[q] = 0
print('Изначальный рейтинг биграмм -  ', Count_rating_bigramm)

def bigrams_af(cipher_text):
    new_rating_bigramm = 0
    for i in range(1, len(cipher_text)): #Считаю количество различных биграмм в своем шифртексте
        bigramms_count[cipher_text[i-1] + cipher_text[i]] = bigramms_count[cipher_text[i-1] + cipher_text[i]] + 1
    # print(bigramms_count)

    for q, j in bigramms_count.items(): # Считаю частоту встречаемости каждой биграммы в тексте
        bigramms_count[q] = bigramms_count[q] / len(cipher_text)
    print(bigramms_count)
    for k, z in bigramms_count.items(): # Считаю рейтинг биграмм для Шифртекста
        if bigramms_count[k] != 0:
            new_rating_bigramm = new_rating_bigramm + log10(bigramms_count[k])
        else:
            new_rating_bigramm = new_rating_bigramm + log10(0.001)
    print('New Rating - ', new_rating_bigramm)
    for i in range(1, len(cipher_text)): #Считаю количество различных биграмм в своем шифртексте
        bigramms_count[cipher_text[i-1] + cipher_text[i]] = 0
    print(bigramms_count)
    # for q, j in bigramms_count.items(): # Считаю частоту встречаемости каждой биграммы в тексте
    #     bigramms_count_freq[q] = 0
    # print(bigramms_count_freq)
    return new_rating_bigramm

for beta in range(0, 25):
    print(beta)
    for i in range(len(alfa_massive)):
        print(alfa_massive[i])
        cipher_text = afin_decode(alfa_massive[i], beta, cipher_text)
        # print(cipher_text)
        bigrams_work = bigrams_af(cipher_text)
        if bigrams_work > Count_rating_bigramm:
            Count_rating_bigramm = bigrams_work
            alfa_found = alfa_massive[i]
            beta_found = beta
            final_text = cipher_text

print(alfa_found)
print(beta_found)
print(final_text)
print(Count_rating_bigramm)
# print(afin_decode(3, 7, 'HQSHUNTJFURTQFNHOJNFTUNTHGTGTJPOMFUZFUAGXOXUZTQOFWTJAHUJKPM'))
