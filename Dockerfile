FROM python:3.9

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app
COPY --chown=user ./requirements.txt $HOME/app/requirements.txt

RUN pip install --user --upgrade pip setuptools wheel
RUN pip install --user --no-cache-dir -r requirements.txt

COPY --chown=user . .

CMD ["chainlit", "run", "chainlit_app.py", "--host", "0.0.0.0", "--port", "7860"]