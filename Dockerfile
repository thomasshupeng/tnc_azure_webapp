FROM ubuntu:16.04
MAINTAINER Shu Peng <thomasshupeng@hotmail.com>

WORKDIR /code
ADD ./doc_img_requirements.txt /code
ADD ./run_waitress_server.py /code
ADD ./tncapp.py /code
ADD ./TNC_ModelLoader.py /code
ADD models /code/models


RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        openmpi-bin \
        python3 \
        python3-dev \
        python3-setuptools \
        python3-pip
RUN pip3 install --upgrade pip
#RUN pip install https://cntk.ai/PythonWheel/CPU-Only/cntk-2.5.1-cp36-cp35-cp35m-linux_x86_64.whl && \
#    pip install -r ./code/doc_img_requirements.txt
RUN pip3 install cntk
RUN pip3 install -r ./doc_img_requirements.txt

EXPOSE 8080
ENV SERVER_PORT 8080

CMD ["python3", "run_waitress_server.py"]


