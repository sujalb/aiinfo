FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["chainlit", "run", "chainlit_app.py", "--host", "0.0.0.0", "--port", "7860"]