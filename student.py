class Student:
  def init(self, si, n, cn, bn):
    self.si = si
    self.n = n
    self.cn = cn
    self.bn = bn
    self.m = {}

  def update_student(self, n=None, cn=None, bn=None):
    if n:
      self.n = n
    if cn:
      self.cn = cn
    if bn:
      self.bn = bn

  def remove_student(self):
    # remove student from database
    pass

  def generate_report_card(self):
    total_marks = 0
    total_subjects = 0
    for subject, m in self.m.items():
      total_marks += m
      total_subjects += 1

    p = total_marks / total_subjects
    if p >= 90:
      grade = 'A'
    elif p >= 80:
      grade = 'B'
    elif p >= 70:
      grade = 'C'
    elif p >= 60:
      grade = 'D'
    elif p >= 50:
      grade = 'E'
    else:
      grade = 'F'

    result = 'PASS' if grade != 'F' else 'FAIL'

    report_card = f'Percentage: {p}\nGrade: {grade}\nResult: {result}'

    # write report_card to text file
    with open(f'{self.n}_report_card.txt', 'w') as f:
      f.write(report_card)
student1 = Student(1, 'John', 2, '2022')
student1.update_student(n='John Smith', cn=3)
student1.remove_student()
student1.m['Maths'] = 85
student1.m['Science'] = 90
student1.m['English'] = 95

student1.generate_report_card()