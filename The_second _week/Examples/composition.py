# assertions -> you and your car (both of you aren't a one object of same class)
# aggregation -> you and your universiti or battery of your clock that is use in other devices
# composions (death) -> Questions and paper of exam or puzzle pieces


class Questions:
    def __init__(self, questions:str, answers:list):
        self.questions = questions
        self.answers = answers


class Exam:
    """In this class we are implementing composion (has - a)"""
    def __init__(self):
        self.q = Questions("What is your name ?", ["mahdi","ali", "mohammad"]) # Create object by class 
    def __str__(self) -> str:
        return f"{self.q.questions}\n{self.q.answers}"

test = Exam()
print(test)

print("-----------------------------aggregations-------------------")
# -----------------------------aggregations-----------------------------------

class Students:
    """This class use for aggregations."""
    def __init__(self, name: str, cart_id: str):
        self.name = name
        self.cart_id = cart_id
    
    def __str__(self):
        return f"{self.name}:{self.cart_id} "
    
class University:
    """This class use for aggregations."""
    def __init__(self, students:list):
        self.students = students
    
st = [Students("mahdi","9921"),Students("zohre","9829")]
uni= University(st) # create objects out of class and without dependencies together and sends as a args
for i in uni.students:
    print(i)

