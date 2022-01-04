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
        try:
            self.cursor.execute('select * from employee_details')
            employee_details = [i for i in self.cursor]
            return employee_details
        except Exception as e:
            return {"message": f"Error : {e}"}

    def get_single_emp_data(self,id):
        """
            desc: get single employee detail
            return: employee detail
        """
        try:
            self.cursor.execute(f'select * from employee_details where id={id}')
            employee_detail = [i for i in self.cursor]
            return employee_detail
        except Exception as e:
            return {"message": f"Error : {e}"}

    def add_employee(self, name, profile, gender, department, salary, start_date, notes):
        """
            desc: add employee to table
            param: name, profile, gender, department, salary, start_date, notes
            return: employee detail
        """
        try:
            query = "insert into employee_details (name, profile_image, gender, department, salary," \
                                                   " start_date, notes) VALUES \
                                                   ('%s','%s', '%s', '%s', %0.2f, '%s', '%s')" \
                                                   % (name, profile, gender, department, salary, start_date, notes)
            self.cursor.execute(query)
            self.connection.commit()
            query2 = "select * from employee_details where name='%s'" %name
            self.cursor.execute(query2)
            employee_detail = [i for i in self.cursor]
            return employee_detail
        except Exception as e:
            return {"message": f"Error : {e}"}

    def delete_employee_details(self, id:int):
        """
            desc: delete employee from table
            param: id
            return: string
        """
        try:
            query = "delete from employee_details where id=%d" %id
            self.cursor.execute(query)
            self.connection.commit()
            return f"Employee deleted successfully with id: {id}"
        except Exception as e:
            return {"message": f"Error : {e}"}

    def update_employee_salary(self, id, salary):
        """
            desc: update employee salary
            param: id, salary
            return: updated detail in dict form
        """
        try:
            query = "update employee_details set salary = %0.2f where id = %d" %(salary, id)
            self.cursor.execute(query)
            self.connection.commit()
            updated_detail = self.get_single_emp_data(id)
            return updated_detail
        except Exception as e:
            return {"message": f"Error : {e}"}

    def update_employee_name(self, id, name):
        """
            desc: update employee name
            param: id, name
            return: updated detail in dict form
        """
        try:
            query = "update employee_details set name = %s where id = %d" % (name, id)
            self.cursor.execute(query)
            self.connection.commit()
            updated_detail = self.get_single_emp_data(id)
            return updated_detail
        except Exception as e:
            return {"message": f"Error : {e}"}

    def update_employee_profile_img(self, id, profile_image):
        """
            desc: update employee profile img
            param: id, name
            return: updated detail in dict form
        """
        try:
            query = "update employee_details set profile_image = %s where id = %d" % (profile_image, id)
            self.cursor.execute(query)
            self.connection.commit()
            updated_detail = self.get_single_emp_data(id)
            return updated_detail
        except Exception as e:
            return {"message": f"Error : {e}"}

    def update_employee_department(self, id, department):
        """
            desc: update employee department
            param: id, department
            return: updated detail in dict form
        """
        try:
            query = "update employee_details set department = %s where id = %d" % (department, id)
            self.cursor.execute(query)
            self.connection.commit()
            updated_detail = self.get_single_emp_data(id)
            return updated_detail
        except Exception as e:
            return {"message": f"Error : {e}"}

    def update_employee_gender(self, id, gender):
        """
            desc: update employee gender
            param: id, gender
            return: updated detail in dict form
        """
        try:
            query = "update employee_details set gender = %s where id = %d" % (gender, id)
            self.cursor.execute(query)
            self.connection.commit()
            updated_detail = self.get_single_emp_data(id)
            return updated_detail
        except Exception as e:
            return {"message": f"Error : {e}"}



