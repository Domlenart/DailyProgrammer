import os

import praw
import html2text

CHALLENGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'challenges')
CHALLENGE_TYPES = ['easy', 'intermediate', 'hard', 'practical exercise', 'weekly', 'difficult']


def run():
    ensure_folder_structure()
    find_new_challenges()


def ensure_folder_structure():

    if not os.path.exists(CHALLENGES_FOLDER):
        os.mkdir(CHALLENGES_FOLDER)

    for challenge_type in CHALLENGE_TYPES:
        if not os.path.exists(os.path.join(CHALLENGES_FOLDER, challenge_type)):
            os.mkdir(os.path.join(CHALLENGES_FOLDER, challenge_type))


def find_new_challenges():

    for challenge in get_new_posts():
        challenge_type, challenge_num = extract_challenge_difficulty_and_number(challenge)

        if challenge_type and challenge_num:
            if not challenge_exists(challenge_type, challenge_num):
                print('Found new {} challenge #{}'.format(challenge_type, challenge_num))
                make_challenge_file(challenge_type, challenge_num, challenge_text=challenge.selftext_html)


def get_new_posts():
    # Returns all posts from the subreddit. Newest posts first.

    reddit = praw.Reddit(client_id='T37444YSYDJKLQ', client_secret=None, user_agent='dailyprogrammer_scraper /u/Siveq',
                         redirect_uri='http://www.google.com/')

    for post in reddit.subreddit('dailyprogrammer').submissions():
        yield post


def extract_challenge_difficulty_and_number(post):

    challenge_type = [chal_type for chal_type in CHALLENGE_TYPES if chal_type in post.title.lower()]
    challenge_num = [split.strip('#]') for split in post.title.split() if '#' in split]

    if challenge_type and challenge_num:
        challenge_type = challenge_type.pop()
        challenge_num = challenge_num.pop()
    else:
        print('Found undefined challenge with title: {} \n{}\n'.format(post.title, post.url))

    return challenge_type, challenge_num


def challenge_exists(diff, challenge_num):
    return os.path.exists(os.path.join(CHALLENGES_FOLDER, 'Challenge_'+diff, challenge_num, 'description.txt'))


def make_challenge_file(diff, challenge_num, challenge_text):
    textifier = html2text.HTML2Text(bodywidth=55)
    textifier.mark_code = True
    textifier.single_line_break = True
    textifier.wrap_links = True

    wrapped_text = textifier.handle(challenge_text)

    try:
        os.mkdir(os.path.join(CHALLENGES_FOLDER, diff, 'Challenge_'+challenge_num))
    except FileExistsError:
        pass

    filename = 'description.txt'.format(challenge_num)
    file_path = os.path.join(CHALLENGES_FOLDER, diff, 'Challenge_'+challenge_num, filename)

    with open(file_path, 'w+') as f:
        f.writelines(wrapped_text)


if __name__ == '__main__':
    run()
