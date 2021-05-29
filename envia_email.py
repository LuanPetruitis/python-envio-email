# Atenção é necessário configurar o programa com seus dados.

import smtplib

email_from = "email-que-quer-enviar"
email_to = "email-que-receberá"

smtp = "smtp.gmail.com"

server = smtplib.SMTP(smtp, 587)
server.starttls()
server.login(email_from, "senha-do-email-from")

msg = """
    <h1>Este e um e-mail usando python para poder aprender e usar nos programas
    </h1>

"""

server.sendmail(email_from, email_to, msg)
server.quit()

print("Email enviado com sucesso!")