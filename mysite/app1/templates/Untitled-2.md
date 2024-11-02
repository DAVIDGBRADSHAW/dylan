"""
Unit 1 Walk through
Django Installation 

0.
-->Install virtualenv using pip: "pip install virtualenv".
-->Create a virtual environment: "virtualenv your_env_name".
-->Activate the virtual environment:
    -->Windows: "your_env_name\Scripts\activate".
    -->macOS/Linux: "source your_env_name/bin/activate".   

# 
# 

1. Install Django inside the virtual environment:
pip install django

# 
# 

2. Confirm install
python -m django --version

# 
# 

3. Create project from scratch
We will now use some commands for Django as we have it installed

django-admin

The above will show available sub commands. For now we will use startproject.

# 
# 

4. django-admin startproject django_project

The command above will create a Django project directory. The directory name will be
django_project. The name should be relevant to your project.

Show the directory structure either in Terminal/VS Code/Sublime etc. Talk through each of the
files. If on Mac a handy tool to view the tree structure can be installed with brew install tree.
More details here https://michaelsoolee.com/tree-tool/

# 
# 
