# frontend/Dockerfile

FROM python:3.9

WORKDIR /.

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.fileWatcherType=none"]
