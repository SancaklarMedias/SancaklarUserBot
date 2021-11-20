# We're Using NaytSeyd's Special Docker
FROM sancaklarmedias/sancaklarbot:j1xlte

# Working Directory
WORKDIR /SancaklarMedias/

# Clone Repo
RUN git clone -b sancaklar https://github.com/SancaklarMedias/sancaklarUsersBot.git /SancaklarMedias/

# Run bot
CMD ["python3", "sancaklar.py"]