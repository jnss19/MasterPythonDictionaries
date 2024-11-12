# Dictionaries Of Employee
employees = {
    'employee1': {
        'name': 'Ichigo Kurosaki',
        'job_title': 'Manager'
    },
    'employee2': {
        'name': 'Haruka Sakura',
        'job_title': 'Developer'
    },
    'employee3': {
        'name': 'Gojo Satoru',
        'job_title': 'Designer'
    },
    'employee4': {
        'name': 'Ippo Makunochi',
        'job_title': 'Sales Associate'
    },
    'employee5': {
        'name': 'Yamamoto Tsugikuni',
        'job_title': 'HR Specialist'
    }
}

def display_employees(employee_dict):
    print("Employees:")
    for key, details in employee_dict.items():
        print(f"{key}: Employee Name: {details['name']}, Job Title: {details['job_title']}")

display_employees(employees)
