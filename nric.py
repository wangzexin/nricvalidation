import re

def check_alphabet(nric):
    weights=[2,7,6,5,4,3,2]
    if nric[0]=='T' or nric[0]=='S':
        check_map={10:'A', 9:'B', 8:'C', 7:'D', 6:'E', 5:'F', 4:'G', 3:'H', 2:'I', 1:'Z', 0:'J'}
    else:
        check_map={10:'K', 9:'L', 8:'M', 7:'N', 6:'P', 5:'Q', 4:'R', 3:'T', 2:'U', 1:'W', 0:'X'}
    sum_products=0
    for i in range(1,8):
        sum_products=sum_products+(int(nric[i])*weights[i-1])
    if nric[0]=='T' or nric[0]=='G':
        sum_products+=4
    remainder=sum_products % 11
    return check_map[remainder]

def validation(nric):
    pattern=re.compile("^[SGFT][0-9]{7}[A-Z]$")
    return pattern.match(nric)

nric=input('Please input your NRIC : ')
if (nric[1:3]<'68') and (nric[1]>'3'):
    f=False
else:
    f=True
if validation(nric) and check_alphabet(nric)==nric[8] and f:
    print('This NRIC is valid')
else:
    print('This NRIC is not valid')
