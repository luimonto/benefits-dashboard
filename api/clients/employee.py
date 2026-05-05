from api.clients.base_client import BaseClient

class Employee(BaseClient):

    def create_employee(self, payload):
        return self.post("/api/Employees", payload)

    def get_employees(self):
        return self.get("/api/Employees")

    def get_employee(self, emp_id):
        return self.get(f"/api/Employees/{emp_id}")

    def update_employee(self, payload):
        return self.put("/api/Employees", payload)

    def delete_employee(self, emp_id):
        return self.delete(f"/api/Employees/{emp_id}")