'''
@author: Shivam Mishra
@date: 29-12-21 10:42 PM

'''
from database_connection import DBConnection


class DBOperations:
    """
    Contains different methods to add, delete, update, and retrive employee details
    """

    connection = DBConnection().establish_connection()
    cursor = connection.cursor()

    def get_employee_details(self):
        """
            desc: get all employee details
            return: employee_details list
        """
        self.cursor.execute('select * from employee_details')
        employee_details = [i for i in self.cursor]
        return employee_details

    def add_employee(self, name, profile, gender, department, salary, start_date, notes):
        """
            desc: add employee to table
            param: name, profile, gender, department, salary, start_date, notes
            return: string
        """
        query = "insert into employee_details (name, profile_image, gender, department, salary, start_date, notes) VALUES \
            ('%s','%s', '%s', '%s', %0.2f, '%s', '%s')" \
            % (name, profile, gender, department, salary, start_date, notes)
        self.cursor.execute(query)
        self.connection.commit()
        return "Employee added successfully"

    def delete_employee_details(self, id:int):
        """
            desc: delete employee from table
            param: id
            return: string
        """
        query = "delete from employee_details where id=%d" %id
        self.cursor.execute(query)
        self.connection.commit()
        return "Employee deleted successfully"

    def update_employee_details(self, id, salary):
        """
            desc: update employee salary to table
            param: id, salary
            return: string
        """
        query = "update employee_details set salary = %0.2f where id = %d" %(salary, id)
        self.cursor.execute(query)
        self.connection.commit()
        return "Employee details updated successfully"



