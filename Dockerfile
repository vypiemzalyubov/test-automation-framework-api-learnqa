FROM python

LABEL "project" = "test-automation-rest-api"

WORKDIR /test-automation-rest-api

VOLUME /allure-results

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python -m pytest -s -v tests/* --alluredir=allure-results/