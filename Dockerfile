FROM python
WORKDIR /test-automation-rest-api/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=allure_results/ /test-automation-rest-api/tests/*