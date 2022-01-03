'''
@author: Shivam Mishra
@date: 02-01-22 11:37 PM
'''

from fastapi import FastAPI
from operations import DBOperations
from models import EmployeePayroll

app = FastAPI()
operation = DBOperations()


@app.get("/employee_details")
def retrieve_employee_details():
    """
        desc: get method to retrieve employee details
        return: dictionary with employee details
    """
    try:
        employee_details = operation.get_employee_details()
        return {"message": "Employee Details fetched successfully", "data": employee_details}
    except Exception as e:
        return {"message": f"Error : {e}"}


@app.post("/add_employee")
def add_employee_details(emp: EmployeePayroll):
    """
        desc: post method to add employee details
        param: name, profile_image, gender, department, salary, start_date, notes
        return: dictionary with employee details added
    """
    try:
        employee_details = operation.add_employee(emp.name, emp.profile_image, emp.gender, emp.department, emp.salary,
                                                     emp.start_date, emp.notes)
        return {"message": "Successfully Added Employee Details", "data": employee_details}
    except Exception as e:
        return {"message": f"Error : {e}"}


@app.delete("/delete_employee{id}")
def delete_employee_details(id:int):
    """
        desc: delete method to delete employee details
        param: id
        return: string message
    """

    try:
        message = operation.delete_employee_details(id)
        return message
    except Exception as e:
        return {"message": f"Error : {e}"}


@app.put("/update_employee_salary")
def update_employee_details(emp:EmployeePayroll):
    """
        desc: put method to update employee details
        param: id, salary
        return: string message
    """
    try:
        message = operation.update_employee_details(emp.id, emp.salary)
        return message
    except Exception as e:
        return {"message": f"Error : {e}"}


