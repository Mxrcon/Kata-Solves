#Kata Source:
# https://www.codewars.com/kata/5708ef48fe2d018413000776/train/python
#5-Kyu
#String manipulation and basic DNA knowledge

def translate_with_frame(dna, frames=[1,2,3,-1,-2,-3]):
    r_f = splitter(dna)+splitter(reverse_complement(dna))
    result = [translate(i) for i in r_f]
    result_dict= {1:result[0],2:result[1],3:result[2]
    ,-1:result[3],-2:result[4],-3:result[5]}
    return [result_dict[i] for i in frames]

def reverse_complement(dna):
    rc= []
    dictdna = {"A":"T","T":"A","C":"G","G":"C"}
    for i in dna[::-1]:
        rc.append(dictdna[i])
    return "".join(rc)
def splitter(dna):
    spt = []
    for i in [0,1,2]:
        spt.append(dna[i:])
    return spt
def translate(dna):
    translation =[]
    cod = ["".join(dna[i:i+3]) for i in range(0,len(dna),3)]
    for i in cod:
        if len(i) ==3:
            translation.append(codons[i])
    return "".join(translation)
