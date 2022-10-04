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
print(re.search("hur{2,}ay","hurray"))
print(re.search("awesomeee+","AWESOMEEE".lower()))

print(re.search("(01){1,2}","010101010"))
print(re.search("(0|1){1,2}","110"))
print(re.search("\*+","11*2"))
print(re.search("awesomeee+","AWESOMEEE".lower(), flags=re.I | re.M))

pattern = re.compile("a+")
print(pattern.search("abc"))

pattern = re.compile("a$")
print(pattern.search("abca"))

pattern = re.compile("^a",flags=re.I|re.M)
print(pattern.search("Abca"))

#pattern = re.compile("^1+0{3,}1*0{1,7}1{2,3}",flags=re.I|re.M) [multiple repeat error]
pattern = re.compile("^1+(000)+1*0{1,7}1{2,3}",flags=re.I|re.M)
print(pattern.search("11000011000111"))

pattern = re.compile(".",flags=re.I|re.M)
print(pattern.search("a"))

pattern = re.compile(".",flags=re.I|re.M)
print(pattern.search("#"))


pattern = re.compile(".{4}0{3}1{2}.{2}",flags=re.I|re.M)
print(pattern.search("abcd00011ft"))


pattern = re.compile("^.{3,15}$",flags=re.I|re.M)
print(pattern.search("Balasubrahmanyam"))


print(re.search("[abc]","abbc")) # uses ASCII internalluy 
print(re.search("[a-c]","abbc"))
print(re.search("[^abc]","dda"))
print(re.search("[a-z]ed","ted"))
print(re.search("[A-z ]","cHandan Kumar Singh"))

#Note that a quantifier loses its special meaning when it’s present inside the character set. Inside square brackets, it is treated as any other character. 

print(re.search("\s+","Upgrad")) #\s [ \t\n\r\f\v]
print(re.search("\S+","Upgrad")) #\S [^ \t\n\r\f\v]
print(re.search("Upgrad","\d+")) #\d [0-9]
print(re.search("Upgrad","\D+")) #\D [^0-9]
print(re.search("Upgrad","\w+")) #w [ a-zA-z0-9_]
print(re.search("Upgrad","\W+")) #W [^ a-zA-z0-9_]
print(re.search("Upgrad","[\w+\s+]")) #W [^ a-zA-z0-9_]
print(re.search("^[A-z]{1,10}\d{4}$","ssam2340")) #meta-sequences that matches usernames of the users of a database. The username starts with alphabets of length one to ten characters long and then followed by a number of length 4.

print(re.search("<.*>","<HTML><TITLE>My Page</TITLE></HTML>"))
print(re.search("<.*?>","<HTML><TITLE>My Page</TITLE></HTML>"))

print(re.match("b+","abbc"))
print(re.search("b+","abbc"))

print(re.sub("Road","Rd","Ramakrishnan Road"))
print(re.sub("R\w+","Rd","Ramakrishnan Road"))


text = "Diwali is a festival of lights,Holi is a festival of colors!"
pattern = 'festival'
for match in re.finditer(pattern,text):
    print("START -",match.start(),end=" ")
    print("END",match.end())

url = "/2017/10/28/oko/2017/05/12"
date_reg = "/(\d{4})/(\d{2})/(\d{2})"
print(re.findall(date_reg,url))

m1=re.search(date_reg,url)
print(m1.group())
print(m1.group(1))
print(m1.group(2))
print(m1.group(3))
print(m1.group(0))



string = "Today's date is 18-05-2018"

# regex pattern
pattern = "(\d{2})\-(\d{2})\-(\d{4})"

# store result
result = re.search(pattern, string)

# extract month using group command
if result != None:
    month = result.group(2)
else:
    month = "NA"

print(month)

res=re.search("\w+@([A-z]+\.com)","user_name_123@gmail.com")
print(res.group(1))
 
# items contains all the files and folders of current directory
items = ['photos', 'documents', 'videos', 'image001.jpg','image002.jpg','image005.jpg', 'wallpaper.jpg',
         'flower.jpg', 'earth.jpg', 'monkey.jpg', 'image002.png']

# create an empty list to store resultant files
images = []

# regex pattern to extract files that end with '.jpg'
pattern = "^(image)\w*\.jpg"

for item in items:
    if re.search(pattern, item):
        images.append(item)

# print result
print(images)


print(re.match("b+","abbc"))