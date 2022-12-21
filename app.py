import smtplib
from email.message import EmailMessage

from utils.logo import printLogo
from utils.menu import printMenu, printMenuAgain

if __name__ == "__main__":
    printLogo()
    
    is_again = True
    while(is_again):
        sender, receiver, subject, message = printMenu()

        msg = EmailMessage()
        msg.set_content(message)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver
        # msg.add_header("reply-to", "phishy@phising.com")  # The attackers address
        # Send the message via our own SMTP server.
        s = smtplib.SMTP("localhost:2525")
        s.send_message(msg)
        s.quit()

        is_again = printMenuAgain()

