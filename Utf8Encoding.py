amount=u"₹50"
print("amount {} and its value {}".format(amount,type(amount)))

amountEncoded = amount.encode("utf-8")
print("encoded value of amoun{} and its type {}".format(amountEncoded,type(amountEncoded)))



amountDecoded = amountEncoded.decode("utf-8")
print("decoded value of amoun{} and its type {}".format(amountDecoded,type(amountDecoded)))

import re
res = re.search('student','Ravi is an exceptional student')
if res != None:
    print("result is {} and start positition is {} , ending posotion {}".format(True,res.start(),res.end()))
else:
    print("result is {} ".format(False)) 

print(re.search("trees?","The tree stands tall."))
print(re.search("ab?","ac"))
print(re.search("ab?","abc."))
print(re.search("ab?","abbc"))

print(re.search("ab*","ac"))
print(re.search("ab*","abc."))
print(re.search("ab*","abbc"))
print(re.search("1010*","10"))
print(re.search("1010*","1010000"))

print(re.search("ab+","ac"))
print(re.search("ab+","abc."))
print(re.search("ab+","abbc"))
print(re.search("1010+","10"))
print(re.search("1010+","1010000"))

print(re.search("ab{3,5}c","aabbbbbc"))
print(re.search("ab{7,10}","aabbbbbc"))
print(re.search("ab{7}","aabbbbbc"))
print(re.search("ab{4}","aabbbbbc"))
print(re.search("hur{2,5}ay","hurray"))
print(re.search("awesomeee+","AWESOMEEE".lower()))


