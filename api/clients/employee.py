from api.clients.base_client import BaseClient

class Employee(BaseClient):

    def create_employee(self, payload):
        return self.post("/employees", payload)

    def get_employees(self):
        return self.get("/employees")

    def delete_employee(self, emp_id):
        return self.delete(f"/employees/{emp_id}")