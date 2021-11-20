# We're Using NaytSeyd's Special Docker
FROM naytseyd/sedenbot:j1xlte

# Working Directory
WORKDIR /SancaklarMedias/

# Clone Repo

# Run bot
CMD ["python3", "sancaklar.py"]