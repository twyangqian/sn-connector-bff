FROM python:3.9

RUN mkdir /app

COPY ./ /app

WORKDIR /app

RUN mkdir ~/.pip && \
    cd ~/.pip/  && \
    echo "[global] \ntrusted-host =  mirrors.aliyun.com \nindex-url = http://mirrors.aliyun.com/pypi/simple" >  pip.conf
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "streamlit_app.py", "--server.port", "8000" ]