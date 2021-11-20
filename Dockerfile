FROM naytseyd/sedenbot:j1xlte

# Working Directory
WORKDIR /DerUntergang/

# Run bot
CMD ["python3", "sancaklar.py"]