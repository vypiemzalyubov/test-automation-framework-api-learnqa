# Test Automation REST API

[![Python](https://img.shields.io/badge/python-3.11.2%2B-blue)](https://www.python.org/downloads/release/python-3112/)
[![Build](https://github.com/franneck94/Python-Project-Template/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/vypiemzalyubov/test-automation-rest-api/actions)

Framework for automating API testing from the course ["Automating REST API testing in Python"](https://www.learnqa.ru/python_api) by LearnQA

## :pushpin: Navigation

**[Description](https://github.com/vypiemzalyubov/test-automation-rest-api#rocket-description) | [Prerequisites](https://github.com/vypiemzalyubov/test-automation-rest-api#rocket-prerequisites) | [Project Structure](https://github.com/vypiemzalyubov/test-automation-rest-api#rocket-project-structure)**

## :pushpin: Description:

Automated CRUD (`POST`, `GET`, `PUT`, `DELETE`) APIs using `Python` and `Pytest`

## :pushpin: Prerequisites:

[![Pytest](https://img.shields.io/badge/pytest-7.4.2-blue)](https://pypi.python.org/pypi/pytest)
[![Requests](https://img.shields.io/badge/requests-2.31.0-blue)](https://pypi.python.org/pypi/requests)
[![Allure Pytest](https://img.shields.io/badge/allure--pytest-2.13.2-blue)](https://pypi.python.org/pypi/allure-pytest)

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
