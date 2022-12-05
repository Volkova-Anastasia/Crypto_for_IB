
import galois

alphabet_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z',' ']
gf_alph_len = len(alphabet_1)
p_marks = ['.', ',', '-', '"', "'", '!', '?', '(', ')', '_', '{', '}', '[', ']', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '0']

irreducible_poly = galois.irreducible_poly(3,3)
GF = galois.GF(3**3,irreducible_poly)

def galya_afin_code(alpha, beta,text):
    alpha = GF(alpha)
    beta = GF(beta)
    if (alpha < gf_alph_len and beta < gf_alph_len):
        cypher = ''
        for i in text:
            if i not in p_marks:
                cypher += alphabet_1[(alpha * GF(int(alphabet_1.index(i))) + beta)]
            else:
                cypher+=i
        return cypher
    else:
        print("Выберите другие значенмия alpha и beta")

def galya_afin_decode(alpha, beta,text):
    alpha = GF(alpha)
    beta = GF(beta)
    obr_a = GF(1)/alpha

    de_cypher = ''
    for i in text:
        if i not in p_marks:
            de_cypher += alphabet_1[(obr_a*(GF(alphabet_1.index(i))-beta))]
        if i in p_marks:
            de_cypher += i 
    return de_cypher
def galya_afin_rec_encode(alpha1, beta1, alpha2, beta2,text):
    alpha1 = GF(alpha1)
    alpha2 = GF(alpha2)
    beta1 = GF(beta1)
    beta2 = GF(beta2)
    cypher = ''
    alpha_array = []
    beta_array = []
    if (alpha1 < gf_alph_len and beta1 < gf_alph_len and alpha2 < gf_alph_len and beta2 < gf_alph_len):
        if text[0] not in p_marks:
            cypher += alphabet_1[(alpha1 * GF(alphabet_1.index(text[0])) + beta1)]
        else:
            cypher+=text[0]
        if text[1] not in p_marks:
            cypher += alphabet_1[(alpha2 * GF(alphabet_1.index(text[1])) + beta2)]
        else:
            cypher+=text[1]
        alpha_array.append(alpha1)
        alpha_array.append(alpha2)
        beta_array.append(beta1)
        beta_array.append(beta2)
        for i in range(2,len(text)):
            if text[i] not in p_marks:

                alpha_i = (alpha_array[i-2]) * (alpha_array[i-1]) 
                beta_i = (beta_array[i-2]) + (beta_array[i-1])
                alpha_array.append(alpha_i)
                beta_array.append(beta_i)

                cypher+= alphabet_1[((alpha_i * GF(alphabet_1.index(text[i]))) + beta_i)]
                
            else:
                cypher+=text[i]
                alpha_array.append(alpha_i)
                beta_array.append(beta_i)
        return cypher

    else:
        print("Выберите другие значенмия alpha и beta")

def galya_afin_rec_dencode(alpha1, beta1, alpha2, beta2,text):
    de_cypher = ''

    alpha1 = GF(alpha1)
    alpha2 = GF(alpha2)
    beta1 = GF(beta1)
    beta2 = GF(beta2)

    alpha_array = []
    beta_array = []
    obr_a_array = []

    obr_a1 = GF(1)/alpha1
    obr_a2 = GF(1)/alpha2

    if text[0] not in p_marks:
        de_cypher += alphabet_1[(obr_a1*(GF(alphabet_1.index(text[0]))-beta1))]
    else:
        de_cypher += text[0]
    if text[1] not in p_marks:
        de_cypher += alphabet_1[(obr_a2*(GF(alphabet_1.index(text[1]))-beta2))]
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
            alpha_i = (alpha_array[i - 2] * alpha_array[i - 1]) 
            beta_i = (beta_array[i - 2] + beta_array[i - 1]) 

            obr_a_i = GF(1)/alpha_i

            de_cypher += alphabet_1[(obr_a_i*(GF(alphabet_1.index(text[i]))-beta_i))]

            alpha_array.append(alpha_i)
            beta_array.append(beta_i)
            obr_a_array.append(obr_a_i)
        else:
            de_cypher+=text[i]
            alpha_array.append(alpha_i)
            beta_array.append(beta_i)
            obr_a_array.append(obr_a_i)
    return(de_cypher)

    
# print(galya_afin_code(5, 7, 'VOLKOVA'))
# print(galya_afin_decode(5, 7, 'UEZXEUH'))
# print(galya_afin_rec_encode(5, 7, 3, 9, 'VOLKOVA'))
# print(galya_afin_rec_dencode(5, 7, 3, 9,'UUO YOX'))