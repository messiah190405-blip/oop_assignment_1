from exam.index import Examination as Exam
from result.index import Result
from data.users import students

class Factory: 

    @classmethod
    def exec(cls) -> None: 
        print(f"\n<< CHIMP MODERN HIGH | STUDENT EXAMINATION >> \n")
        print('info: Current exams are only availabe for the following subjects: \n \t Math \n \t History \n \t Accounting')

        print("\nSign In to take your exam")

        email = input(f'\n>> Enter your email \n \t <<  _ ')
        password = input(f'\n>> Enter your password \n \t <<  _ ')

        subject = input(f'\n  >> Select by retyping from any of the above to start your exam \n \t <<  _ ')
        
        ids = [student["id"] for student in students]
        emails = [student["email"] for student in students]

        if email in emails: 

            user_index = emails.index(email)

            stu_id = students[user_index]["id"]
            first_name = students[user_index]["first_name"]
            last_name = students[user_index]["last_name"]
            inc_pass = students[user_index]["password"]  


            if password == inc_pass: 
                fine_name = first_name.title() + " " + last_name.title()
                
                exam_instance = Exam(stu_id, fine_name, subject)
                print_result = exam_instance.take_exam()

                if print_result == True: 
                    result_instance = Result(stu_id, fine_name, subject, exam_instance.current_score)
                    result_instance.generate()

                else: 
                    print('\n[!] Invalid Entry.') 
                 
            else: 
                print("\n[!] Access Denied")


        else: 
            print("\n [!] Oops! Access Denied")

            
            

        