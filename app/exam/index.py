from data.questions import math_questions, history_questions, accounting_questions

class Examination:

    available_subjects = ('Math', 'History', 'Accounting')
    current_score = 0

    def __init__(self, stu_id: int, name: str, subject: str) -> None:
        self.id = int(stu_id)
        self.name = name
        self.suject = subject.capitalize()

    def take_exam(self) -> bool:
        if self.suject in self.available_subjects:
            if self.suject == 'Math':
                for question in math_questions: 
                    entry = input(f'\n>> {question["que"]}\n\t << ') 

                    if entry.title() == question["ans"].title():
                        self.current_score += question["score"]
                        

            if self.suject == 'History':
                for question in history_questions: 
                    entry = input(f'\n>> {question["que"]}\n\t << ') 
                
                    if entry.title() == question["ans"].title():
                        self.current_score += question["score"]


            if self.suject == 'Accounting':
                for question in accounting_questions: 
                    entry = input(f'\n>> {question["que"]}\n\t << ') 
                
                    if entry.title() == question["ans"].title():
                        self.current_score += question["score"]

            return True

        
        else: 
            return False

