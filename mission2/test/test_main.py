from unittest.mock import patch, Mock, mock_open
import pytest
from mission2 import main
from mission2.player import Player


@pytest.mark.parametrize('return_value, result', [
    (FileNotFoundError("파일을 찾을 수 없습니다."), "파일을 찾을 수 없습니다.\n"),
    (Exception("Attendance data error"), "Attendance data error\n"),
    ([[Mock(), Mock()]], "")])
def test_update_attendance(return_value, result, capsys):
    with patch('mission2.main.read_from_file') as mock_read_from_file,\
            patch('mission2.main.Player.update_bonus_point'), \
            patch('mission2.main.Player.update_bonus_point'),\
            patch('mission2.main.show_removed_player'):
        mock_read_from_file.side_effect = return_value
        main.update_attendance()
        captured = capsys.readouterr()
        assert captured.out == result

@pytest.mark.parametrize('player_data, player_list, name, result', [
    [{'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5},
     [Mock(spec=Player), Mock(spec=Player), Mock(spec=Player), Mock(spec=Player), Mock(spec=Player)], 'name6', 6],
    [{'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5},
     [Mock(spec=Player), Mock(spec=Player), Mock(spec=Player), Mock(spec=Player), Mock(spec=Player)], 'name5', 5]])
@patch("mission2.main.Player")
def test_get_player(player,player_data, player_list, name, result):
    player.return_value = Mock(spec=Player)
    ret_instance = main.get_player(player_data, player_list, name)
    assert isinstance(ret_instance, Player)
    assert len(player_list) == result

@pytest.mark.parametrize('player_data, player_list, name, result', [
    [{'name1': 1, 'name2': 2, 'name3': 3, 'name4': 4, 'name5': 5,
      'name6': 6, 'name7': 7, 'name8': 8, 'name9': 9, 'name10': 10,
      'name11': 11, 'name12': 12, 'name13': 13, 'name14': 14,
      'name15': 15, 'name16': 16, 'name17': 17, 'name18': 18,
      'name19': 19},
     [Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),
      Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock(),Mock()], 'name20', 19]])
@patch("mission2.main.Player")
def test_get_player_exceed_19(player,player_data, player_list, name, result):
    with pytest.raises(Exception):
        main.get_player(player_data, player_list, name)
    assert len(player_list) == result


@pytest.mark.parametrize('file_data, result', [("Umar monday\nDaisy tuesday\nAlice tuesday\nXena saturday\nIan tuesday",5),
                                               ("Umar monday\nDaisy tuesday",2)])
def test_read_from_file(file_data,result):
    with patch("builtins.open", mock_open(read_data=file_data)) as mock_file,\
            patch('mission2.main.get_player') as mock_get_player,\
            patch('mission2.main.Player.update_attendance_point') as mock_update_attendance_point:
        mock_file.read_data = "Umar monday\nWill monday"
        mock_get_player.return_value = Mock(spec=Player)
        main.read_from_file()
        assert mock_get_player.call_count == result
        #assert mock_update_attendance_point.call_count == 2

@pytest.mark.parametrize('file_data, result', [("Umarmonday",1)])
def test_read_from_file_error_case(file_data,result):
    with pytest.raises(Exception),\
            patch("builtins.open", mock_open(read_data=file_data)) as mock_file,\
            patch('mission2.main.get_player') as mock_get_player,\
            patch('mission2.main.Player.update_attendance_point') as mock_update_attendance_point:
        mock_file.read_data = "Umar monday\nWill monday"
        mock_get_player.return_value = Mock(spec=Player)
        main.read_from_file()

@pytest.mark.parametrize('file_data, result', [("Umarmonday",1)])
def test_show_removed_player(capsys, file_data,result):
    player_list = [Mock(spec=Player, player_name='name1', player_id=1, grade='NORMAL', wednesday_count=0, weekend_count=0),
                   Mock(spec=Player, player_name='name2', player_id=2, grade='NORMAL', wednesday_count=0, weekend_count=1),
                   Mock(spec=Player, player_name='name3', player_id=3, grade='NORMAL', wednesday_count=1, weekend_count=0),
                   Mock(spec=Player, player_name='name4', player_id=4, grade='SILVER', wednesday_count=0, weekend_count=0),
                   Mock(spec=Player, player_name='name5', player_id=5, grade='GOLD', wednesday_count=5, weekend_count=1),]
    main.show_removed_player(player_list)
    captured = capsys.readouterr()
    assert captured.out == "\nRemoved player\n==============\nname1\n"
