import pytest
import yaml
from pythoncode.calculator import calculator


class TestDemo:
    def setup_class(self):
        self.cal = calculator()
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)

    def setup_method(self):
      print("setup_method:开始计算")

    def teardown_method(self):
      print("teardown_method:计算结束")

    @pytest.mark.parametrize("a, b, expect", datas["add"])
    def test_add(self, a, b, expect):
        result = self.cal.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", datas["minus"])
    def test_minus(self, a, b, expect):
        result = self.cal.minus(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", datas["times"])
    def test_times(self, a, b, expect):
        result = self.cal.times(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect", datas["into"])
    def test_into(self, a, b, expect):
        result = self.cal.into(a, b)
        assert result == expect