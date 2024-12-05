FROM python
WORKDIR /AutomationExerciseProject
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /AutomationExerciseProject
CMD ["python", "-m", "pytest", "-s", "/AutomationExerciseProject/tests/api_tests/"]
