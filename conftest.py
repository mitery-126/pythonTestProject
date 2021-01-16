import pytest
import yaml

from pythoncode.calculator import calculator

import os
yaml_file_path = os.path.dirname(__file__) + "/data.yml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas["add"]
    minus_datas = datas["minus"]
    times_datas = datas["times"]
    into_datas = datas["into"]
    my_ids = datas["myids"]

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = calculator()
    return calc

@pytest.fixture(scope="class", params=add_datas, ids=my_ids)
def get_add(request):
    print("开始计算")
    yield request.param
    print("计算结束")

@pytest.fixture(params=minus_datas, ids=my_ids)
def get_minus(request):
    print("\n开始计算")
    yield request.param
    print("\n计算结束")

@pytest.fixture(scope="class",params=times_datas, ids=my_ids)
def get_times(request):
    print("\n开始计算")
    yield request.param
    print("\n计算结束")

@pytest.fixture(scope="class", params=into_datas, ids=my_ids)
def get_into(request):
    print("开始计算")
    yield request.param
    print("计算结束")