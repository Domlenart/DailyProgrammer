import logging
logging.basicConfig(filename='saved.log', level=logging.DEBUG)


def get_user_data(log=False):
    prompt = 'What is your {}\n>'
    response_template = 'Your name is {name}, you are {age} years old, and your username is {reddit_username}'

    name = input(prompt.format('name'))
    age = input(prompt.format('age'))
    reddit_login = input(prompt.format('reddit username'))

    response = response_template.format(name=name, age=age, reddit_username=reddit_login)

    if log:
        logging.info(response)

    return response