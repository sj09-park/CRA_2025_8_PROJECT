from dataclasses import dataclass

PLAYER_DATA = {}
PLAYER_LIST = list()


@dataclass
class Player:
    name: str
    player_id: int
    point = 0
    grade = 'NORMAL'
    wednesday_count = 0
    weekend_count = 0


def get_player_number(name: str) -> int:
    if name not in PLAYER_DATA:
        id_cnt = len(PLAYER_LIST)
        if id_cnt == 19:
            raise Exception("Player count exceeds 19")
        id_cnt += 1
        PLAYER_DATA[name] = id_cnt
        PLAYER_LIST.append(Player(name=name, player_id=id_cnt))
    return PLAYER_DATA[name]


def update_player_attendance(name: str, weekday:str) -> None:
    player_id = get_player_number(name)

    weekday_point = {'monday':1,
                     'tuesday':1,
                     'wednesday':3,
                     'thursday':1,
                     'friday':1,
                     'saturday':2,
                     'sunday':2,}
    PLAYER_LIST[player_id-1].point += weekday_point[weekday]

    if weekday == "wednesday":
        PLAYER_LIST[player_id-1].wednesday_count += 1
    elif weekday in ['saturday', 'sunday']:
        PLAYER_LIST[player_id-1].weekend_count += 1


def read_from_file() -> None:
    try:
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
                update_player_attendance(name, weekday)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    except Exception as e:
        print(e)


def update_bonus_point() -> None:
    for player in PLAYER_LIST:
        if player.wednesday_count > 9:
            player.point += 10
        if player.weekend_count > 9:
            player.point += 10


def update_player_grade() -> None:
    for player in PLAYER_LIST:
        if player.point >= 50:
            player.grade = 'GOLD'
        elif player.point >= 30:
            player.grade = 'SILVER'
        else:
            player.grade = 'NORMAL'

        print(f"NAME : {player.name}, POINT : {player.point}, GRADE : {player.grade}")

def show_removed_player() -> None:
    print("\nRemoved player")
    print("==============")
    for player in PLAYER_LIST:
        if player.grade == 'NORMAL' and player.wednesday_count == 0 and player.weekend_count == 0:
            print(player.name)


if __name__ == "__main__":
    read_from_file()
    update_bonus_point()
    update_player_grade()
    show_removed_player()