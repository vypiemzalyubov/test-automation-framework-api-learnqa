# Test Automation REST API

Framework for automating API testing from the course ["Automating REST API testing in Python"](https://www.learnqa.ru/python_api) by LearnQA

## :pushpin: Navigation

**[Description](https://github.com/vypiemzalyubov/test-automation-rest-api#rocket-description) | [Prerequisites](https://github.com/vypiemzalyubov/test-automation-rest-api#rocket-prerequisites) | [Project Structure](https://github.com/vypiemzalyubov/test-automation-rest-api#rocket-project-structure)**

## :pushpin: Description:

Automated CRUD (`POST`, `GET`, `PUT`, `DELETE`) APIs using `Python`

## :pushpin: Prerequisites:

[![Static Badge](https://img.shields.io/badge/pytest-gray)](https://pypi.python.org/pypi/pytest)[![pytest](https://img.shields.io/pypi/v/allure-pytest)](https://pypi.python.org/pypi/pytest)
[![Static Badge](https://img.shields.io/badge/requests-gray)](https://pypi.python.org/pypi/requests)[![requests](https://img.shields.io/pypi/v/allure-pytest)](https://pypi.python.org/pypi/requests)
[![Static Badge](https://img.shields.io/badge/allure--pytest-gray)](https://pypi.python.org/pypi/allure-pytest)[![allure--pytest](https://img.shields.io/pypi/v/allure-pytest)](https://pypi.python.org/pypi/allure-pytest)

## :pushpin: Project Structure:

```
test-automation-rest-api/
├─ .github/
│  ├─ workflows/
│  │  ├─ run_tests.yml
├─ lib
│  ├─ __init__.py/
│  ├─ assertions.py
│  ├─ base_case.py
│  ├─ logger.py
│  ├─ my_requests.py
├─ logs 
├─ tests/
│  ├─ __init__.py
│  ├─ test_user_auth.py
│  ├─ test_user_delete.py
│  ├─ test_user_edit.py
│  ├─ test_user_get.py
│  ├─ test_user_register.py
├─ .gitignore
├─ Dockerfile
├─ README.md
├─ docker-compose.yml
├─ environment.py
├─ pytest.ini
├─ requirements.txt
```
