import re

# re modülü
# result = dir(re)

#re.findall()

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# result = re.findall("Python",str)
# result = len(result)

#re.split()

# result = re.split(" ",str)

#re.sub()

# result = re.sub(" ","-",str)
# result = re.sub("\s","*",str)


#re.search()

# result = re.search("Python",str)
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string
# print(result)


#regular expression


'''
    [] - Köşeli parantezler arasına alınan bütün karakterler aranır.

    [abc] => a      : 1 match
            ac      : 2 match
            Python  : No matches

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39]=> [01239]

    [^abc] => abc dışındaki karakterler.
    [^0-9] => rakam olmayan karakterler.

'''

# result = re.findall("[abc]",str)
# result = re.findall("[0-5]",str)
# result = re.findall("[a-e]",str)
# # result = re.findall("[sat]",str) - saat yazmama gerek yok. 1 a yeter
# result = re.findall("[^abc]",str)
# print(result)

"""
    . - Her hangi bir karakteri belirtir.

        .. => a     : No match
              b     : 1 match
              abc   : 1 match
              abcd  : 2 matches

"""

# result = re.findall("...",str)
# result = re.findall("Py..on", str)


"""
    ^ - Belirtilen karakterlerle başlıyor mu?

    ^a => a: 1 match
          abc: 1 match
          bac: No match
"""

result = re.findall("^a",str)
result = re.findall("^P",str)


"""
    $ - Belirtilen karakterle bitiyor mu?

    a$ =>a      : 1 match
         lamba  : 1 match
         Python : No match
"""

result = re.findall("t$",str)


"""

    * - Bir karakterin sıfır ya da daha fazla sayıda 
    olmasını kontrol eder.

    ma*n = > mn     :1 match
             man    :1 match
             maaan  :1 match
             main   :No match (a'nın arkasına n gelmiyor.)
"""
result = re.findall("sa*t", str)


"""

    + - Bir karakterin bir ya da daha fazla sayıda olmasını
    kontrol eder.

        ma+n => mn      : No match
                man     : 1 match
                maaan   : 1 match
                main    : No match (a'nın arkasına n gelmiyor.)
"""

result = re.findall("sa+t", str)

"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
    kontrol eder.

    ma?n => mn      : No match
            man     : 1 match
            maaan   : 1 match
            main    : No match (a'nın arkasına n gelmiyor.)
"""

result = re.findall("sa?t", str)

"""

    {} - Karakter sayısını kontrol eder.

        al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2, en fazla 3
        kez tekrarlamalı.
        [0-9]{2,4} => en az 2, en çok 4 basamaklı sayılar.
"""
result = re.findall("a{2}" , str)
result = re.findall("[0-9]{2}", str)


"""
    | - alternatif seçeneklerden birinin gerçeklemesi gerekir.

        a | b => a ya da b

            cde => no match
            ade=> 1 match
            acdbea => 3 matches

"""


"""

    () - gruplama için kullanılır.

        (a|b|c)xz => a,b,c karakterleinin arasına xz gelmelidir.
"""

"""

    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasındaki a karakterini arar. Yani
        $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı?
        \Athe => the stringin başında mı?

    \Z - Belirtilen karakter string in sonunda mı?
        the\Z => the stringin sonunda mı?

    \b - Belirtilen karakter kelimenin başında ya da sonunda mı?
        \bthe => kelimenin başında mı?
        the\b => kelimenin sonunda mı?

    \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi?
        \Bthe => the kelimenin başında değil mi?
        the\B => the kelimenin sonunda değil mi?

    \d - [0-9] ile aynı anlama gelir. Yani rakamları arar.
        \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir. Yani rakam olmayanları arar.
        \D => 1ab44_50

    \s - Boşluk karakterlerini arar. " "
    \S - Boşluk karakteri dışındakileri arar.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakterini arar.
    \W - \w nin tam tersi
"""
print(result)