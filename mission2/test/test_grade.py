import pytest
from _pytest.fixtures import fixture

from mission2.grade import GradeFactory

@fixture
def test_grade_factory():
    return GradeFactory()


@pytest.mark.parametrize('point, result',[(0,'NORMAL'),(10,'NORMAL'),
                                          (30,'SILVER'),(50,'GOLD'),
                                          (80,'GOLD'),(100,'GOLD')])
def test_get_grade_from_factory(test_grade_factory, point, result):
    grade = test_grade_factory.get_grade(point)
    assert grade == result