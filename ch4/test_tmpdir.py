def test_tmpdir(tmpdir):
    # 在 $tmpdir 创建文件 something.txt
    a_file = tmpdir.join('something.txt')
    print(tmpdir)
# 在 $tmpdir 创建目录 anything
    a_sub_dir = tmpdir.mkdir('anything')

    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')

    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')
    print(a_dir)
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)
    
    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'