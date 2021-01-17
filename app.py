
import argparse
import utils
import argparse

parser = argparse.ArgumentParser(description='Add card to Trello Board')


parser.add_argument('--board_name',required=True, help='Board name for the card')
parser.add_argument('--list_name', required=True, help='List name for the card')
parser.add_argument('--card_name', required=True, help= 'Title of the card')

parser.add_argument(
    '--comment',
    default=None,
    help='Provide a comment'
)

parser.add_argument(
	'--label',
	default = None ,
	help ='Provide a label ')



if __name__ == '__main__':		
    

    args = parser.parse_args()

  
    board_name = args.board_name
    card_name = args.card_name
    list_name = args.list_name

    comment = args.comment

    label = args.label

    resp = utils.add_new_card(board_name= board_name, card_name= card_name, list_name= list_name ,comment= comment, label=label)

    print(resp)
    