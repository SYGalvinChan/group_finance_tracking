FROM public.ecr.aws/amazonlinux/amazonlinux:latest

RUN yum install python3.11 -y

RUN yum install python3.11-pip -y

RUN yum install openssl -y

COPY ./requirements.txt .

COPY ./bot.py .

COPY ./start_bot.sh .

RUN pip3.11 install -r requirements.txt

EXPOSE 443/tcp

ENTRYPOINT ["bash" , "./start_bot.sh"]