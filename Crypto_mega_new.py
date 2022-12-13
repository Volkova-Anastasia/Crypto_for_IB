# from Cipher_all import simple_decode, simple_code
from math import log10
from bigrams import bigramms_count, bigramms_freq
import regex as re
from collections import Counter
import random

alfa_massive = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] # 12
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
alph_len = len(alphabet)
symbols_occurrence = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 6.33, 9.06, 2.76,0.98, 2.36,0.15, 1.97, 0.05]
p_marks = [' ', '.', ',', '-', '"', "'", '!', '?', '(', ')', '_', '{', '}', '[', ']', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '%', '‘', '’']
#text for first
# text = 'QRCQFETLOFDTROEQSLEOTFETQKTKTLXSZOFUOFHKGSGFUTRSOYTLHQFLWXZZITKTOLQAFGEAGFTYYTEZYGKHXWSOEITQSZILTKCOETLVOZIDQFNIGLHOZQSLLZKXUUSOFUZGEGHTVOZIQFQUOFUHGHXSQETDQFNEGXFZKOTLTFPGNZITWTFTYOZLGYYKTTGKLXWLOROLTRFQZOGFQSHXWSOEITQSZILTKCOETLIGVTCTKZITKTQKTLGDTVOZIOFLTFOGKITQSZIDQFQUTDTFZVIGESQODZIQZLXEIHKGCOLOGFVOSSWTEGDTXFLXLZQOFQWSTQFROYOKDSNQUKTTZIQZEIQFUTLFTTRZGWTDQRTOFGKRTKZGKTYSTEZZIOLEIQFUOFUKTQSOZNRTLHOZTZITFGZOGFZIQZITQSZIEQKTLIGXSRWTYKTTLXEIEQKTOLHKTRGDOFQFZSNYXFRTRWNZITZQBHQNTKZGUOCTQLHTEOYOETBQDHSTQKTETFZKTHGKZOFDNEGXFZKNTLZQWSOLITRZIQZQSDGLZGYZITFQZOGFLZQBLHTFROFUOLROLZKOWXZTRZGITQSZIEQKTQFRLGDTGYZIQZYOUXKTOLKTLTKCTRYGKZKTQZOFUZITTSRTKSNZIOLOLQROLHKGHGKZOGFQZTQDGXFZGYDGFTNVIOEIIQLUKTQZSNOFEKTQLTRZITWXKRTFGFZITLZQZTQFRTBOLZOFUYXFROFUOLFGSGFUTKLXYYOEOTFZZGDTTZZITLTFTTRLZIOLOFZXKFODHQEZLGFZITLZQFRQKRGYEQKTZIQZEQFWTHKGCORTRQLLIGVFWNFXDTKGXLFTUQZOCTDTROQKTHGKZLQWGXZZITEGFROZOGFLYGKWGZILZQYYQFRHQZOTFZLOYVTVQFZJXQSOZNITQSZIEQKTZITFESTQKSNZIOLYOFQFEOQSWXKRTFFTTRLZGWTQSSTCOQZTRGFTVQNZGRGLGVGXSRWTZGOFEKTQLTZITEGFZKOWXZOGFLDQRTWNEOZOMTFLZIKGXUIOFEKTQLTRZQBQZOGFQSZTKFQZOCTSNUGCTKFDTFZLEGXSRTFEGXKQUTZIGLTVIGEQFQYYGKROZZGZQATXHHKOCQZTITQSZIEQKTQKKQFUTDTFZLWNLVOZEIOFUZGQHKOCQZTDGRTSZITVTSSGYYEQFQYYGKRQIOUITKJXQSOZNGYEQKTVIOSTQZZITLQDTKTSOTCOFUHKTLLXKTGFHXWSOELTKCOETLYGKZIGLTVIGRGFGZIQCTZITDTQFLZGUGHKOCQZTGFTZIOFUOLYGKETKZQOFQFQUTOFUHGHXSQZOGFIQLOFEKTQLTRZITHKTLLXKTGFTBOLZOFUITQSZIHKGCOLOGFOYVTQKTUGOFUZGDQOFZQOFZITLZQFRQKRLGYITQSZIEQKTZIQZVTQKTXLTRZGDGKTYXFROFUFTTRLZGWTYGXFRTOZITKZIKGXUIZQBQZOGFQFRQSZTKFQZOCTYGKDLGYHKGCOLOGFLIGXSRWTEGFLORTKTRGZITKVOLTLZQFRQKRLVOSSYQSSQFRHTGHSTLSOCTLVOSSWTHXZQZKOLA'
#text for second
# text = 'HWIHURBTVUPBWVRHKTRVBURBHOBOBTDKYVULVUEOZKZULBWKVGBTEHUTMDYYQBOBVTHFUZRFZUBGGBRYGZOEDMKVRQBHKYQTBOIVRBTNVYQPHUXQZTEVYHKTTYODLLKVULYZRZEBNVYQHUHLVULEZEDKHRBPHUXRZDUYOVBTBUAZXYQBMBUBGVYTZGGOBBZOTDMTVWVTBWUHYVZUHKEDMKVRQBHKYQTBOIVRBTQZNBIBOYQBOBHOBTZPBNVYQVUTBUVZOQBHKYQPHUHLBPBUYNQZRKHVPYQHYTDRQEOZIVTVZUNVKKMBRZPBDUTDTYHVUHMKBHUWVGVOPKXHLOBBYQHYRQHULBTUBBWYZMBPHWBVUZOWBOYZOBGKBRYYQVTRQHULVULOBHKVYXWBTEVYBYQBUZYVZUYQHYQBHKYQRHOBTQZDKWMBGOBBTDRQRHOBVTEOBWZPVUHUYKXGDUWBWMXYQBYHSEHXBOYZLVIBHTEBRVGVRBSHPEKBHOBRBUYOBEZOYVUPXRZDUYOXBTYHMKVTQBWYQHYHKPZTYZGYQBUHYVZUTYHSTEBUWVULVTWVTYOVMDYBWYZQBHKYQRHOBHUWTZPBZGYQHYGVLDOBVTOBTBOIBWGZOYOBHYVULYQBBKWBOKXYQVTVTHWVTEOZEZOYVZUHYBHPZDUYZGPZUBXNQVRQQHTLOBHYKXVUROBHTBWYQBMDOWBUZUYQBTYHYBHUWBSVTYVULGDUWVULVTUZKZULBOTDGGVRVBUYYZPBBYYQBTBUBBWTYQVTVUYDOUVPEHRYTZUYQBTYHUWHOWZGRHOBYQHYRHUMBEOZIVWBWHTTQZNUMXUDPBOZDTUBLHYVIBPBWVHOBEZOYTHMZDYYQBRZUWVYVZUTGZOMZYQTYHGGHUWEHYVBUYTVGNBNHUYJDHKVYXQBHKYQRHOBYQBURKBHOKXYQVTGVUHURVHKMDOWBUUBBWTYZMBHKKBIVHYBWZUBNHXYZWZTZNZDKWMBYZVUROBHTBYQBRZUYOVMDYVZUTPHWBMXRVYVCBUTYQOZDLQVUROBHTBWYHSHYVZUHKYBOUHYVIBKXLZIBOUPBUYTRZDKWBURZDOHLBYQZTBNQZRHUHGGZOWVYYZYHFBDEEOVIHYBQBHKYQRHOBHOOHULBPBUYTMXTNVYRQVULYZHEOVIHYBPZWBKYQBNBKKZGGRHUHGGZOWHQVLQBOJDHKVYXZGRHOBNQVKBHYYQBTHPBOBKVBIVULEOBTTDOBZUEDMKVRTBOIVRBTGZOYQZTBNQZWZUZYQHIBYQBPBHUTYZLZEOVIHYBZUBYQVULVTGZORBOYHVUHUHLBVULEZEDKHYVZUQHTVUROBHTBWYQBEOBTTDOBZUBSVTYVULQBHKYQEOZIVTVZUVGNBHOBLZVULYZPHVUYHVUYQBTYHUWHOWTZGQBHKYQRHOBYQHYNBHOBDTBWYZPZOBGDUWVULUBBWTYZMBGZDUWBVYQBOYQOZDLQYHSHYVZUHUWHKYBOUHYVIBGZOPTZGEOZIVTVZUTQZDKWMBRZUTVWBOBWZYQBONVTBTYHUWHOWTNVKKGHKKHUWEBZEKBTKVIBTNVKKMBEDYHYOVTF'
#text fo third
# text = 'HSTZCCBTIYVSKFSRMEPTEWBUVWAADSTGTRQUVYRYHPVEOZKDLYOTGKSRZXYPYLBZZOFPVRBKPOGQSYFUHZGDDSRPNNLRXIUGPKJNVQPNYIYIVKGQTMUTTBIUTQNTPOUPXNGGHFFXZUEAUWDADOCQTZVKIPHKXOMDJIGEPTVSBWVFRRGDZTSSUFDBJRIWEHXHHFHTZRZBWUQEYFYQVPKPPCRIGVGQCHJBBMFAJHTTLQINPIIWENYKTSZZCPHFQDDJLBTNBOVQYQHLXBLREHHPMNVRFNDTKYSEYNGPOZEHLRJQPWIFKBUZEPZELOAHPBFBVLQDRBLSPZJMQYXCLIYXWLDWEMFDZVKETGEOCCJEVGALUQOIWWYYOVJMRUSGTXFIGJTZNXPOOJWQGJVZPHVSCIIWKRXVJJQKIWKEHENANOYBGOJCYUVPSDJLWXNZFXDXZMUWWGHGVYSQCXHGGOCOMSUOOCEPFIDQJAPXBCOPIVAGHVPPVOAPQWKUHIYLLBAQOCPFMFTPZKNXXGWGPZRPGVZBLJUHQLPDKAVXBHSNGVTPCOLCGIDRBGOEEISFWPSOJGTVWGQBXWPZBJRYIKDOOLSXHBEPJXIUKIEGZVDXZMYJOZGBBUPJEBEDKANZBYJXRBYZBKVNYZANPYKBUCUYUXJYPUGPZVFEZRDWBXXHHTLOEFSSQOVBRHTDYRICFLBZOJUHQVLREFBECOWLRLFPCMFCJRMQBQMEBBTQXHGSLDLFMQGHCSDMGCMDHGQGLRBIPQFUTKJMERKYMIOZZJCXJOJGELWADSGWTJJPXWLPERHIEJGEGWQOFYSGCCUYYVDHUWDVRDPPMDDPDQOHQVSSZLDHCGJJZFTHPQUAOSDCUPYHQVEFIFJGYHYCWZBIHNIRLJOVPOVIHZVNVINOWPGBXJQLEXYGYRTHPFCCELIIMGOEVNJZRSZFERWMZJDMMXDVMTNIRLGDEUJPPSEPKBNWIJOEERDPLYTIAEDAPRENMDIZZDLPRIYZXQAMOPPDMICGDPBVXNPCKJHDFAAXXJQAYWDFBMULXNOEXLOUCKAPLZNZPWNZQLFSWUJVNTAITLGZCKAYRFGIMGQJMBIQZXFUJKJNTLNCIXJMTBWTTYHFHPATGZEPLBGOGTGYCJJPBHDRWBDBDEDQZVQQJRUYVVJCMUJCEIGIPRBBMETPMWEJTFUVJABCIXPGTLIZLRLBBIKRVPJGAHSIXIOROOGBUIYJJHQPDDNYWJMOKTPKTSXXPFPPEHJIHKNBBULMPNDXGROPWRFZNYYCTXEZDZODBVADIUQHODSBLQGORISZLMJZTZAITNRPPKTIKBLZROJCMWJLDQQWHIQMUVHDFIERFGEOTHOHPZCFQYJMWIFAYFFPOQTMBEGRPUWTNESNTBRMWLATZLRSAFTOKGYVKZWBUWFPWJBSXMACOLKRERGCTROZBBHCCHIZDDCVKHGWGTFINLDEEJCIOFZXQITCJHJNYNLOANLLMMOEIBVPJJTCXXKDBIDZWSMDTNGWHHXIGMOTWFXPHSUFWRWLMDQAVMQYRFVGTZOULLOTCKSYUEUIVVRACYOYIYSNRRPATSUNJFDAVEROLXRGUIIAHP'

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
def simple_decode(text, key2, key1): # key1 - Alfgavit ; key2  - Zamenen znachenia

    key_dict = dict(zip(key1, key2))
    out_string = ''.join([key_dict[text[i]] for i in range(len(text))])

    return out_string
