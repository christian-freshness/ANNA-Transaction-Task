# ANNA-Transaction-Task
# Transaction Quality Checker

This repository contains a Python project to perform quality checks on a dataset of categorized transactions. The main functionality includes generating a classification report using the `sklearn` library and ensuring the code adheres to linting standards via `pre-commit`.

## Table of Contents
1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Running the Quality Check Script](#running-the-quality-check-script)
4. [Linting with Pre-commit](#linting-with-pre-commit)
5. [Directory Structure](#directory-structure)
6. [Contributing](#contributing)
7. [Contact](#contact)

---

## Requirements

To run this project, ensure you have the following installed:
- Python 3.12
- Git
- Conda (optional but recommended)
- `pre-commit` for linting

Python dependencies are specified in the `requirements.txt` file.

---

## Setup

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/christian-freshness/ANNA-Transaction-Task.git
cd ANNA-Transaction-Task
```
### 2. Set Up Python Environment
#### Using Conda (Recommended):
Create a new Conda environment with Python 3.12:
``` bash
conda create -n py3_12 python=3.12
conda activate py3_12
```
#### Using Virtualenv:
Create and activate a virtual environment:
``` bash
python3.12 -m venv env
source env/bin/activate  # On macOS/Linux
.\env\Scripts\activate   # On Windows
```
### 3. Install Dependencies
Install all required packages:
``` bash
pip install -r requirements.txt
```
---

## Running the Quality Check Script
The quality check script generates a classification report (report.txt) by comparing the true category column with the predicted_category column in the dataset.

### Usage
To run the script, execute the following command:
``` bash
python quality_check.py --input <path_to_dataset.csv>
```
Example:
``` bash
python quality_check.py --input data/transactions.csv
```
### Output
The script saves the classification report to the output directory as report.txt. Ensure this directory exists, or create it before running the script.

---

## Linting with Pre-commit
This project uses pre-commit to enforce coding standards with Flake8 and Isort.

### 1. Install Pre-commit
Install pre-commit in your environment:
```bash
pip install pre-commit
```
### 2. Install Hooks
Set up pre-commit hooks:
```bash
pre-commit install
```

### 3. Run Pre-commit Manually
You can manually check all files for issues by running:
``` bash
pre-commit run --all-files
```
### GitHub Actions Integration
The repository includes a GitHub Action `(linter.yml)` to automatically run linting checks on pull requests. Any issues will be flagged, ensuring code quality.

---

## Directory Structure
``` plaintext
.
├── .github/
    └── workflows/
        └── linter.yml        # GitHub Action for linting
├── data/
│   └── datasets_part1.csv    # dataset
├── reports/
│   └── report.txt            # Output classification report
├── scripts/
│   └──quality_check.py       # Main script for generating classification report
├── requirements.txt          # Python dependencies
├── .pre-commit-config.yaml   # Pre-commit configuration
├── setup.cfg                 # Linter configuration (Flake8/Isort)
├── README.md                 # Project documentation
```
---

## Contributing
Contributions are welcome! Follow these steps to contribute:

Fork the repository.
Create a new branch:
``` bash
git checkout -b feature-branch
```
Commit your changes:
``` bash
git commit -m "Add your message here"
```
Push to your branch:
``` bash
git push origin feature-branch
```
Open a pull request.

---

## Contact
If you have any questions or issues, feel free to open an issue on GitHub or contact the maintainer.
