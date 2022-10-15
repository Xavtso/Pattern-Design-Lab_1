from ast import Add
from typing import List, Any, Dict
from datetime import datetime, timedelta


class Assignment:
    """declare variables in assigment class"""
    def __init__(self, tasks: Dict, description: str, is_done: bool, status: str, ) -> None:
        self.received_tasks = tasks
        self.description = description
        self.status = status
        self.is_done = is_done
# function to send task to date  
    def get_tasks_to_date(self, date: datetime) -> List[Dict]:
        return [value for key, value in self.received_tasks.items()
                if key <= date]


class Developer:
# declare variables to Developer class
    def __init__(self, id_: int, name: str,
                 address: str, phone_number: str, email: str, position: str, rank: str, salary: float,) -> None:
        self.id_ = id_
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.position = position
        self.rank = rank
        self.salary = salary
        self.assignments: List[Assignment] = []
        self.projects: List[Any] = []

# function to assign project
    def assign(self, project):
        self.projects.append([project])
# function to view assigned projects
    def assigned_projects(self):
        return self.projects
# function to unassign projects
    def unassign(self, project_title: str):
        self.projects = list(filter(lambda x: x.title == project_title,
                                    self.projects))


class Project:
    # declare variables to Project class
    def __init__(self, title: str, tasks: List[Dict], limit: int) -> None:
        self.title = title
        self.tasks = tasks
        self.limit = limit
        self.developers: List[Developer] = []
# function for add developers to list
    def add_developer(self, developer: Developer) -> bool:
        if len(self.developers) < self.limit:
            developer.assign(self)
            self.developers.append(developer)
            print(f'Developer {developer.name} has been added to the project {self.title}🎉')
            return True
        else:
            print("Limit has been exceeded")
            return False
# function for remove developer
    def remove_developer(self, id_:int, assignment) -> bool:
        if assignment.is_done == False:
            for dev in self.developers:
                 if dev.id_ == id_:
                     self.developers = list(filter(lambda x: x.id_ == id_, self.developers))
                     print(f'Developer {developer.name} has been fired💔')
                     return True
                 else:
                     print(f"Developer with id = {id_} does not exist⛔")
                     return False
        else:
            print(f'Ok {developer.name}, i\'ll not dismiss you now.You can continue to work😉')

class QAEngineer:
    # declare variables to QaEngineer class
    def __init__(self, id_: int, name: str, addres: str,
                 phone_number: str, email: str, salary: float,
                 rank: str, position: str,
                 ) -> None:
                self.id_ = id_
                self.name = name
                self.address = addres
                self.phone_number = phone_number
                self.email = email
                self.salary = salary
                self.rank = rank
                self.position = position
# Function to test true project
    def  test_feature(self, project: Project ):
        if project.title == 'Pattern Design':
            print('It\'s your project✅ -- start to do 💻')    
        else:
            print(f'{developer.name} it\'s not your task⛔.Change the project🔁')


class ProjectManager:
    def __init__(self, id_: int, name: str, addres: str, phone_number: str,
                 email:str, salary: float, project:Project):
            self.id_ = id_
            self.name = name
            self.addres = addres
            self.phone_number = phone_number
            self.email = email
            self.salary = salary
            self.project = list([project])
# function to test proggres on project
    def discuss_project (self, assigment: dict) -> None:
        if assigment.is_done == True:
            print('You are good worker😎.Keep going')
        else:
            print(f'{developer.name}, Why project is not done yet. I will dismiss you!🤬')

# declare values
developer = Developer(id_=1,
                      name='Vitaliy',
                      address='99a street',
                      email='vitaliyhavrona@gmail.com',
                      phone_number='0934627774',
                      position='Junior',
                      rank='high',
                      salary=1.200,
                      )

#  declare values
qa = QAEngineer(id_= 2, 
                name = 'Anybody',
                addres = 'anywhere', 
                phone_number = '0665364546', 
                email = 'anybodymail@gmail.com', 
                salary = 2.200, rank = 'Midlle', 
                position = 'QaEngineer'
                )
# declae values
manager = ProjectManager(id_= 3,
                         name = 'Oleg',
                         addres = 'Lviv',
                         phone_number = '+38 (099) 373-3031',
                         email = 'oleh.sinkevych@lnu.edu.ua',
                         salary = 3.2,
                         project = Project)

tasks = {
    datetime.now(): {'title': 'implement tests', 'is_done': False,
                     'description': 'to test'},
    datetime.now() + timedelta(minutes=1): {'title': 'implement tests', 'is_done': False,
                                            'description': 'to test'},

}
# declare values 
assignment = Assignment(description='Testing...', 
                        tasks=tasks, 
                        status='In progress..', 
                        is_done= False)

assignment1 = Assignment(description='Testing...', 
                        tasks=tasks, 
                        status='Done=)', 
                        is_done= True)

developer.assignments = [assignment, assignment]

project = Project(tasks=[tasks], limit=10, title='Pattern Design')
# calling function for adding developer 
project.add_developer(developer=developer)
# call QaEngeneer function
qa.test_feature(project)

manager.discuss_project(assignment1)
# call
project.remove_developer(developer.id_,assignment)

