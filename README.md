# homework

import re

text = '''Жирафы любят таска различные __СУЩ ВО МНОЖ ЧИСЛЕ__ целый день напролет.
Жирафы также славятся тем,  что поедают прекрасные __СУЩ ВО МНОЖ ЧИСЛЕ__,
но после этого у них часто болит
__ЧАСТЬ ТЕЛА__.
Если же жирафы находят __ЧИСЛО__ __СУЩ ВО МНОЖ ЧИСЛЕ__,
у них моментально отваливается __ЧАСТЬ ТЕЛА__.'''

def mad_libs(mls):
    hints = re.findall('__.*?__',mls)
    if hints is not None:
        for word in hints:
            q = 'Vvedite {}'.format(word)
            new = input(q)
            mls = mls.replace(word,new,1)
        print('\n')
        mls = mls.replace('\n', ' ')
        print(mls)
    else:
        print('Misstake of Vvod')

mad_libs(text)

    
