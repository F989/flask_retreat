from enum import Enum

class RoleModel(Enum):
    Admin = 1
    User = 2


print(RoleModel.Admin.value) # 1 
print(RoleModel.Admin.name) # Admin 