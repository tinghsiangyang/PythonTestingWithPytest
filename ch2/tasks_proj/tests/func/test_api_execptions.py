from typing import Type
import pytest
import tasks


def test_add_raise():
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')
    

def test_start_tasks_db_raises():
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    execption_msg = excinfo.value.args[0]
    assert execption_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate():
    '''Test execpted execptions with tasks.update()'''

    def test_bad_id(self):
        ''' A non-int id should raise an exception. '''
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1}, task=tasks.Task())


    def test_bad_task(self):
        '''A non-Task task should raise an exception.'''
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')

