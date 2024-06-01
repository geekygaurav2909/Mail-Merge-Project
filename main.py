# Creating a list to have mailing list
mailing_list = []

# Reading files and appending them to mailing list
with open("./Input/Names/invited_names.txt",'r') as name_file:
    for line in name_file:
        mailing_list.append(line.strip())
    
# Creating loop, replacing [name] with recipient and creating mails for them.
for mailer in mailing_list:
    with open(f"./Output/ReadyToSend/mail_to_{mailer}.txt","w+") as create_mail:
        with open("./Input/Letters/starting_letter.txt",'r') as mail_content:
                mail_read = mail_content.read()
                replace_mailer_name = mail_read.replace("[name]", mailer)
        create_mail.write(replace_mailer_name)
