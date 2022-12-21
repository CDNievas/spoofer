from PyInquirer import prompt

menuQuestions = [{
    "type":"input",
    "name":"sender",
    "message":"Sender email (from): "
},{
    "type":"input",
    "name":"receiver",
    "message":"Receiver email (to): "
},{
    "type":"input",
    "name":"subject",
    "message":"Subject: ",
    "default":"Ingreso sospechoso a tu cuenta"
},{
    "type":"input",
    "name":"message",
    "message":"Message: ",
    "default":"This is a test"
}]

menuAgainQuestions = [{
    "type":"confirm",
    "name":"is_again",
    "message":"Send another email?",
    "default":True
}]


def printMenu():
    answers = prompt(menuQuestions)
    return answers.get("sender"), answers.get("receiver"), answers.get("subject"), answers.get("message")

def printMenuAgain():
    answers = prompt(menuAgainQuestions)
    return answers.get("is_again")