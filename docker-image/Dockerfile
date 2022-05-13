FROM ubuntu:22.04

WORKDIR /replic-app

COPY requirements.txt .

RUN apt update
RUN apt install python3 pip -y

# "bash" as replacement for	"sh"
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN pip3 install virtualenv

RUN virtualenv ./venv

RUN source venv/bin/activate

RUN pip install -r ./requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE 80

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "9000"]
