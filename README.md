# Terraform Folder Structure Automation
This Python script automates the creation of a Terraform folder structure for managing infrastructure. It reads configuration values from a .env file, allowing users to dynamically define the environments (e.g., production, staging, dev) and the root directory where the structure should be created.
Features

      •	Dynamic Environment Configuration: Enable or disable production, staging, and dev environments through the .env file.
      •	Custom Root Directory: Specify the root directory where the Terraform structure will be created.
      •	Modular Structure: Automatically generates Terraform modules and global configurations.
      •	Easy-to-Use: Simple setup and execution with minimal dependencies.
________________________________________
Folder Structure
When the script runs, it creates the following folder structure (example for production=yes and dev=yes):

    plaintext
    CopyEdit
    <ROOT_FOLDER>/infra/
    ├── global/
    │   ├── providers.tf
    │   ├── versions.tf
    │   └── variables.tf
    ├── modules/
    │   ├── compute_instance/
    │   │   ├── main.tf
    │   │   ├── variables.tf
    │   │   ├── outputs.tf
    │   │   └── README.md
    │   ├── firewall/
    │   │   ├── main.tf
    │   │   ├── variables.tf
    │   │   ├── outputs.tf
    │   │   └── README.md
    │   └── network/
    │       ├── main.tf
    │       ├── variables.tf
    │       ├── outputs.tf
    │       └── README.md
    └── environments/
        ├── dev/
        │   ├── main.tf
        │   ├── variables.tf
        │   ├── outputs.tf
        │   ├── backend.tf
        │   └── terraform.tfvars
        └── prod/
            ├── main.tf
            ├── variables.tf
            ├── outputs.tf
            ├── backend.tf
            └── terraform.tfvars
•	global/: Contains shared Terraform configurations (providers, versions, and global variables).
•	modules/: Includes reusable Terraform modules for managing resources (e.g., VMs, firewalls, networks).
•	environments/: Environment-specific configurations (prod, staging, dev) with their own state and settings.
________________________________________


Prerequisites
    1.	Python 3.6+: Ensure you have Python installed on your system.
    2.	python-dotenv Library: Install this library for reading environment variables from a .env file:
    
    bash
    CopyEdit
    pip install python-dotenv
________________________________________
Setup and Usage
1. Clone the Repository
Clone this repository to your local machine:
bash
CopyEdit
git clone https://github.com/your-username/terraform-folder-automation.git
cd terraform-folder-automation
2. Configure the .env File
Create a .env file in the root of the repository with the following structure:
dotenv
CopyEdit
# Root directory where the folder structure will be created

      ROOT_FOLDER=/path/to/your/root/directory

# Enable or disable environments

      production=yes
      staging=no
      dev=yes
      
•	Replace /path/to/your/root/directory with the desired root folder (e.g., /var/www/project1).
•	Set yes or no for production, staging, and dev to control which environments are created.

3. Run the Script
   
      Execute the Python script to generate the folder structure:
      bash
      CopyEdit
      python create_terraform_structure.py
   
5. Verify the Structure
   
      The Terraform folder structure will be created under <ROOT_FOLDER>/infra/.
________________________________________
Example Output

      Given the following .env file:
      dotenv
      CopyEdit
      ROOT_FOLDER=/var/www/project1
      production=yes
      staging=no
      dev=yes
      The script will create the folder structure under /var/www/project1/infra/, including prod and dev environments but excluding staging.
________________________________________
Customization
You can customize the script by modifying the FOLDER_STRUCTURE dictionary in the create_terraform_structure.py file to add new modules, files, or environments as needed.
________________________________________
Troubleshooting
Error: "ROOT_FOLDER is not defined in the .env file."
Ensure that the .env file exists and includes the ROOT_FOLDER variable pointing to a valid directory.
Error: "Root directory '<ROOT_FOLDER>' does not exist."
Verify that the directory specified in ROOT_FOLDER exists. If not, create it manually or specify a valid path.
________________________________________
Contributing
Feel free to contribute by submitting issues or pull requests to improve the functionality of this script. Suggestions for additional features are always welcome!
________________________________________
License
This project is licensed under the MIT License. See the LICENSE file for details.
________________________________________
Author
Ranuka Thilakarathne
https://www.linkedin.com/in/ranuka-thilakarathne-47a1a4162/
