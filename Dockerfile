# FROM kısmını Değiştirmeyiniz sancaklarye DockerFile Kullanın

FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/SancaklarMedias/SancaklarUsersBot /root/SancaklarUsersBot
WORKDIR /root/SancaklarUsersBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
