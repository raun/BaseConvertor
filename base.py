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

def baseConvertDec(num,curBase,newBase):
    newNum=0
    power=1
    count=0
    mapper = createMapper()
    for ch in num:
        newNum += mapper[ch]*(curBase**(-power))
        power += 1
    #print "number in base 10",newNum
    result=''
    while newNum%1!=0 and count<50:
        count+=1
        #print newNum,result
        result = result + mapper[int(newNum*newBase)]
        newNum=newNum*newBase-int(newNum*newBase)
    return result

def baseConvert(num,curBase,newBase):
    if '.' in num:
        newNum = num.split('.')
        return baseConvertion(newNum[0],curBase,newBase)+'.'+baseConvertDec(newNum[1],curBase,newBase)
    else:
        return baseConvertion(num,curBase,newBase)

def validateInput():
    num=str(raw_input("Enter the number:"))
    curBase=int(raw_input("Enter the base of the number(integer):"))
    mapper= createMapper()
    for ch in num:
        if mapper[ch] > curBase-1:
            print "You have input a wrong number:"
            return
    newBase=int(raw_input("Enter the base you want to convert into:"))
    print baseConvert(num,curBase,newBase)
