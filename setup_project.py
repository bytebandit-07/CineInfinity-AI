import os

directories = [
    "backend/routes",
    "backend/models",
    "backend/utils",
    "frontend/templates",
    "frontend/static/css",
    "frontend/static/js",
    "database"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

print("Project structure created successfully!")
 
