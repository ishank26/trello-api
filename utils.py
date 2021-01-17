import requests
from trello import TrelloApi
import config

API_KEY = config.API_KEY
USER_TOKEN = config.USER_TOKEN

trello = TrelloApi(API_KEY)
trello.set_token(USER_TOKEN)


def check_board_exists(board_name, board_id = None):
    resp = trello.search.get(query = board_name)

    for item in resp['boards']:
        if item['name'] == board_name:
            return item
    return None

def check_list_exists(list_name, board_name, list_id = None):
    board = check_board_exists(board_name)

    if not board:
        print('Wrong board')
        return None

    resp = trello.boards.get_list(board_id = board['id'])

    for item in resp:
        if item['name'] == list_name:
            return item
    return None


def add_new_board(board_name):
    resp = trello.boards.new(name=board_name)
    return resp


def add_new_card(board_name, card_name, list_name, comment, label):
    # check board exists
    board = check_board_exists(board_name)


    if board:
        board_id = board['id']
    else:
        board_id = add_new_board(board_name)    


    list = check_list_exists(list_name=list_name, board_name=board_name)

    if not list:
        list_id = trello.boards.new_list(board_id= board_id, name= list_name)
    else:
        list_id = list['id']

    # create card
    resp = trello.cards.new(name = card_name, idList = list_id)

    if not resp: return None

    card_id = resp['id']


    trello.cards.new_label(card_id, color = label)
    
    trello.cards.new_action_comment(card_id, text = comment)

    return resp



