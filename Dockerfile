# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "quickstart.py"]

