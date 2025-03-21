from pydantic import BaseModel
from typing import List, Union


CREATE = 4     
READ = 1       
UPDATE = 3     
DELETE = 2   

# Create a dictionary for mapping permission names to permission integers
permission_mapping = {
    "read": READ,
    "delete": DELETE,
    "update": UPDATE,
    "create": CREATE,
}

# Pydantic model to assign permissions to a role
class RolePermissionRequest(BaseModel):
    role_id: int
    permission_ids: List[int]



 
