from mission2.grade import GradeFactory

class Player:
    def __init__(self, player_name, player_id):
        self._player_name = player_name
        self._player_id = player_id
        self._point = 0
        self._grade = None
        self._wednesday_count = 0
        self._weekend_count = 0

    @property
    def player_name(self):
        return self._player_name

    @property
    def point(self):
        return self._point

    @property
    def grade(self):
        return self._grade

    @property
    def wednesday_count(self):
        return self._wednesday_count

    @property
    def weekend_count(self):
        return self._weekend_count

    @point.setter
    def point(self, point):
        self._point = point

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    @wednesday_count.setter
    def wednesday_count(self, wednesday_count):
        self._wednesday_count = wednesday_count

    @weekend_count.setter
    def weekend_count(self, weekend_count):
        self._weekend_count = weekend_count

    def update_attendance_point(self, weekday: str) -> None:
        weekday_point = {'monday': 1,
                         'tuesday': 1,
                         'wednesday': 3,
                         'thursday': 1,
                         'friday': 1,
                         'saturday': 2,
                         'sunday': 2, }
        self.point += weekday_point[weekday]
        if weekday == 'wednesday':
            self.wednesday_count += 1
        if weekday in ('saturday', 'sunday'):
            self.weekend_count += 1

    def update_bonus_point(self) -> None:
        if self.wednesday_count > 9:
            self.point += 10
        if self.weekend_count > 9:
            self.point += 10

    def update_player_grade(self) -> None:
        gf = GradeFactory()
        self.grade = gf.get_grade(self.point)
        print(f"NAME : {self.player_name}, POINT : {self.point}, GRADE : {self.grade}")
