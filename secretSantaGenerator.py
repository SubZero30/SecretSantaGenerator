import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import shuffle, randint
smtpPort, smtpsrv = 587, "smtp.gmail.com"
username = 'email@gmail.com'
password = 'type your password here'

InputMappingList = [{"name":"recepient1","email":"email1"},
				{"name":"recepient2","email":"email2"},
				{"name":"recepient3","email":"email3"}]
AddressDict = {"recepient1":"address1",
				"recepient2":"address2",
				"recepient3":"address3"}

def assign_santa(InputMappingList : list) -> list:
    shuffle(InputMappingList)
    start = 0
    n = len(InputMappingList)
    while start < n - 1:
        cut = randint(start + 2, n - 1) if start + 2 < n - 1 else n
        if cut == n - 1: cut = n
        for i in range(start, cut):
            InputMappingList[i]['assigned'] = InputMappingList[(i + 1) % cut]['name']
        start = cut
    not_true = True
    while not_true:
        master_dict = {}
        not_true = False
        for i in range(n):
            if InputMappingList[i]['assigned'] not in master_dict.keys():
                master_dict[InputMappingList[i]['assigned']] = 1
            else:
                not_true = True
                assign_santa(InputMappingList)
                break
    return InputMappingList

def sendMail():
	smtpserver = smtplib.SMTP(smtpsrv, smtpPort)
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(username, password)
	for i in InputMappingList:
		msg = MIMEMultipart()
		msg['From'] = username
		msg['To'] = i['email']
		sentTo = i['name']
		msg['Subject'] = "Secret Santa Bot - Lots Have Been Drawn"
		message = """Hiiiiieeee """ + sentTo + """

		I am a Secret Santa Bot and I have drawn the lots.
		For this Christmas/NYE, you will be the Secret Santa for """ + i['assigned'] + """.

		Their address is : """+AddressDict[i['assigned']]+"""

		Have a Merry Christmas! 

		Not yours,
		Secret Santa Generator Bot

		Find source code for this and other such useless stuff at https://github.com/SubZero30
		"""
		msg.attach(MIMEText(message, 'plain'))
		smtpserver.sendmail(msg['From'], msg['To'], msg.as_string())
	smtpserver.close()
	return ()

assign_santa(InputMappingList)
sendMail()