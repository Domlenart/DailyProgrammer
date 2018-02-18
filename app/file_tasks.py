import os
from collections import namedtuple

TASK_FOLDER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'challenges')
CHALLENGE_TYPE_FOLDERS = [folder for folder in os.listdir(TASK_FOLDER_PATH) if 'init' not in folder]


def get_challenge_status():
    challenge = namedtuple('challenge', 'id difficulty completed tested text')

    for challenge_type in CHALLENGE_TYPE_FOLDERS:
        challenge_type_dir = os.path.join(TASK_FOLDER_PATH, challenge_type)
        challenge_folders = [folder for folder in os.listdir(challenge_type_dir) if 'init' not in folder]
        for challenge_folder in challenge_folders:
            try:
                cid = int(challenge_folder.split('_')[-1])
            except ValueError:
                pass
            else:
                completed = False
                tested = False

                with open(os.path.join(challenge_type_dir, challenge_folder, 'description.txt')) as f:
                    text = f.read()

                #Strip special chars
                text = ''.join([letter for letter in text if ord(letter) < 65536])

                if 'solution.py' in os.listdir(os.path.join(challenge_type_dir, challenge_folder)):
                    completed = True
                if 'test' in '\t'.join(os.listdir(os.path.join(challenge_type_dir, challenge_folder))):
                    tested = True

                yield challenge(cid, challenge_type, completed, tested, text)
