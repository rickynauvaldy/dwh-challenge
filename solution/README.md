# DWH Coding Challenge Solution

## Description
This code compile sample JSON files of event logs with 'create' and 'update' operation where 'update' operation doesn't keep all the column values. Based on the data available, this code will achieve:

1. Visualize the complete historical table view of each tables in tabular format
2. Visualize the complete historical table view of the denormalized joined table in stdout by joining the three tables 
3. Discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction

## Prerequisites
This project is available to run as a standalone `Python` application or by running it as `Docker`. 
- If run as a `Python` application, list of requirements are available in the `requirements.txt` and can be installed by running `pip install -r requirements.txt`
- If run as `Docker`, make sure that `Docker` has already been installed.

## Flow

## Running the Program
- Make sure that all the prerequisites are satisfied
- If run as a `Python` application, execute the following script inside the `solution` folder:
```
$ python src/main.py
```
(or `python3` if it's needed)
- If run as `Docker`, there are three steps:
1. Build it first by running this command:

```
sudo bash build.sh
```

(or without sudo if you have adequate privilege)

2. Run the `run.sh` script by executing this command:

```
sudo bash run.sh
```

## Output
Output of this file is shown on the terminal where you run the program whether as `Python` application or in `Docker`, with answers as follows:
1. Task 1
<br>
<br>Accounts
<br>![Alt text](img/T1_accounts.png?raw=true, "Title")
<br>
<br>Cards
<br>![Alt text](img/T1_cards.png?raw=true, "Title")
<br>
<br>Savings Accounts
<br>![Alt text](img/T1_savings.png?raw=true, "Title")

2. Task 2
<br> As the table is tabular formed printed, it needs a long window to adequate

3. Task 3
<br>
<br>![Alt text](img/T3.png?raw=true, "Title")

## Contact
For further information, you might want to reach me to ricky.nauvaldy@gmail.com. This code is available on Github https://github.com/rickynauvaldy/dwh-challenge