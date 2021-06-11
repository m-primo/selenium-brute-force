# Selenium Brute Force
This script will do login brute force in a website using a list of users and passwords.


# Installation
First, you'll need to have:
1. [Python 3](https://www.python.org/downloads/)
2. pip
3. [Google Chrome](https://www.google.com/chrome/)
4. [Chrome Driver](https://chromedriver.chromium.org/downloads)

Once that's all set up:

1. Clone this repository ```git clone https://github.com/m-primo/selenium-brute-force```.
2. Go to the cloned directory ```cd selenium-brute-force```.
3. Install the requirements ```pip install -r xreqs.txt```.


# Run
- Using arguments:
```bash
python app.py -u <URL> -l <LIST> -fu <INPUT_NAME_OF_USER_FIELD> -fp <INPUT_NAME_OF_PASSWORD_FIELD> -fl <INPUT_NAME_OF_LOGIN_BUTTON>
```
to get the help message:
```bash
python app.py -h
```
- Or you can just run the app and it'll ask you with the inputs:
```bash
python app.py
```


# Contributing
1. [Fork this repository](https://github.com/m-primo/selenium-brute-force/fork).
2. Clone your repository.
```bash
git clone [your_repo]
```
3. Make & commit your changes.
```bash
git commit -m "[message]"
```
3. Push it.
```bash
git push
```
4. Create a [new pull request](https://github.com/m-primo/selenium-brute-force/pulls) in this repository.


# Disclaimer
THIS REPOSITORY AND EVERY SCRIPT INCLUDED IN IT IS FOR EDUCATIONAL, TESTING, AND RESEARCH PURPOSES ONLY. THE OWNER NOR ANY CONTRIBUTOR IS NOT RESPONSIBLE FOR YOUR ACTIONS.


# License
[BSD-2-Clause License](LICENSE)