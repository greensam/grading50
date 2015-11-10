# Grader7 Automation for CS50 Finance Grading

This Python script automates many of the repetitive tasks required while grading a running CS50 finance implementation. Its dependencies are listed in requirements. It's written for python 2.7. Using a virtualenv is recommended. It requires _Firefox_.

## Setup

Clone this repo. Make a directory for grading, cd into it, and activate a virtualenv as below. 

```
git clone git@github.com:greensam/grading50.git
mkdir grading7
cd grading7
virtualenv venv
source venv/bin/activate
pip install selenium-2.48.0
```

You may need to use sudo with the last step.

After that, you should be ready to start. The script assumes that you will have access to the CS50 Finance instance at the URL listed in early in the script. 

Start with
```
python grader7.py
```

For each student graded, you will find a .json file containing the axes. 










