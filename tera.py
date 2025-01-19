#Coded By Ranuka Thilakarathne @ITQqubes. This script will create a folder structure for Terraform projects.

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


INFRA_FOLDER_NAME = "infra"  
FOLDER_STRUCTURE = {
    "global": ["providers.tf", "versions.tf", "variables.tf"],
    "modules": {
        "compute_instance": ["main.tf", "variables.tf", "outputs.tf", "README.md"],
        "firewall": ["main.tf", "variables.tf", "outputs.tf", "README.md"],
        "network": ["main.tf", "variables.tf", "outputs.tf", "README.md"],
    },
    "environments": {
        "prod": ["main.tf", "variables.tf", "outputs.tf", "backend.tf", "terraform.tfvars"],
        "staging": ["main.tf", "variables.tf", "outputs.tf", "backend.tf", "terraform.tfvars"],
        "dev": ["main.tf", "variables.tf", "outputs.tf", "backend.tf", "terraform.tfvars"],
    },
}

def create_structure(base_dir, structure):
    """Recursively create directories and files based on the structure."""
    for key, value in structure.items():
        path = os.path.join(base_dir, key)
        if isinstance(value, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, value)
        else:
            os.makedirs(base_dir, exist_ok=True)
            for file in value:
                file_path = os.path.join(base_dir, file)
                with open(file_path, "w") as f:
                    f.write("")  


def main():
    root_directory = os.getenv("ROOT_FOLDER")
    if not root_directory:
        print("Error: ROOT_FOLDER is not defined in the .env file.")
        return

    
    if not os.path.exists(root_directory):
        print(f"Error: Root directory '{root_directory}' does not exist.")
        return

    
    infra_dir = os.path.join(root_directory, INFRA_FOLDER_NAME)
    os.makedirs(infra_dir, exist_ok=True)

    
    create_structure(infra_dir, {"global": FOLDER_STRUCTURE["global"]})
    create_structure(infra_dir, {"modules": FOLDER_STRUCTURE["modules"]})

    
    production_enabled = os.getenv("production", "no").lower() == "yes"
    staging_enabled = os.getenv("staging", "no").lower() == "yes"
    dev_enabled = os.getenv("dev", "no").lower() == "yes"

    
    env_structure = {}
    if production_enabled:
        env_structure["prod"] = FOLDER_STRUCTURE["environments"]["prod"]
    if staging_enabled:
        env_structure["staging"] = FOLDER_STRUCTURE["environments"]["staging"]
    if dev_enabled:
        env_structure["dev"] = FOLDER_STRUCTURE["environments"]["dev"]

    create_structure(os.path.join(infra_dir, "environments"), env_structure)

    print(f"Infrastructure folder structure created successfully at '{infra_dir}'!")


if __name__ == "__main__":
    main()
