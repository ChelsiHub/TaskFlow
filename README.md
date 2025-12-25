# TaskFlow

TaskFlow is a Python-based **Task Automation & Reporting System** designed to help users create, assign, and manage tasks efficiently. It includes task tracking, progress reporting, and automated email notifications for task updates.

## Features

- Create and assign tasks to users  
- Track task status and deadlines  
- Generate automated progress reports  
- Send email notifications for task updates  
- Role-based access (Admin/User)  
- Console-based interface for managing tasks

## Tech Stack / Libraries Used

- **Python 3.14.4**  
- **smtplib** and **email** for sending emails  
- **datetime** for task scheduling and deadlines  
- **pandas** for generating reports  
- **os** and **json** for file handling and data storage

## Installation

1. Clone the repository:  
   ```bash
   git clone <repository-url>
```
2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main Python script:  
   ```bash
   python main.py
2. Follow the console prompts to add, assign, and manage tasks.
3. Reports and notifications are generated automatically.

## Folder Structure

## Contributing

1. Fork the repository  
2. Create a branch:  
   ```bash
   git checkout -b feature/YourFeature
```
3. Commit your changes:
```bash
git commit -m "Add feature"
```
4. Push and create a pull request

