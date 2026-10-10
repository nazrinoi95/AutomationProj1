# AutomationProj1 
A simple automation project designed to demonstrate how a proper test automation suite would look like.

## Tech Stack
- Python 3.13
- Selenium 4
- Pytest
- GitHub Actions

## Project Structure

```
AutomationProj1/
├──.github/ # GitHub Actions CI/CD workflows
├── core/ # Internal automation framework — driver, actions
├── pages/ # Page objects for the web application
├── tests/ # Test cases for herokuapp.com
│ └── data/ # CSV test data files
├── utils/ # Helper modules — logger, screenshot, config
├── logs/ # Generated logs (gitignored)
├── reports/ # Generated HTML reports (gitignored)
└── screenshots/ # Captured on test failure (gitignored)
```
## Pre-requisites
- Python 3.13 installed on your machine.
- Google Chrome / Mozilla Firefox browser installed.
- ChromeDriver installed and added to your system PATH.
- Git installed on your machine.

## Setup
```bash

# Clone the repository
git clone https://github.com/nazrinoi95/AutomationProj1.git
cd AutomationProj1

# Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

# Install the required dependencies
pip install -r requirements.txt

#Create .env file in project root
cp .env.example .env

#Fill in your credentials in the .env file
```
# Running Tests
```bash
# Run full test suite (Chrome and Firefox)
pytest tests/ -v

# Run smoke tests only
pytest tests/ -v -m smoke

# Run regression tests only
pytest tests/ -v -m regression

# Run headless tests
pytest tests/ -v --headless

#Generate HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html
```
## CI/CD
Tests run automatically via GitHub Actions on:
- Pull Requests to Master
- Push to Master
- Manual trigger via workflow_dispatch

HTML reports are generated and uploaded as artifacts for each run.


