# &#1057;&#1086;&#1076;&#1077;&#1088;&#1078;&#1072;&#1085;&#1080;&#1077;

1.  [Что такое регулярные выражения?](#org10b7d18)
2.  [Варианты регулярок](#org81cc879)
3.  [Библиотеки RegEx в Python](#org0513ec0)
4.  [Глобы](#orgb758bca)
5.  [grep](#org2b2e302)
6.  [Наивная реализация регулярок](#org56eab2b)
7.  [Конечные Автоматы](#org2170ddc)
8.  [Поиск подстроки на DFA](#org3d8ea53)
9.  [Реализация RegExp на конечных автоматах](#org043e418)
10. [Примеры использования RE](#orgb0a8af3)
11. [Задача решена](#org56c6a6c)
12. [Задача решена?](#orgca9c281)
13. [Задача решена](#org0bc2e45)
14. [Опережающие и ретроспективные проверки](#orgb1d1994)
15. [Задача решена](#orgcd95cc1)
16. [Задача решена?](#orgab43db4)
17. [Задача решена!](#orgc472b29)
18. [lookahead & lookbehind](#orgf9b2f36)
19. [Жадные квантификаторы](#orgfb09ed5)
20. [Задача решена](#orgc9b36b7)
21. [Задача решена?](#org79e3fb9)
22. [Задача решена](#orgc68add8)
23. [Отладка RegExp](#org5028cf7)
24. [Практика](#org30fa69b)
25. [Практика](#org613aa60)
26. [Практика](#orgb37b64a)
27. [Практика](#orge68dedd)
28. [Литература](#org1c49624)



<a id="org10b7d18"></a>

# Что такое регулярные выражения?

![img](automata_theory.png)


<a id="org81cc879"></a>

# Варианты регулярок

![img](re_variants.png)
<span class="underline"><span class="underline">[PCRE](https://www.pcre.org/current/doc/html/pcre2syntax.html)</span></span>


<a id="org0513ec0"></a>

# Библиотеки RegEx в Python

-   <span class="underline"><span class="underline">[стандартная](https://docs.python.org/3/library/re.html)</span></span>
-   <span class="underline"><span class="underline">[regex](https://github.com/mrabarnett/mrab-regex)</span></span>


<a id="orgb758bca"></a>

# Глобы

    man 7 glob

    import glob

    print(glob.glob("*.py"))

    ['automaton_kmp.py', 'naive_re.py', 'naive_grep.py']


<a id="org2b2e302"></a>

# grep

*g/<Regular Expression>/p*

    echo "g/def/p" | ed naive_re.py

    1234
    def match(regexp: str, text: str) -> bool:
    def matchhere(regexp: str, text: str) -> bool:
    def matchstar(c: str, regexp: str, text: str) -> bool:

    ./naive_grep.py '^def .*(.*):$' \
      ../praktikum_project_5/*/*.py \
      | head -n 5


<a id="org56eab2b"></a>

# Наивная реализация регулярок



    print(match("abc", "abc"))
    print(match("abc$", "xyzabc"))
    print(match("^abc", "xyzabc"))
    print(match("^abc", "abcx"))
    print(match("a*b", "bcd"))
    print(match("a*b", "aaaaabcd"))

    True
    True
    False
    True
    True
    True


<a id="org2170ddc"></a>

# Конечные Автоматы

![img](dfa_matrix.png)

![img](dfa_flow.png)


<a id="org3d8ea53"></a>

# Поиск подстроки на DFA



    kmp1 = KMP("abc")
    print(kmp1.search("abcd"))
    print(kmp1.search("fooabcd"))
    print(kmp1.search("foobar"))

    0
    3
    -1


<a id="org043e418"></a>

# Реализация RegExp на конечных автоматах

<span class="underline"><span class="underline">[для особо пытливых](https://github.com/avli/nfa-regex)</span></span>


<a id="orgb0a8af3"></a>

# Примеры использования RE

    Задача: написать регулярку, проверяющую,
    что в строке корректный email адрес


<a id="org56c6a6c"></a>

# Задача решена


    print(re.search(
        r"\w+@\w+\.\w+",
        "example@gmail.com"
    )[0])
    print(re.search(
        r"\w[\w_.]+@\w+\.\w+",
        "example.1.2.3@gmail.com"
    )[0])

    example@gmail.com
    example.1.2.3@gmail.com


<a id="orgca9c281"></a>

# Задача решена?



    print(re.search(
        r"\w+@\w+\.\w+",
        "example@foo.gmail.com"
    )[0])
    print(re.search(
        r"\w[\w_.]+@\w+\.\w+",
        "example.1.2.3@foo.gmail.com"
    )[0])

    example@foo.gmail
    example.1.2.3@foo.gmail


<a id="org0bc2e45"></a>

# Задача решена


    rg = re.compile(
      r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+"
      r"(?:\.[a-zA-Z0-9-]+)+$"
    )

    print(re.match(
        rg, "example@foo.gmail.com"
    )[0])
    print(re.match(
        rg, "example.1.2.3@foo.gmail.com"
    )[0])

    example@foo.gmail.com
    example.1.2.3@foo.gmail.com


<a id="orgb1d1994"></a>

# Опережающие и ретроспективные проверки

    Задача: заменить переводы строк на <br/>,
    за исключением случая, если перед этим шел html-тэг


<a id="orgcd95cc1"></a>

# Задача решена

    import re

    print(re.sub(
        r"([^>])\n",
        r"\1<br\\>",
        "<p>Привет\nдрузья</p>"
    ))

    <p>Привет<br\>друзья</p>


<a id="orgab43db4"></a>

# Задача решена?

    import re

    print(re.sub(
        r"([^>])\n",
        r"\1<br\>",
        "<p>Привет\n\nдрузья</p>"
    ))

    <p>Привет<br\>
    друзья</p>


<a id="orgc472b29"></a>

# Задача решена!

    import re

    print(re.sub(
        r"(?<=[^>])\n",
        r"<br\>",
        "<p>Привет\n\nдрузья</p>"
    ))

    <p>Привет<br\><br\>друзья</p>


<a id="orgf9b2f36"></a>

# lookahead & lookbehind

-   **(?<=&#x2026;):** Должно совпасть слева (Позитивная ретроспективная проверка).
-   **(?<!&#x2026;):** Не должно совпасть слева (Негативная ретроспективная проверка).
-   **(?=&#x2026;):** Должно совпасть справа (Позитивная опережающая проверка).
-   **(?!&#x2026;):** Не должно совпасть справа (Негативная опережающая проверка).


<a id="orgfb09ed5"></a>

# Жадные квантификаторы

    Задача: заменить буржуинские кавычки лапки
    на отечественные кавычки ёлочки.


<a id="orgc9b36b7"></a>

# Задача решена


    print(re.sub(
        r'"(.+)"',
        r"«\1»",
        '"Идиот"'
    ))

    «Идиот»


<a id="org79e3fb9"></a>

# Задача решена?


    print(re.sub(
        r'"(.+)"',
        r"«\1»",
        '"Идиот" "Бесы"'
    ))

    «Идиот" "Бесы»


<a id="orgc68add8"></a>

# Задача решена


    print(re.sub(
        r'"([^"]+)"',
        r"«\1»",
        '"Идиот" "Бесы"'
    ))
    print(re.sub(
        r'"(\w+)"',
        r"«\1»",
        '"Идиот" "Бесы"'
    ))

    «Идиот» «Бесы»
    «Идиот» «Бесы»


<a id="org5028cf7"></a>

# Отладка RegExp

<span class="underline"><span class="underline">[RegeExer](https://regexr.com/)</span></span>
<span class="underline"><span class="underline">[Как это отладить?!](http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html)</span></span>


<a id="org30fa69b"></a>

# Практика

    Задача: преобразовать все ссылки в тексте в
    html-тэги <a href=[url]>url</a>


<a id="org613aa60"></a>

# Практика

    Задача: является ли текст числом
    (в том числе, дробным)?


<a id="orgb37b64a"></a>

# Практика

    Задача: поставить пробелы после запятых,
    если их там нет.


<a id="orge68dedd"></a>

# Практика

    Задача: заменить идущие подряд знаки ,.!? на один


<a id="org1c49624"></a>

# Литература

-   <span class="underline"><span class="underline">[import re](https://docs.python.org/3/library/re.html)</span></span>
-   <span class="underline"><span class="underline">[lookahead & lookbehind](https://docs-python.ru/tutorial/ispolzovanie-reguljarnyh-vyrazhenij-python/operezhajuschaja-retrospektivnaja-proverka-pozitsii-regexp/)</span></span>
-   <span class="underline"><span class="underline">[хорошая статья](https://habr.com/ru/post/349860/?ysclid=l15brkrx4y)</span></span>
-   <span class="underline"><span class="underline">[Практика программирования](https://www.labirint.ru/books/518955/)</span></span>
-   <span class="underline"><span class="underline">[Регулярные выражения](https://www.labirint.ru/books/647977/)</span></span>
-   <span class="underline"><span class="underline">[NFA & RE](https://swtch.com/~rsc/regexp/regexp1.html)</span></span>
-   <span class="underline"><span class="underline">[Алгоритмы](https://www.labirint.ru/books/512969/)</span></span>
