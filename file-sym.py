import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main_menu():
    print("=====================================")
    print("|    Bienvenido a la herramienta de  |")
    print("|            phishing               |")
    print("|         Autor: Tekilla            |")
    print("=====================================")
    print("Por favor, selecciona una opción:")
    print("1. Phishing de Gmail")
    print("2. Phishing de Outlook")
    print("3. Otros servicios de correo")
    print("4. Salir")

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

main_menu()
