class Result: 

    def __init__(self, stu_id: int, name: str, subject: str, score: int) -> None:
        self.id = int(stu_id)
        self.name = name
        self.subject = subject.capitalize()
        self.score = int(score)

    def generate(self) -> None:
        print('\n\n=============================================')
        print(f'      CHIMP MODERN HIGH | STUDENT RESULT')
        print('=============================================')
        print(f"Stu. ID: {self.id} \nName: {self.name} \nSubject: {self.subject} \n--------------------------------------------- \nScore: {self.score}")
        print('=============================================\n\n')