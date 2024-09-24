FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a non-root user
RUN useradd -m chainlit_user

# Change ownership of the /app directory
RUN chown -R chainlit_user:chainlit_user /app

# Switch to the non-root user
USER chainlit_user

CMD ["chainlit", "run", "chainlit_app.py", "--host", "0.0.0.0", "--port", "7860"]