from unittest.mock import patch, Mock
import pytest
from _pytest.fixtures import fixture

from mission2.player import Player
from mission2.grade import GradeFactory

@fixture
def test_player():
    return Player('name',1)



@pytest.mark.parametrize('weekday,point,wednesday_count, weekend_count',
                         [('monday', 1,0,0),('tuesday',1,0,0),('wednesday',3,1,0),('thursday',1,0,0),
                          ('friday',1,0,0),('saturday',2,0,1),('sunday',2,0,1),])
def test_update_attendance_point(test_player, weekday,point,wednesday_count, weekend_count):
    test_player.update_attendance_point(weekday)
    assert test_player.point == point
    assert test_player.wednesday_count == wednesday_count
    assert test_player.weekend_count == weekend_count


@pytest.mark.parametrize('weekday,point,wednesday_count, weekend_count',
                         [('dayday',0,0,0),])
def test_update_attendance_point_with_wrong_day(test_player, weekday,point,wednesday_count, weekend_count):
    with pytest.raises(Exception):
        test_player.update_attendance_point(weekday)


@pytest.mark.parametrize('wednesday_count, weekend_count, result',
                         [(0,0,0),(10,0,10),(0,10,10),(10,10,20),])
def test_update_bonus_point(test_player, wednesday_count, weekend_count, result):
    test_player.wednesday_count = wednesday_count
    test_player.weekend_count = weekend_count
    test_player.update_bonus_point()
    assert test_player.point == result


@pytest.mark.parametrize('point, grade',
                         [(10,'NORMAL'),(30,'SILVER'),(50,'GOLD'),])
def test_update_player_grade(capsys, test_player, point, grade):
    with patch("mission2.player.GradeFactory") as grade_factory:
        test_player.point = point
        grade_factory.return_value = Mock(spec=GradeFactory)
        grade_factory.get_grade.return_value = grade
        test_player.update_player_grade()
        captured = capsys.readouterr()

        assert captured.out == f"NAME : {test_player.player_name}, POINT : {test_player.point}, GRADE : {test_player.grade}\n"