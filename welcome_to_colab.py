

import json
from datetime import datetime
from typing import Dict, List, Optional

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.communication_logs: List[Dict] = []
        self.sales_pipeline: List[Dict] = [{"stage": "Lead", "created": datetime.now().isoformat(), "notes": ""}]

    def add_communication(self, log_type: str, message: str):
        log = {
            "type": log_type,  # e.g., 'email', 'call', 'meeting'
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self.communication_logs.append(log)

    def update_pipeline(self, stage: str, notes: str = ""):
        if self.sales_pipeline:
            self.sales_pipeline[-1]["stage"] = stage
            self.sales_pipeline[-1]["notes"] = notes
            self.sales_pipeline[-1]["updated"] = datetime.now().isoformat()
        else:
            self.sales_pipeline.append({"stage": stage, "created": datetime.now().isoformat(), "notes": notes})

    def get_status(self) -> str:
        return self.sales_pipeline[-1]["stage"] if self.sales_pipeline else "No pipeline"

class CRM:
    def __init__(self, filename: str = "crm_data.json"):
        self.customers: Dict[str, Customer] = {}
        self.filename = filename
        self.load_data()

    def add_customer(self, customer_id: str, name: str, email: str, phone: str):
        if customer_id in self.customers:
            print(f"Customer {customer_id} already exists.")
            return
        self.customers[customer_id] = Customer(customer_id, name, email, phone)
        self.save_data()

    def get_customer(self, customer_id: str) -> Optional[Customer]:
        return self.customers.get(customer_id)

    def add_communication(self, customer_id: str, log_type: str, message: str):
        customer = self.get_customer(customer_id)
        if customer:
            customer.add_communication(log_type, message)
            self.save_data()
            print(f"Log added for {customer_id}.")
        else:
            print(f"Customer {customer_id} not found.")

    def update_pipeline_stage(self, customer_id: str, stage: str, notes: str = ""):
        customer = self.get_customer(customer_id)
        if customer:
            customer.update_pipeline(stage, notes)
            self.save_data()
            print(f"Pipeline updated for {customer_id} to {stage}.")
        else:
            print(f"Customer {customer_id} not found.")

    def list_customers(self):
        for cid, cust in self.customers.items():
            print(f"{cid}: {cust.name} - {cust.get_status()}")

    def save_data(self):
        data = {}
        for cid, cust in self.customers.items():
            data[cid] = {
                "name": cust.name,
                "email": cust.email,
                "phone": cust.phone,
                "communication_logs": cust.communication_logs,
                "sales_pipeline": cust.sales_pipeline
            }
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for cid, info in data.items():
                    cust = Customer(cid, info["name"], info["email"], info["phone"])
                    cust.communication_logs = info["communication_logs"]
                    cust.sales_pipeline = info["sales_pipeline"]
                    self.customers[cid] = cust
        except FileNotFoundError:
            pass

# Example usage and menu
def main():
    crm = CRM()

    while True:
        print("\nCRM Menu:")
        print("1. Add Customer")
        print("2. List Customers")
        print("3. Add Communication Log")
        print("4. Update Sales Stage")
        print("5. View Customer Details")
        print("6. Quit")
        choice = input("Choose: ").strip()

        if choice == '1':
            cid = input("Customer ID: ")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            crm.add_customer(cid, name, email, phone)

        elif choice == '2':
            crm.list_customers()

        elif choice == '3':
            cid = input("Customer ID: ")
            log_type = input("Log type (email/call/meeting): ")
            msg = input("Message: ")
            crm.add_communication(cid, log_type, msg)

        elif choice == '4':
            cid = input("Customer ID: ")
            stage = input("New stage (Lead/Qualified/Proposal/Closed): ")
            notes = input("Notes: ")
            crm.update_pipeline_stage(cid, stage, notes)

        elif choice == '5':
            cid = input("Customer ID: ")
            cust = crm.get_customer(cid)
            if cust:
                print(f"Name: {cust.name}, Email: {cust.email}, Phone: {cust.phone}")
                print("Pipeline:", cust.sales_pipeline)
                print("Logs:")
                for log in cust.communication_logs:
                    print(f"  {log['timestamp']}: {log['type']} - {log['message']}")
            else:
                print("Customer not found.")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()