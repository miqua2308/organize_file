import os
import shutil

# Define the folder to organize
source_folder = "D:/"

# Define file categories and their extensions
categories = {
    "Working file": [".xls", ".xlsx", ".doc", ".docx", ".pdf",".pptx",".ppt",".pptm"],
    "Media": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4", ".mkv", ".avi", ".mov",".mp3",".wmv",".webp",".svg"],
    "data": [".json",".csv"],
    "Jupyter": [".ipynb"],
    "Sql": [".sql"],
    "App": [".exe"],
    "Text": [".txt",".log"]
}
working_file_subcategories = {
    "Word": [".doc", ".docx"],
    "PDF": [".pdf"],
    "Excel": [".xls", ".xlsx"],
    "PowerPoint": [".ppt", ".pptx", ".pptm"]
}
media_subcategories = {
    "image": [".jpg", ".jpeg", ".png", ".gif",".webp",".svg"],
    "Video": [".mp4",".wmv",".mov"],
    "Music": [".mp3"]
}


# Create subfolders and move files
def organize_folder(folder):
    for category, extensions in categories.items():
        # Create category folder if it doesn't exist
        category_folder = os.path.join(folder, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        # Move files into their respective category folder
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(category_folder, file_name))   
                   
    for file_origin in os.listdir(folder):
        if file_origin == "Working file":
            file_path = os.path.join(folder, file_origin)
            print(file_path)
            for subcategory, extensions in working_file_subcategories.items():
                # Create subcategory folder if it doesn't exist
                subcategory_folder = os.path.join(file_path, subcategory)
                if not os.path.exists(subcategory_folder):
                    os.makedirs(subcategory_folder)
                for file_name in os.listdir(file_path):
                    file_path_2 = os.path.join(file_path, file_name)
                    if os.path.isfile(file_path_2) and any(file_name.lower().endswith(ext) for ext in extensions):
                        shutil.move(file_path_2, os.path.join(subcategory_folder, file_name)) 
                        
    for file_origin in os.listdir(folder):
        if file_origin == "Media":
            file_path = os.path.join(folder, file_origin)
            print(file_path)
            for subcategory, extensions in media_subcategories.items():
                # Create subcategory folder if it doesn't exist
                subcategory_folder = os.path.join(file_path, subcategory)
                if not os.path.exists(subcategory_folder):
                    os.makedirs(subcategory_folder)
                for file_name in os.listdir(file_path):
                    file_path_2 = os.path.join(file_path, file_name)
                    if os.path.isfile(file_path_2) and any(file_name.lower().endswith(ext) for ext in extensions):
                        shutil.move(file_path_2, os.path.join(subcategory_folder, file_name)) 
            
        

# Run the function
organize_folder(source_folder)