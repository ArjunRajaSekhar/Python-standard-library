import smtplib
server = smtplib.SMTP('127.0.0.1')
server.sendmail('santhoshk728@gmail.com', 'rarjunsekhar@gmai.com',"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
