# We're Using NaytSeyd's Special Docker
FROM sancaklarmedias/sancaklar:j1xlte

# Working Directory
WORKDIR /DerUntergang/

# Clone Repo
RUN git clone -b sancaklar https://github.com/SancaklarMedias/SancaklarUsersBot /DerUntergang/

# Run bot
CMD ["python3", "sancaklar.py"]