def afin_decode(alpha, beta, text):
    obr_a = evklid_first(26, alpha)

    de_cypher = ''
    for i in text:
        if i not in p_marks:
            de_cypher += alphabet[(obr_a*(alphabet.index(i)-beta))%alph_len]
        if i in p_marks:
            de_cypher += i
    return de_cypher
def rec_afin_dencode(alpha1, beta1, alpha2, beta2, text):
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

analyz_text = text.upper()
analyz_text = re.sub(r'[^A-Z]','',analyz_text) # удаляю лишние символы
print(analyz_text)

def crypto_first_analyz(analyz_text):
    first_key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']

    cipher_text_new = analyz_text
    the_best_key = first_key
    var = 0
    the_best_rat = -10000000000000
    while var < 1:
        var = var + 1
        print(first_key)
        random.shuffle(first_key)
        print(first_key)

        bigramms_count = []
        for i in range(len(cipher_text_new) - 1):
            bigramms_count.append(cipher_text_new[i:i + 2])

        Count_rating_bigramm = 0
        for i in range(len(bigramms_count)):
            if bigramms_count[i] in bigramms_freq:
                Count_rating_bigramm += log10(float(bigramms_freq[bigramms_count[i]]) / 4916301)
            else:
                Count_rating_bigramm += log10(0.01 / 4916301)

        print('NEW KEY LETS GO')
        var_2 = 0
        while var_2 < 1000:
            i_1 = random.randint(0, 25)
            i_2 = random.randint(0, 25)
            key_for_cipher = [j for j in first_key]
            key_for_cipher[i_1], key_for_cipher[i_2] = key_for_cipher[i_2], key_for_cipher[i_1]
            # print(key_for_cipher)
            cipher_text_new = simple_decode(analyz_text, key_for_cipher, alphabet)

            bigramms_count = []
            for i in range(len(cipher_text_new) - 1):
                bigramms_count.append(cipher_text_new[i:i + 2])

            new_rating_bigramm = 0
            for i in range(len(bigramms_count)):
                if bigramms_count[i] in bigramms_freq:
                    new_rating_bigramm += log10(float(bigramms_freq[bigramms_count[i]]) / 4916301)
                else:
                    new_rating_bigramm += log10(0.01 / 4916301)

            print('New rat - ', new_rating_bigramm)
            # print('Count rat - ', Count_rating_bigramm)

            if new_rating_bigramm > Count_rating_bigramm:
                Count_rating_bigramm = new_rating_bigramm
                var_2 = 0
                first_key = key_for_cipher
            var_2 += 1
        if Count_rating_bigramm > the_best_rat:
            the_best_rat = Count_rating_bigramm
            the_best_key = first_key
            print(the_best_rat)
    final_text = simple_decode(analyz_text, the_best_key, alphabet)

    return final_text, the_best_rat, the_best_key
