# &#1057;&#1086;&#1076;&#1077;&#1088;&#1078;&#1072;&#1085;&#1080;&#1077;

1.  [Блобы](#orgbdd0d47)
2.  [Простая реализация регулярок](#org94f9171)
3.  [grep](#orgbefd11c)
4.  [Конечные Автоматы](#orgffa0927)
5.  [Язык RE](#org1e8b9b7)
6.  [Реализация RegExp на конечных автоматах](#orgfc5edef)
7.  [Библиотеки для RegExp](#org64e2706)
8.  [Отладка RegExp](#org3cea2cb)
9.  [Практика](#org3cd4525)



<a id="orgbdd0d47"></a>

# Блобы


<a id="org94f9171"></a>

# Простая реализация регулярок



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


<a id="orgbefd11c"></a>

# grep

    ./naive_grep.py '^def .*(.*):$' ../praktikum_project_5/*/*.py \
        | head -n 5

    ../praktikum_project_5/posts/models.py::21: def __str__(self):
    ../praktikum_project_5/posts/models.py::54: def __str__(self):
    ../praktikum_project_5/posts/views.py::11: def index(request):
    ../praktikum_project_5/posts/views.py::33: def group_posts(request, slug):
    ../praktikum_project_5/posts/views.py::56: def new_post(request):


<a id="orgffa0927"></a>

# Конечные Автоматы


<a id="org1e8b9b7"></a>

# Язык RE


<a id="orgfc5edef"></a>

# Реализация RegExp на конечных автоматах


<a id="org64e2706"></a>

# Библиотеки для RegExp


<a id="org3cea2cb"></a>

# Отладка RegExp


<a id="org3cd4525"></a>

# Практика
