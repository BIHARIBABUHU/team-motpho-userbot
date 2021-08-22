FROM BIHARI_USERBOT/team-motpho-userbot:latest

#clonning repo 
RUN git clone https://github.com/BIHARIBABUHU/BIHARI_USERBOT.git /root/morphobot

#working directory 
WORKDIR /root/morphobot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","morphobot"]
