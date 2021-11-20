# We're Using NaytSeyd's Special Docker
FROM naytseyd/Sancaklarbot:j1xlte

# Working Directory
WORKDIR /DerUntergang/

# Clone Repo
RUN git clone -b Sancaklar https://github.com/TeamDerUntergang/Telegram-SancaklarUserBot.git /DerUntergang/

# Run bot
CMD ["python3", "Sancaklar.py"]