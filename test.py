from user import User
from session import Session
from requirements import Requirements

user = User('admin', 'admin')
session = Session(user.username,user.password, "http://localhost:8080/squash/api/rest/latest")
requirements_space = Requirements(session)

print(requirements_space.get_all_requirements())

print(requirements_space.create_requirement('requirement','name_req','MINOR','APPROVED','desc','requirement-folder',254))