# Organize Files Script

This script helps you organize files in a folder by automatically categorizing them into specific subfolders based on their file types. It is useful for decluttering and organizing large collections of files.

## How It Works
The script scans the specified source folder and moves files into predefined categories and subcategories based on their extensions. If a category or subcategory folder does not exist, it is created automatically.

### File Categories
The script organizes files into the following main categories:

1. **Working Files**:
   - Subcategories:
     - **Word**: `.doc`, `.docx`
     - **PDF**: `.pdf`
     - **Excel**: `.xls`, `.xlsx`
     - **PowerPoint**: `.ppt`, `.pptx`, `.pptm`
2. **Media**:
   - File Types: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.mp4`, `.mkv`, `.avi`, `.mov`, `.mp3`, `.wmv`, `.webp`, `.svg`
3. **JSON**:
   - File Types: `.json`, `.csv`
4. **Jupyter**:
   - File Types: `.ipynb`
5. **SQL**:
   - File Types: `.sql`
6. **App**:
   - File Types: `.exe`
7. **Text**:
   - File Types: `.txt`, `.log`

### Customization
You can modify the `categories` and `working_file_subcategories` dictionaries in the script to add or remove categories and subcategories, or to handle different file types.

## Usage
1. Define the folder to organize by modifying the `source_folder` variable in the script:
   ```python
   source_folder = "Your/folder"
   ```
2. Run the script using Python:
   ```bash
   python organize_files.py
   ```
3. The script will create subfolders in the specified directory and move files accordingly.

## Notes
- The script does not delete files; it only moves them to categorized subfolders.
- Files that do not match any category or subcategory will remain in the original folder.

## Future Improvements
- Add more subcategories for better file organization (e.g., categorizing media by image, video, and audio).
- Support for handling duplicate file names.
- Logging for tracking moved files and errors.

Feel free to enhance and adapt this script to fit your specific organizational needs!

