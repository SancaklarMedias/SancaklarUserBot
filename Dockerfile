# We're Using NaytSeyd's Special Docker
FROM naytseyd/sedenbot:j1xlte

# Working Directory
WORKDIR /SancaklarMedias/

# Clone Repo
RUN git clone -b sancaklarmedias https://github.com/SancaklarMedias/SancaklarUsersBot.git /SancaklarMedias/

# Run bot
CMD ["python3", "sancaklar.py"]