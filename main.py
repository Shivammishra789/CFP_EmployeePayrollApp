'''
@author: Shivam Mishra
@date: 02-01-22 11:37 PM
'''

import logging
from fastapi import FastAPI
from operations import DBOperations
from models import EmployeePayroll

logging.basicConfig(filename='employee_details.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

app = FastAPI()
operation = DBOperations()


@app.get("/employee_details")
def retrieve_employee_details():
    """
        desc: get method to retrieve employee details
        return: employee details in SMD format
    """
    try:
        employee_details = operation.get_employee_details()
        logging.info("Successfully Get All Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        return {"status": 200, "message": "Employee Details fetched successfully", "data": employee_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.get("/emp")
def single_employee_data(id: int):
    """
        desc: get method to retrieve single employee detail
        return: employee detail in SMD format
    """
    try:
        employee_detail = operation.get_single_emp_data(id)
        logging.info("Successfully Get Employee Details")
        logging.debug(f"Employee Details are : {employee_detail}")
        return {"status": 200, "message": "Employee Details fetched successfully", "data": employee_detail}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.post("/add_employee")
def add_employee_details(emp: EmployeePayroll):
    """
        desc: post method to add employee details
        param: name, profile_image, gender, department, salary, start_date, notes
        return: employee details added in SMD format
    """
    try:
        employee_details = operation.add_employee(emp.name, emp.profile_image, emp.gender, emp.department, emp.salary,
                                                     emp.start_date, emp.notes)
        logging.info("Successfully Added Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        return {"status": 200, "message": "Successfully Added Employee Details", "data": employee_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.delete("/delete_employee")
def delete_employee_details(id:int):
    """
        desc: delete method to delete employee details
        param: id
        return: updated employee details in SMD format
    """
    try:
        message = operation.delete_employee_details(id)
        logging.info("Successfully Deleted The Employee Details")
        logging.debug(f"Employee ID is : {id}")
        return {"status": 200, "message": message}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/update_employee_name")
def update_employee_name(id: int, name: str):
    """
        desc: put method to update employee name
        param: id, name
        return: updated employee details in SMD format
    """
    try:
        updated_details = operation.update_employee_name(id, name)
        return {"status": 200, "message": "Employee name updated successfully", "data": updated_details}
    except Exception as e:
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/update_employee_profile")
def update_employee_profile(id: int, profile_image: str):
    """
        desc: put method to update employee profile image
        param: id, profile image
        return: updated employee details in SMD format
    """
    try:
        updated_details = operation.update_employee_profile_img(id, profile_image)
        return {"status": 200, "message": "Employee profile image updated successfully", "data": updated_details}
    except Exception as e:
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/update_employee_salary")
def update_employee_salary(id: int, salary: float):
    """
        desc: put method to update employee salary
        param: id, salary
        return: updated employee details in SMD format
    """
    try:
        updated_details = operation.update_employee_salary(id, salary)
        return {"status": 200, "message": "Employee salary updated successfully", "data": updated_details}
    except Exception as e:
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/update_employee_department")
def update_employee_department(id: int, department: str):
    """
        desc: put method to update employee department
        param: id, department
        return: updated employee details in SMD format
    """
    try:
        updated_details = operation.update_employee_department(id, department)
        return {"status": 200, "message": "Employee salary updated successfully", "data": updated_details}
    except Exception as e:
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/update_employee_gender")
def update_employee_gender(id: int, gender: str):
    """
        desc: put method to update employee gender
        param: id, gender
        return: updated employee details in SMD format
    """
    try:
        updated_details = operation.update_employee_gender(id, gender)
        return {"status": 200, "message": "Employee salary updated successfully", "data": updated_details}
    except Exception as e:
        return {"status": 500, "message": f"Error : {e}"}




