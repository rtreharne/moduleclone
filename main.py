from canvasapi import Canvas
import getpass
import datetime
import tqdm
import os
import warnings

warnings.filterwarnings('ignore', 'SettingWithCopyWarning')
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    print(
"""
                      ░▓▓░   ░░                             
                       ░░    ▓▓                             
                   ░░       ░██░       ░░                   
                 ░░█▒░  ░██████████░  ░▒█░░                 
            ░▒░  ░░█▒░░     ░██░      ░▒█░░ ░░▒░            
             ▒     ░░        ▓▓        ░░    ░▒             
                    ░░░      ░░      ░░░                    
                 ▓███████▓░      ░▓███████▓                 
        ░▒▒░   ▒██▒░░░  ▒██▒░  ░▒██▒░░▒ ░▒██▒   ░▒▒░        
        ░███▓ ░██░░█▒    ░██░░░░██░░▓▓░▒█░░██░ ▓███░        
        ░▓░▓█▒▒█▒░▓░      ▒██████▒░█░░█░░  ▒█▒▒█▓░▓░        
         ░ ▒█▓░██░        ▓█▒░░▒█▓░░▓▓░   ░██░▓█▓ ░         
          ░▓██░▓█▓░     ░▒██░  ░▓█▓░     ░▓█▓░██▓░          
          ░████░░███▓▓▓███▒░    ░▒███▓▓▓███░░████░          
          ▒▒▒██░  ░▒▓▓▓▒░░        ░░▒▓▓▓▒░  ░██▒▒▒          
           ░███░       ░░░░      ░░░░       ░███░           
           ▒███░     ▒██████▒  ▒██████▒     ░███▒           
          ░██▒░    ▒████████████████████▒    ░▒██░          
         ░▓█████▓███████████▒░░▒███████████▓▓████▓░         
         ░███████████████▓░      ░▒███████████████░         
         ▓██▓███░░░░░░░     ░▓▓░     ░░░░░░░███▓██▓░        
        ░▓█░▓█████▓▓▓▓▓ ░  ▒████▒  ░ ▓▓▓▓▓█████▓░█▓░        
         ▒▓░███████████░▓░░██████░░█░███████████░▓▒         
          ░ █████████████▓▒██████▒▓█████████████ ░          
            ░██▒████████████████████████████▒██░            
             ▓█░████████████████████████████░█▓░            
             ░▓░▒██████████████████████████▒░▓░             
                 ▓██▒▓████████████████▓▒██▓                 
                 ░██▒░███▓▓███████▓███▒▒██░                 
                   ▒█░▒██▓▒██████▓▒██▒░█▒                   
                    ░░░░██░▓█████░▓█░ ░░                    
                         ▒▒░▓███░▒▒░                        
                             ▒▓                                             
""" )
    print("")
    print("www.canvaswizards.org.uk")
    print("")
    print("Welcome to the Canvas Module Cloner!")
    print("By Robert Treharne, University of Liverpool. 2024")
    print("")

    # if config.py exists, import it
    try:
        from config import CANVAS_URL, CANVAS_TOKEN
    except ImportError:
        CANVAS_URL = input('Enter your Canvas URL: ')
        print("")
        CANVAS_TOKEN = getpass.getpass('Enter your Canvas token: ')
        print("")

    # if course_id in config.py, use it
    try:
        from config import course_id
    except ImportError:
        course_id = int(input('Enter the course ID: '))
        print("")


    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)

    try: 
        course = canvas.get_course(course_id)
    except:
        print("Course not found.")
        return None
    
    print("")
    module = choose_module(course)

    courses = get_courses(canvas)
    
    check = input("I will now attempt to clone the module into all courses listed in your courses.csv file. Confirm with 'Y':" )
    if check.lower() == "y":
        print("")
        for course in courses:
            import_module(course_id, module.id, course)

def choose_module(course):
    modules = [x for x in course.get_modules()]
    for i, module in enumerate(modules):
        print(f"{i+1}. {module.name}")
    
    try:
        module_num = int(input("Choose module to clone (enter number): "))
        module = modules[module_num-1]
        return module
    except:
        choose_module(course)

def get_courses(canvas, fname="courses.csv"):
    with open(fname, "r") as f:
        courses = []
        lines = f.readlines()
        for line in lines:
            course_id, course_sis_id = [line.split(",")[0], line.split(",")[1]]
            if course_sis_id != "":
                try:
                    courses.append(canvas.get_course(course_sis_id, use_sis_id=True))
                except:
                    continue
            else:
                try:
                    courses.append(canvas.get_course(int(course_id)))
                except:
                    continue
        return courses

def import_module(source_course_id, module_id, destination_course):
    """
    This function will copy a module from a source course to a destination course.
    params:
    source_course_id: int
    module_id: int
    destination_course: Canvas course object
    """

    try:

        destination_course.create_content_migration(
            migration_type="course_copy_importer",
            settings = {"source_course_id": str(source_course_id), "insert_into_module_position": 1},
            select = {"modules": [module_id]}
        )
        print(f"SUCCESS: Module is being imported into {destination_course.name}")
    except:
        print(f"ERROR: There was a roblem importing the module into {destination_course.name}")


if __name__ == "__main__":
    main()