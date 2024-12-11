import os
from setuptools import setup, find_packages

def setup_directories(directories: list[str] = ['data', 'logs', 'reports', 'notebook']):
    """
    Ensures the required project directories exist. If they do not, creates them.

    Parameters:
    -----------
    directories : list[str]
        A list of directory paths that need to be created. Defaults to common project folders
        such as "data", "logs", "output", and "notebooks".

    Outputs:
    --------
    None
        Creates missing directories and logs their creation status.
    """
    print("Setting up directories...")
    
    # Iterate through the list of required directories.
    for directory in directories:
        # Check if the directory exists; if not, create it.
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create the directory and any necessary parent directories.
            print(f"Created directory: {directory}")
        else:
            # Log if the directory already exists.
            print(f"Directory already exists: {directory}")

def get_requirements(filepath: str) -> list[str]:
    """
    Reads the "requirements.txt" file, processes it to extract package dependencies, 
    and returns a list of requirements, with potential cleanup if needed.
    
    Parameters:
    -----------
    filepath : str
        The path to the "requirements.txt" file containing package dependencies.

    Outputs:
    --------
    list[str] : 
        A list of package requirements (dependencies) with any unnecessary characters 
        (like newlines) removed, and any development flags like "-e ." omitted.
    """
    
    # Initialize an empty list to hold the requirements.
    requirements = []

    # Open the file at the given filepath to read the contents.
    with open(filepath) as file:
        # Read all the lines from the file and store them in the requirements list.
        requirements = file.readlines()

        # Remove newline characters "\n" from each requirement to clean up the entries.
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        # If the list contains "-e ." (which is used for editable installs), remove it.
        # This ensures that editable installs are not included in production dependencies.
        if "-e ." in requirements:
            requirements.remove("-e .")
    
    # Return the processed list of requirements.
    return requirements


setup(
    name="signal_adjustment",
    author="B M Tazbiul Hassan Anik",
    author_email="anik.bmtazbiulhassan@gmail.com", 
    packages=find_packages(),
    install_requires=get_requirements(filepath="requirements.txt")
)




