import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main_menu():
    print(Colors.HEADER + "=====================================")
    print("|   Bienvenido a la herramienta de   |")
    print("|             phishing              |")
    print("|            Autor: Tekilla          |")
    print("=====================================" + Colors.END)
    print("Por favor, selecciona una opción:")
    print("1. " + Colors.BLUE + "Phishing de Gmail" + Colors.END)
    print("2. " + Colors.BLUE + "Phishing de Outlook" + Colors.END)
    print("3. " + Colors.BLUE + "Otros servicios de correo" + Colors.END)
    print("4. " + Colors.FAIL + "Salir" + Colors.END)

    option = input("Ingrese el número de opción: ")

    if option == "1":
        phishing_gmail()
    elif option == "2":
        phishing_outlook()
    elif option == "3":
        phishing_otro_correo()
    elif option == "4":
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        main_menu()

def phishing_gmail():
    print("¡Phishing de Gmail seleccionado!")
    sender_email = input("Ingresa tu dirección de correo electrónico: ")
    sender_password = input("Ingresa tu contraseña: ")
    target_email = input("Ingresa la dirección de correo electrónico del objetivo: ")
    subject = input("Ingresa el asunto del correo: ")
    body = input("Ingresa el cuerpo del correo: ")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        server.close()
        print("Correo enviado con éxito.")
    except:
        print("Error al enviar el correo. Verifica tus credenciales y asegúrate de tener acceso al servidor SMTP de Gmail.")

def phishing_outlook():
    print("¡Phishing de Outlook seleccionado!")
    sender_email = input("Ingresa tu dirección de correo electrónico: ")
    sender_password = input("Ingresa tu contraseña: ")
    target_email = input("Ingresa la dirección de correo electrónico del objetivo: ")
    subject = input("Ingresa el asunto del correo: ")
    body = input("Ingresa el cuerpo del correo: ")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        server.close()
        print("Correo enviado con éxito.")
    except:
        print("Error al enviar el correo. Verifica tus credenciales y asegúrate de tener acceso al servidor SMTP de Outlook.")

def phishing_otro_correo():
    print("¡Phishing de otros servicios de correo seleccionado!")
    sender_email = input("Ingresa tu dirección de correo electrónico: ")
    sender_password = input("Ingresa tu contraseña: ")
    target_email = input("Ingresa la dirección de correo electrónico del objetivo: ")
    subject = input("Ingresa el asunto del correo: ")
    body = input("Ingresa el cuerpo del correo: ")
    smtp_server = input("Ingresa el servidor SMTP: ")
    smtp_port = input("Ingresa el puerto SMTP: ")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        server.close()
        print("Correo enviado con éxito.")
    except:
        print("Error al enviar el correo. Verifica tus credenciales y asegúrate de tener acceso al servidor SMTP especificado.")

main_menu()
