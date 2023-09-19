import os, subprocess
from git import Repo

# Define the directory structure
root_dir = "my_git_repo_00X"
dirs_and_files = {
    "src": {
        "python": ["main.py", "utils.py"],
        "java": ["Main.java", "Utils.java"]
    },
    "data": ["data.csv", "config.json"],
    "docs": ["README.md"]
}

# Create the root directory
os.makedirs(root_dir, exist_ok=True)

# Initialize a Git repository in the root directory
subprocess.check_call(f"git fetch --all; git reset origin/master; ", shell=True)
repo = Repo.init(root_dir)

# Function to create directories and files recursively
def create_dirs_and_files(parent_dir, structure):
    for name, content in structure.items():
        path = os.path.join(parent_dir, name)
        if isinstance(content, list):
            # Create files
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                file_path = os.path.join(path, file_name)
                with open(file_path, "w") as f:
                    f.write(f"This is {file_name}\n")
        elif isinstance(content, dict):
            # Recursively create subdirectories and files
            os.makedirs(path, exist_ok=True)
            create_dirs_and_files(path, content)

# Create the directory structure and files
create_dirs_and_files(root_dir, dirs_and_files)

# Add all files to the Git repository
repo.index.add(["."])

# Commit the changes
repo.index.commit("Initial commit")

# Print the repository tree
def print_tree(root_dir):
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}[{os.path.basename(root)}]")
        subindent = " " * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

print_tree(root_dir)

# You can push this repository to a remote repository if needed.
repo.create_remote('origin', 'https://github.com/eaedk/repo.git')
repo.remotes.origin.push()
