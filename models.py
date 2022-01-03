'''
@author: Shivam Mishra
@date: 03-01-22 1:07 AM
'''

from datetime import date
from pydantic import BaseModel


class EmployeePayroll(BaseModel):
    """
    Contains different parameters of employee like id, name, gender etc
    """
    id: int
    name: str
    profile_image: str
    gender: str
    department: str
    salary: float
    start_date: date
    notes: str