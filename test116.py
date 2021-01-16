
import pytest

class TestCalAdd:

    @pytest.mark.run(order=0)
    def test_add(self, get_calc, get_add):
        result = get_calc.add(get_add[0], get_add[1])
        assert result == get_add[2]

class TestCalInto:

    @pytest.mark.run(order=3)
    def test_into(self, get_calc, get_into):
        result = get_calc.into(get_into[0], get_into[1])
        assert result == get_into[2]

class TestCalMinus:

    @pytest.mark.run(order=1)
    def test_minus(self, get_calc, get_minus):
        result = get_calc.minus(get_minus[0], get_minus[1])
        print(get_minus[1])
        assert result == get_minus[2]

    @pytest.mark.run(order=2)
    def test_times(self, get_calc, get_times):
        result = get_calc.times(get_times[0], get_times[1])
        assert result == get_times[2]
