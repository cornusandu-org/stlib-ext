from tests.base import _TestSuite, static_mark_parametrize
from src import moretyping
import pytest

class DataTests(_TestSuite):
    class Number(_TestSuite):
        class Conversions(_TestSuite):
            @pytest.mark.parametrize("inputData, expected",
                [
                    (2, 2),
                    (4, 4),
                    (5, 5),
                    (-100, -100),
                    (12083, 12083)
                ])
            @staticmethod
            def int_to_int(inputData, expected):
                out = moretyping.data.Number(inputData)
                assert out == expected

            @pytest.mark.parametrize("inputData, expected",
                [
                    (0.0, 0.0),
                    (2.3, 2.3),
                    (-100.2, -100.2),
                    (0.1, 0.1)
                ])
            def float_to_float(self, inputData, expected):
                out = moretyping.data.Number(inputData)
                assert out == expected

            @pytest.mark.parametrize("inputData, expected",
                [
                    ("0", 0.0),
                    ("-1.3", -1.3),
                    ("1", 1),
                    ("2.3", 2.3)
                ])
            def str_to_float(self, inputData, expected):
                out = moretyping.data.Number(inputData)
                assert out == expected

            @pytest.mark.parametrize("invalidInputData", ["s", "avc", "0x2", "1823f"])
            def invalid_str(self, invalidInputData):
                with pytest.raises(ValueError):
                    moretyping.data.Number(invalidInputData)

            def invalid_type(self):
                with pytest.raises(TypeError):
                    moretyping.data.Number(None)

            __targets__ = (int_to_int, float_to_float, str_to_float, invalid_str, invalid_type)

        class InstanceChecks(_TestSuite):
            @static_mark_parametrize("inputInt", [-100, 83, 0, -2, 2])
            def check_int(inputInt):
                assert isinstance(inputInt, moretyping.data.Number)

            @static_mark_parametrize("inputFloat", [-100.0, 83.0, 0.0, -2.1, 2.9])
            def check_float(inputFloat):
                assert isinstance(inputFloat, moretyping.data.Number)

            @static_mark_parametrize("inputString", ["3", "0", "1.0", "-1", "2.9"])
            def check_str(inputString):
                assert not isinstance(inputString, moretyping.data.Number)

            @static_mark_parametrize("invalidData", [None, lambda x: x, type('EmptyClass', (), {})])
            def check_invalid_types(invalidData):
                assert not isinstance(invalidData, moretyping.data.Number)

            __targets__ = (check_int, check_float, check_str, check_invalid_types)
        
        __targets__ = (Conversions, InstanceChecks)
    
    __targets__ = (Number,)
