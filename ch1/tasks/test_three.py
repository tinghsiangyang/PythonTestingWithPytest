from collections import namedtuple
import pytest


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None) # 创建默认的Task对象，不必指定所有属性

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

@pytest.mark.run_these_case # 使用mark打标记，打上相同标记的case为【测试集合】，使用pytest -m run_these_case执行该测试集合的case
def test_member_access():
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)