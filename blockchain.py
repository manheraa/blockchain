GenisisBlock = {"Previous-hash": "", "Index": 0, "Transactions": []}
blockchain = [GenisisBlock]
openTransaction = []
owner = "Manhera"
"""Here blockchain is an empty list which forms the chain in future"""


def getTheValueOfPreviousBlock():
    """Get the value of previous block"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def getInput():
    """This function takes the input that is transaction amount"""
    txRecipent = input("Enter  the name of recipent:")
    txAmount = float(input("Enter  the transaction amount:"))
    return txRecipent, txAmount


def addTransaction(recipent, amount=1.0, sender=owner):
    """Append a new value as well as last value"""
    Transaction = {"Sender": sender, "Recipent": recipent, "Amount": amount}
    openTransaction.append(Transaction)


def mineBlock():
    lastBlock = blockchain[-1]
    previousHash=""
    for key in lastBlock:
        value=lastBlock[key]
        previousHash=previousHash+str(value)
    transactions = openTransaction
    block = {
        "Previous-hash": previousHash,
        "Index": len(blockchain),
        "Transactions": transactions,
    }
    blockchain.append(block)
    

def verifyChain():

    isValid = True
    for blockIndex in range(len(blockchain)):
        if blockIndex == 0:
            blockIndex += 1
            continue
        elif blockchain[blockIndex][0] == blockchain[blockIndex - 1]:
            isValid = True
        else:
            isValid = False
            break
        blockIndex += 1
    return isValid


def printBlockchainELements():
    for block in blockchain:
        print("Output Block:")
        print(block)
    else:
        print("-" * 20)


waitingForInput = True


while waitingForInput:
    """Choose the value to perform any function"""
    userChoice = input(
        " 1.To add a new block \n 2.TO print the blocks\n 3.Press h to Manupliate the blockchain \n 4.Press 4 to mine a new block \n 5.Press q to exit to exit:"
    )

    if userChoice == "1":
        """This function adds the block to the blockchain"""
        txData = getInput()
        recipent, amount = txData
        addTransaction(recipent, amount=amount, sender=owner)
        print(openTransaction)
    elif userChoice == "2":
        """This is used to print the blocks"""
        printBlockchainELements()
    elif userChoice=="3":
        mineBlock()
        openTransaction=[]
        
    elif userChoice == "h":
        if len(blockchain) >= 2:
            blockchain[0] = [2]
        else:
            print("Not Possible")
    elif userChoice == "q":
        waitingForInput = False

    else:
        print("Invalid Choice")
    #if not verifyChain():
#
    #    print("Invalid chain!")
    #    break
else:
    print("User Left!")
print("Completed")
