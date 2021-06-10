import pytest
# import unneceaasry_math
# from dt.dt3 import unnecessary_math
import unnecessary_math
# from ch4.dt.dt3 import unnecessary_math


@pytest.fixture(autouse=True)
def add_um(doctest_namespace):
    doctest_namespace['um'] = unnecessary_math