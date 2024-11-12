# Univerties Dictionaries
universities = {
    'university1': {
        'name': 'Harvard University',
        'location': 'Cambridge, Massachusetts, USA'
    },
    'university2': {
        'name': 'Stanford University',
        'location': 'Stanford, California, USA'
    },
    'university3': {
        'name': 'Massachusetts Institute of Technology (MIT)',
        'location': 'Cambridge, Massachusetts, USA'
    },
    'university4': {
        'name': 'University of Oxford',
        'location': 'Oxford, England'
    },
    'university5': {
        'name': 'University of Tokyo',
        'location': 'Tokyo, Japan'
    }
}

# Function to display university details
def display_universities(university_dict):
    print("Universities:")
    for key, details in university_dict.items():
        print(f"{key}: Name: '{details['name']}', Location: {details['location']}")

# Display the universities
display_universities(universities)