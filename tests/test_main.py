'''
@author: Shivam Mishra
@date: 06-01-22 11:28 AM
@desc: api testing done with help of testclient
'''
import pytest
from fastapi.testclient import TestClient
from main import app


class TestApi:

    client = TestClient(app)

    def test_all_employee_data_is_retrieved(self):
        response = self.client.get('/employee_details')
        assert response.json()["message"] == "Employee Details fetched successfully"

    def test_all_employee_data_is_not_retrieved_if_path_is_incorrect(self):
        response = self.client.get('/employee_detail')
        assert response.json()["detail"] == "Not Found"

    def test_single_employee_data_is_retrieved(self):
        response = self.client.get('/emp?id=3')
        response.json()["data"][0]["name"] == "Alex"

    def test_single_employee_data_if_id_incorrect_not_retrieved(self):
        response = self.client.get('/emp?id=1')
        response.json()[0]["error"] == "id not found"

    @pytest.mark.parametrize("emp_data",[{
                                          "id": 101,
                                          "name": "Alex",
                                          "profile_image": "E:pythonProjectfastApi_projectsphotoemployee-img3.png",
                                          "gender": "Male",
                                          "department": "HR",
                                          "salary": 40000,
                                          "start_date": "2010-01-02",
                                          "notes": "Hard Working"
                                        }])
    def test_employee_data_is_added(self,emp_data):
        response = self.client.post('/add_employee', json=emp_data)
        assert response.json()["message"] == "Employee Details added successfully"

    @pytest.mark.parametrize("emp_data",[{
                                          "id": 101,
                                          "name": "Dipak",
                                          "profile_image": "E:pythonProjectfastApi_projectsphotoemployee-img3.png",
                                          "gender": "Male",
                                          "department": "HR",
                                          "salary": 40000,
                                          "start_date": "2010-01-02",
                                          "notes": "Hard Working"
                                        }])
    def test_all_employee_data_is_not_added_for_duplicate_id(self, emp_data):
        response = self.client.post('/add_employee', json=emp_data)
        assert response.json()["message"] == "Error : Id already exists"

    def test_for_employee_gets_deleted_by_passing_id(self):
        response = self.client.delete('/delete_employee101')
        assert response.json()["message"] == "Successfully Deleted The Employee Details"

    def test_passing_wrong_employee_id_for_deleting(self):
        response = self.client.delete('/delete_employee45')
        assert response.json()["message"] == "Error : Id not found"

    @pytest.mark.parametrize("id, salary",[(100,5000),(42,10000),(43,20000)])
    def test_for_employee_salary_gets_updated(self, id, salary):
        response = self.client.put(f'/update_employee_salary?id={id}&salary={salary}')
        assert response.json()["message"] == "Employee salary updated successfully"

    @pytest.mark.parametrize("id, salary",[(111,5000),(444,10000),(333,20000)])
    def test_for_employee_salary_not_updated_if_wrong_id(self, id, salary):
        response = self.client.put(f'/update_employee_salary?id={id}&salary={salary}')
        assert response.json()["message"] == "Error : Id not found"

    @pytest.mark.parametrize("id, name",[(100,"Aman"),(42,"Rahul"),(43,"Santosh")])
    def test_for_employee_name_gets_updated(self, id, name):
        response = self.client.put(f'/update_employee_name?id={id}&name=%22{name}%22')
        assert response.json()["message"] == "Employee name updated successfully"

    @pytest.mark.parametrize("id, name",[(111,"Aman"),(444,"Amar"),(333,"Shiv")])
    def test_for_employee_name_not_updated_if_wrong_id(self, id, name):
        response = self.client.put(f'/update_employee_name?id={id}&name=%22{name}%22')
        assert response.json()["message"] == "Error : Id not found"

    @pytest.mark.parametrize("token",[{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDV9.80LF03iG4OIHVqThh13ONxA4QVxhMJm-SrJzInSHpqk"}])
    def test_for_login_is_valid(self,token):
        response = self.client.post("/login/", headers=token)
        assert response.json()["message"] == "Successfully Logged In"

    @pytest.mark.parametrize("token",[{"token": "yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDV9.80LF03iG4OIHVqThh13ONxA4QVxhMJm-SrJzInSHpqk"}])
    def test_for_login_is_not_valid(self,token):
        response = self.client.post("/login/", headers=token)
        assert response.json()["message"] == "You are not authorized employee"























