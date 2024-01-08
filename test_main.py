from main import otm_function, mtm_function, set_a

#TDD-фреймворк
def test_otm_function():
    expected = [('25x35x90', 250, 'Ротбанд'), ('30x30x80', 350, 'Петрович'), ('25x36x90', 450, 'Ротбанд'),
                ('25x46x96', 350, 'Ротбанд'), ('25x26x96', 250, 'Петрович'), ('35x36x76', 200, 'Пемолюкс')]
    actual = []
    assert otm_function(actual) == expected


def test_mtm_function():
    expected = [('25x35x90', 250, 'Кнауф'), ('30x30x80', 350, 'Петрович'), ('25x36x90', 450, 'Петрович'),
                ('25x46x96', 350, 'Пемолюкс'), ('25x26x96', 350, 'Ротбанд'), ('25x46x96', 450, 'Пемолюкс'),
                ('25x35x90', 250, 'Петрович'), ('30x30x80', 200, 'Все смеси'), ('25x36x90', 350, 'Пемолюкс'),
                ('35x36x76', 200, 'Все смеси'), ('25x26x96', 350, 'Петрович'), ('25x46x96', 250, 'Все смеси')]
    actual = []
    assert mtm_function(actual) == expected


def test_set_a():
    expected = {'25x35x90': ['Кнауф', 'Пемолюкс'], '30x30x80': ['Петрович', 'Ротбанд']}
    m_to_m = []
    res = {}
    actual = set_a(mtm_function(m_to_m), res)
    assert expected == actual
