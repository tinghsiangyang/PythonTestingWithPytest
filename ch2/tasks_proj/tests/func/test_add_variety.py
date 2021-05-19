from _pytest.capture import TeeCaptureIO
import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


def equivalent(t1, t2):
        return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done))


def test_add_1():    
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', 
                        [Task('sleep', done=True), 
                        Task('wake', 'brian'), 
                        Task('breathe', 'BRIAN', True), 
                        Task('exercise', 'Brian', False)])
def test_add_2(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)