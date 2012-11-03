import string
def createMapper():
    mapper={}   
    for ch in string.digits:
        mapper[ch]=ord(ch)-ord('0')
        mapper[ord(ch)-ord('0')]=ch
    for ch in string.ascii_uppercase:
        mapper[ch]=ord(ch)-ord('A')+10
        mapper[ord(ch)-ord('A')+10]=ch
    for ch in string.ascii_lowercase:
        mapper[ch]=ord(ch)-ord('a')+36
        mapper[ord(ch)-ord('a')+36]=ch
    return mapper

def baseConvertion(num,curBase,newBase):
    newNum=0
    power=len(num)-1
    mapper = createMapper()
    for ch in num:
        #print newNum,mapper[ch],power
        newNum += mapper[ch]*(curBase**power)
        power -=1
    result = ''
    while newNum>0:
        result=mapper[newNum%newBase]+result
        newNum=newNum/newBase
    return result
