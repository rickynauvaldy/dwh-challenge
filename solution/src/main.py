# DWH Coding Challenge

import pandas as pd

import json

from os import walk

import numpy as np



# Configure paths

data_path = 'data/'

accounts_folder = 'accounts/'

cards_folder = 'cards/'

savings_accounts_folder = 'savings_accounts/'



# Some panda options

pd.options.mode.chained_assignment = None  # default='warn

pd.options.display.max_rows = 999

pd.options.display.max_columns = 999



# functions

def file_json_to_df(filenames, path):

    result = []

    for filename in filenames:

        full_path = path + filename

        

        # set encoding for unhandled char

        with open(full_path, 'r', encoding='utf-8') as f:

            data = json.load(f)

            result.append(data)

    result = pd.json_normalize(result)

    return result



def task():



    # Create a folder path

    accounts_path = data_path + accounts_folder

    cards_path = data_path + cards_folder

    savings_accounts_path = data_path + savings_accounts_folder



    # Assign filenames to iterate

    _,_, accounts_filenames = next(walk(accounts_path))

    _,_, cards_filenames = next(walk(cards_path))

    _,_, savings_accounts_filenames = next(walk(savings_accounts_path))

    

    # Compile JSON to DataFrame

    accounts = file_json_to_df(accounts_filenames, accounts_path)

    cards = file_json_to_df(cards_filenames, cards_path)

    savings_accounts = file_json_to_df(savings_accounts_filenames, savings_accounts_path)

    

    # Task 1. Visualize the complete historical table view of each tables in tabular format in stdout

    # Cleanse accounts

    accounts.sort_values(by='ts', inplace=True)

    new_accounts = pd.DataFrame(columns=accounts.columns)

    for account in accounts['id'].unique():

        account_data_by_id = accounts[accounts['id'] == account].reset_index().drop(columns='index')

        data = {}

        for i in range(0, len(account_data_by_id)):

            if account_data_by_id['op'][i] == 'c':

                data['account_id'] = account_data_by_id['data.account_id'][i]

                data['name'] = account_data_by_id['data.name'][i]

                data['address'] = account_data_by_id['data.address'][i]

                data['phone_number'] = account_data_by_id['data.phone_number'][i]

                data['email'] = account_data_by_id['data.email'][i]

                

            elif account_data_by_id['op'][i] == 'u':

                if ~pd.isna(account_data_by_id['set.phone_number'])[i]:

                    data['phone_number'] = account_data_by_id['set.phone_number'][i]

                    

                if ~pd.isna(account_data_by_id['set.address'])[i]:

                    data['address'] = account_data_by_id['set.address'][i]

                    

                if ~pd.isna(account_data_by_id['set.email'])[i]:

                    data['email']= account_data_by_id['set.email'][i]

                    

                account_data_by_id['data.account_id'][i] = data['account_id']

                account_data_by_id['data.name'][i] = data['name']

                account_data_by_id['data.address'][i] = data['address']

                account_data_by_id['data.phone_number'][i] = data['phone_number']

                account_data_by_id['data.email'][i] = data['email']

                

        new_accounts = pd.concat([new_accounts, account_data_by_id])

    

    # Cleanse cards

    cards.sort_values(by='ts', inplace=True)

    new_cards = pd.DataFrame(columns=cards.columns)

    for card in cards['id'].unique():

        card_data_by_id = cards[cards['id'] == card].reset_index().drop(columns='index')

        data = {}

        for i in range(0, len(card_data_by_id)):

            if card_data_by_id['op'][i] == 'c':

                data['card_id'] = card_data_by_id['data.card_id'][i]

                data['card_number'] = card_data_by_id['data.card_number'][i]

                data['credit_used'] = card_data_by_id['data.credit_used'][i]

                data['monthly_limit'] = card_data_by_id['data.monthly_limit'][i]

                data['status'] = card_data_by_id['data.status'][i]

                

            elif card_data_by_id['op'][i] == 'u':

                if ~pd.isna(card_data_by_id['set.status'])[i]:

                    data['status'] = card_data_by_id['set.status'][i]

                    

                if ~pd.isna(card_data_by_id['set.credit_used'])[i]:

                    data['credit_used'] = card_data_by_id['set.credit_used'][i]

                    

                card_data_by_id['data.card_id'][i] = data['card_id']

                card_data_by_id['data.card_number'][i] = data['card_number']

                card_data_by_id['data.credit_used'][i] = data['credit_used']

                card_data_by_id['data.monthly_limit'][i] = data['monthly_limit']

                card_data_by_id['data.status'][i] = data['status']

                

            

        new_cards = pd.concat([new_cards, card_data_by_id])

                    

    # Cleanse Savings Accounts

    savings_accounts.sort_values(by='ts', inplace=True)

    new_savings_accounts = pd.DataFrame(columns=savings_accounts.columns)

    for savings_account in savings_accounts['id'].unique():

        savings_account_data_by_id = savings_accounts[savings_accounts['id'] == savings_account].reset_index().drop(columns='index')

        data = {}

        for i in range(0, len(savings_account_data_by_id)):

            if savings_account_data_by_id['op'][i] == 'c':

                data['savings_account_id'] = savings_account_data_by_id['data.savings_account_id'][i]

                data['balance'] = savings_account_data_by_id['data.balance'][i]

                data['interest_rate_percent'] = savings_account_data_by_id['data.interest_rate_percent'][i]

                data['status'] = savings_account_data_by_id['data.status'][i]

                

            elif savings_account_data_by_id['op'][i] == 'u':

                if ~pd.isna(savings_account_data_by_id['set.balance'])[i]:

                    data['balance'] = savings_account_data_by_id['set.balance'][i]

                    

                if ~pd.isna(savings_account_data_by_id['set.interest_rate_percent'])[i]:

                    data['interest_rate_percent'] = savings_account_data_by_id['set.interest_rate_percent'][i]

                    

                savings_account_data_by_id['data.savings_account_id'][i] = data['savings_account_id']

                savings_account_data_by_id['data.balance'][i] = data['balance']

                savings_account_data_by_id['data.interest_rate_percent'][i] = data['interest_rate_percent']

                savings_account_data_by_id['data.status'][i] = data['status']

                

            

        new_savings_accounts = pd.concat([new_savings_accounts, savings_account_data_by_id])

                    

    print("=== Task 1 Visualize Complete Historical Each Table ===")

    print("=== Accounts ===")

    print(new_accounts)

    print("=== Cards ===")

    print(new_cards)

    print("=== Savings_Account ===")

    print(new_savings_accounts)

    print("==================================================")

                    

    

    

    # Task 2. Visualize the complete historical table view of the denormalized joined table in stdout by joining these three tables

    accounts_cards = pd.merge(new_accounts, new_cards, left_on='set.card_id', right_on='data.card_id', suffixes=('', '_cards'), how='left')

    denom_data = pd.merge(accounts_cards, new_savings_accounts, left_on='set.savings_account_id', right_on='data.savings_account_id', suffixes=('_accounts', '_savings_account'), how='left')

    print("=== Task 2 Visualize Complete Historical Table ===")

    print(denom_data)

    print("==================================================")



    # Task 3. From result from point no 2, discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction?

    observed_columns = ['id_accounts', 'id_cards', 'ts_cards', 

                        'set.credit_used', 'id_savings_account', 

                        'ts_savings_account', 'set.balance']



    transactions = denom_data[(~pd.isnull(denom_data['set.credit_used'])) | (~pd.isnull(denom_data['set.balance']))][observed_columns]



    clean_transactions = transactions.copy()

    clean_transactions['time_occured'] = np.where(~pd.isnull(clean_transactions['ts_cards']), clean_transactions['ts_cards'], clean_transactions['ts_savings_account'])

    clean_transactions['value'] = np.where(~pd.isnull(clean_transactions['set.credit_used']), clean_transactions['set.credit_used'], clean_transactions['set.balance'])

    clean_transactions = clean_transactions.sort_values(by='time_occured').reset_index(drop=True)

    clean_transactions.drop(columns = ['ts_cards', 'set.credit_used', 'ts_savings_account', 'set.balance'])

    

    print("=== Task 3 Transactions Made ===")

    print('Based on the results, there are %s transactions' % len(clean_transactions))

    print('With time occured and values as shown in the table below:')

    print(clean_transactions)

    print("==================================================")



if __name__ == '__main__':

    task()