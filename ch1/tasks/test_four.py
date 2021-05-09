from collections import namedtuple
import pytest


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# collections.namedtuple(typename, field_names, verbose=False, rename=False)
# typename: 元组名称
# field_names: 元组中元素名称
# rename: 如果元素名称中还有Python的关键字，则必须设置为rename=True
# verbose: 默认就好
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    excepted = {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    }
    assert t_dict == excepted

@pytest.mark.run_these_case
def test_replace():
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    t_excepted = Task('finish book', 'brain', True, 11)
    assert t_after == t_excepted
