from typing import NamedTuple
from _pytest.cacheprovider import cache
import pytest
import datetime
import time
from random import random
from collections import namedtuple


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        errorstring = 'test duration over 2x last duration'
        assert this_duration <= last_duration * 2, errorstring


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random())





