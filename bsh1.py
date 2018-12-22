import re



zen = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''


text = 'Привидение прошуршало и и исчезло в углу'
ex1 = re.findall(' и.*.',text,re.MULTILINE)
print(ex1)

ex2 = re.findall(' .*?ало ',text)
print(ex2)
ex3 = re.findall(' .*?зло ',text)
print(ex3)





'''
string = 'Mosckva:, 777,999,79. Tula: 071,950,112...'
matches = re.findall('\d', string, re.MULTILINE)
print(matches)




golandec = re.findall('Dutch', zen, re.MULTILINE)
print(golandec)

matches = re.findall('^If', zen , re.MULTILINE)
print(matches)


string = 'Два даа'
m = re.findall('д[ав]а', string,re.IGNORECASE)
print(m)



line = '12345hi21423hello777porn999'
kek = re.findall('\d',line,re.IGNORECASE)
print(kek)
'''
