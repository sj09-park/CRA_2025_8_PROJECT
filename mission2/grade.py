from abc import ABC, abstractmethod

class Grade(ABC):
    def __init__(self):
        self._grade = None

    @abstractmethod
    def get_grade(self) -> str: ...

class Gold(Grade):
  def get_grade(self):
      self._grade = 'GOLD'
      return self._grade

class Silver(Grade):
  def get_grade(self):
      self._grade = 'SILVER'
      return self._grade

class Normal(Grade):
  def get_grade(self):
      self._grade = 'NORMAL'
      return self._grade


class GradeFactory():
    def get_grade(self, point: int) -> str:
        if point >= 50:
            object = Gold()
        elif point >= 30:
            object = Silver()
        else:
            object = Normal()
        return object.get_grade()