def crypto_second_analyz(analyz_text):
    the_best_rat = -10000000000000
    for alfa in alfa_massive:
        for beta in range(0, 25):
            cipher_text = afin_decode(alfa, beta, analyz_text)
            bigramms_count = []
            for i in range(len(cipher_text) - 1):
                bigramms_count.append(cipher_text[i:i + 2])

            Count_rating_bigramm = 0
            for i in range(len(bigramms_count)):
                if bigramms_count[i] in bigramms_freq:
                    Count_rating_bigramm += log10(float(bigramms_freq[bigramms_count[i]]) / 4916301)
                else:
                    Count_rating_bigramm += log10(0.01 / 4916301)
            if Count_rating_bigramm > the_best_rat:
                the_best_rat = Count_rating_bigramm
                the_best_alfa = alfa
                the_best_beta = beta
                print(the_best_rat)
    final_text = afin_decode(the_best_alfa, the_best_beta, analyz_text)
    print(the_best_alfa, the_best_beta)
    return final_text
def crypto_third_analyz(analyz_text):
    the_best_rat = -10000000000000
    for alfa_first in alfa_massive:
        for beta_first in range(0, 25):
            for alfa_second in alfa_massive:
                for beta_second in range(0, 25):
                    cipher_text = rec_afin_dencode(alfa_first, beta_first, alfa_second, beta_second, analyz_text)
                    bigramms_count = []
                    for i in range(len(cipher_text) - 1):
                        bigramms_count.append(cipher_text[i:i + 2])

                    Count_rating_bigramm = 0
                    for i in range(len(bigramms_count)):
                        if bigramms_count[i] in bigramms_freq:
                            Count_rating_bigramm += log10(float(bigramms_freq[bigramms_count[i]]) / 4916301)
                        else:
                            Count_rating_bigramm += log10(0.01 / 4916301)
                    if Count_rating_bigramm > the_best_rat:
                        the_best_rat = Count_rating_bigramm
                        the_best_alfa_first = alfa_first
                        the_best_alfa_second = alfa_second
                        the_best_beta_first = beta_first
                        the_best_beta_second = beta_second
                        print(the_best_rat)
                        print(the_best_alfa_first, the_best_beta_first, the_best_alfa_second, the_best_beta_second)
    final_text = rec_afin_dencode(the_best_alfa_first, the_best_beta_first, the_best_alfa_second, the_best_beta_second, analyz_text)
    return final_text

# print(crypto_first_analyz(text))
# print(crypto_second_analyz(text))
# print(crypto_third_analyz(text))