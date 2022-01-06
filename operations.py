'''
@author: Shivam Mishra
@date: 29-12-21 10:42 PM

'''
from database_connection import DBConnection


class DBOperations:
    """
    Contains different methods to add, delete, update, and retrieve employee details
    """

    connection = DBConnection().establish_connection()
    cursor = connection.cursor(dictionary=True)

    def get_employee_details(self):
        """
            desc: get all employee details
            return: employee_details
        """
        self.cursor.execute('select * from employee_details')
        employee_details = [i for i in self.cursor]
        return employee_details

    def get_single_emp_data(self,id):
        """
            desc: get single employee detail
            return: employee detail
        """
        if id == "":
            raise Exception({"status": 400, "message": "Employee Details cannot be fetched", "error": "id can't be empty"})
        self.cursor.execute(f'select * from employee_details where id={id}')
        employee_detail = [i for i in self.cursor]
        if not employee_detail:
            raise Exception({"status": 400, "message": "Employee Details cannot be fetched", "error": "id not found"})
        else:
            return employee_detail

    def add_employee(self, id, name, profile, gender, department, salary, start_date, notes):
        """
            desc: add employee to table
            param: name, profile, gender, department, salary, start_date, notes
            return: employee detail
        """

        query = "insert into employee_details (id, name, profile_image, gender, department, salary," \
                                               " start_date, notes) VALUES \
                                               (%d,'%s','%s', '%s', '%s', %0.2f, '%s', '%s')" \
                                               % (id, name, profile, gender, department, salary, start_date, notes)
        self.cursor.execute(query)
        self.connection.commit()
        query2 = "select * from employee_details where name='%s'" %name
        self.cursor.execute(query2)
        employee_detail = [i for i in self.cursor]
        return employee_detail

    def delete_employee_details(self, id:int):
        """
            desc: delete employee from table
            param: id
            return: string
        """
        query = "delete from employee_details where id=%d" %id
        self.cursor.execute(query)
        self.connection.commit()
        return f"Employee deleted successfully with id: {id}"

    def update_employee_salary(self, id, salary):
        """
            desc: update employee salary
            param: id, salary
            return: updated detail in dict form
        """
        query = "update employee_details set salary = %0.2f where id = %d" %(salary, id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.get_single_emp_data(id)
        return updated_detail

    def update_employee_name(self, id, name):
        """
            desc: update employee name
            param: id, name
            return: updated detail in dict form
        """
        query = "update employee_details set name = %s where id = %d" % (name, id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.get_single_emp_data(id)
        return updated_detail

    def update_employee_profile_img(self, id, profile_image):
        """
            desc: update employee profile img
            param: id, name
            return: updated detail in dict form
        """
        query = "update employee_details set profile_image = %s where id = %d" % (profile_image, id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.get_single_emp_data(id)
        return updated_detail

    def update_employee_department(self, id, department):
        """
            desc: update employee department
            param: id, department
            return: updated detail in dict form
        """
        query = "update employee_details set department = %s where id = %d" % (department, id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.get_single_emp_data(id)
        return updated_detail

    def update_employee_gender(self, id, gender):
        """
            desc: update employee gender
            param: id, gender
            return: updated detail in dict form
        """
        query = "update employee_details set gender = %s where id = %d" % (gender, id)
        self.cursor.execute(query)
        self.connection.commit()
        updated_detail = self.get_single_emp_data(id)
        return updated_detail



