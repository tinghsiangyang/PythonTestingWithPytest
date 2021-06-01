 def pytest_addopt(parser):
     parser.addoption('--myopt', action='store_true', help='some bollean option')
     parser.addoption('--foo', action='store', default='bar', help='foo: bar or baz')