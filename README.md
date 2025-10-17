## Overview

AI File Manager is a background automation agent powered by AI tools. It organizes files, performs drive backups, removes duplicates, and keeps your workspace clean—using Python scripts and batch automation.

## Features
1. Intelligent file organization
2. Automated backup routines
3. Duplicate file detection and removal
4. Continuous background monitoring using scheduled tasks

## Prerequisites
1. Python 3.11 or higher installed
2. PowerShell
3. Basic knowledge of command line

## Installation Steps

1. Clone this Repository

        git clone https://github.com/SANGIDSK/ai_file_manager.git

2. Install Required Python Packages

        pip install -r requirements.txt
   (Add all dependencies in your requirements.txt)

3. Configure Your Environment
   
    i. Place your Python scripts and .bat files within the ai_file_manager directory.
   
    ii. Adjust script paths if necessary.
   
    iii. Set Up Automated Scheduled Task

4. Open PowerShell as administrator.

    (i) Run the following command to create a scheduled task:
   
        schtasks /create /tn "AIFileManager" /tr "D:\ai_file_manager\start_background.bat" /sc onlogon /f
  
    (ii) Check status:
   
        schtasks /query /tn AIFileManager

    (iii) To manually start:
   
        D:\ai_file_manager\start_background.bat

    (iv) Monitor if it’s running:
   
        tasklist | findstr pythonw.exe
  
    (v) Manual Test
   
   Run the batch file manually when needed:

       D:\ai_file_manager\start_background.bat
      
## Confidentiality Notice
The source code is not included for privacy and security. Demo scripts, documentation, and setup instructions are provided to illustrate the workflow.

## License
For demonstration and educational use only.
