from mission2.player import Player

def update_attendance() -> None:
    try:
        player_list = read_from_file()
        for player in player_list:
            player.update_bonus_point()
            player.update_player_grade()
        show_removed_player(player_list)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except Exception as e:
        print(e)


def get_player(player_data, player_list, name: str) -> Player:
    if name not in player_data:
        id_cnt = len(player_list)
        if id_cnt == 19:
            raise Exception("Player count exceeds 19")
        id_cnt += 1
        player_data[name] = id_cnt
        player_list.append(Player(player_name=name, player_id=id_cnt))
    return player_list[player_data[name]-1]


def read_from_file() -> list:
    player_data = {}
    player_list = list()
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        for _ in range(500):
            line = f.readline()
            if not line:
                break
            attendance_data = line.strip().split()
            if len(attendance_data) != 2:
                raise Exception('Attendance data error')
            name = attendance_data[0]
            weekday = attendance_data[1]
            player = get_player(player_data, player_list, name)
            player.update_attendance_point(weekday)
    return player_list

def show_removed_player(player_list) -> None:
    print("\nRemoved player")
    print("==============")
    for player in player_list:
        if player.grade == 'NORMAL' and player.wednesday_count == 0 and player.weekend_count == 0:
            print(player.player_name)