from . import cheese
# 在当前目录添加__init__.py文件之后，使用相对路径导入，不会报错


def test_def_prefs_full():
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert actual == expected