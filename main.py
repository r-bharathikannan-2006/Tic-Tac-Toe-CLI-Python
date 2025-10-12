import requests
import time

def last_move_det(dictionary):
    return dictionary['last_move']

def display(data):
        print("-------------")
        for row in data:
            print(f"| {row[0]} | {row[1]} | {row[2]} |")
            print("-------------")

def get_request(url):
    """Returns dictionary"""
    try:
        response = requests.get(url)
        return response.json()['record']
    except:
        print("Error in getting the response...")
    return None


def put_request(url, data, master_key=None, access_key=None):
    """Returns status code"""

    if master_key == None and access_key != None:
        headers = {
            'Content-Type': 'application/json',
            'X-Access-Key': access_key
        }
    elif master_key != None and access_key == None:
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': master_key
        }
    req = requests.put(url, json=data, headers=headers)
    return req.status_code

def check_winner(board_data):
    # Check rows and columns
    for i in range(3):
        if board_data[i][0] == board_data[i][1] == board_data[i][2] and board_data[i][0] != " ":
            return board_data[i][0]
        if board_data[0][i] == board_data[1][i] == board_data[2][i] and board_data[0][i] != " ":
            return board_data[0][i]

    # Check diagonals
    if board_data[0][0] == board_data[1][1] == board_data[2][2] and board_data[0][0] != " ":
        return board_data[0][0]
    if board_data[0][2] == board_data[1][1] == board_data[2][0] and board_data[0][2] != " ":
        return board_data[0][2]

    # Check for a tie
    if all(cell != " " for row in board_data for cell in row):
        return "Tie"

    # No winner yet
    return None

def host_server(servers):
    isError = False
    for server in servers:
        try:
            response = requests.get(server['url'])
            if response.json()['record'].get('host_joined') != None:
                return servers.index(server), server
            else: 
                continue
        except:
            print(f"Error in getting the response from server {server.index(server)}")
    return None,None
            
    

def join_server(number, servers):
    return servers[number]

def exit_game(url, x_Master_Key):
    print("Exiting the game...")
    print("Wait for 10 seconds before stopping the program...")
    time.sleep(10)
    dictionary = {
        "host_joined": False,
        "guest_joined": False,
        "last_move": [None, None],
    }
    code = put_request(url, dictionary, master_key=x_Master_Key)
    if code == 200:
        print("Successfully stopped the program")
    else:
        print("Error in stopping the program")
    exit()

x_Master_Key = '$2a$10$I7Kbd4g31GwjrzCZBc8xuut3AxLjVYfmWH1q.6/lfzKZCQdlXGkjW'
x_Access_Key = "$2a$10$q6QUNwuyvptYhYrv8PnDxOBp9mpzKU5mxVJCwoQ93VoQAj.5eMUx6",
# Main Code
servers = [
    {
        "url": "https://api.jsonbin.io/v3/b/67dad0858960c979a574bdb3",
    },
    {
        "url": "https://api.jsonbin.io/v3/b/68ea900ad0ea881f409deb1d",
    },
    {
        "url": "https://api.jsonbin.io/v3/b/68ea9019ae596e708f0eb288",
    },
    {
        "url": "https://api.jsonbin.io/v3/b/68ea90a7ae596e708f0eb3b6",
    },
    {
        "url": "https://api.jsonbin.io/v3/b/68ea90b9d0ea881f409dec66",
    },
]

data = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
chances = [[0, 0], [0, 1], [0, 2], [1, 0],
           [1, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
winner = None

print("Welcome to Tic Tac Toe")

while (True):
    temp = input("Host or Join (h or j) : ")
    if temp == 'h' or temp == 'H':
        ishost = True
        last_move = [None, None]
        number, server = host_server(servers)
        if number == None and server == None:
            print("All servers are currently occupied...")
            exit()
        else:
            url = server['url']
            dictionary = {
                "guest_joined": False,
                "last_move": ["*", "*"]
            }
            code = put_request(url, dictionary, master_key=x_Master_Key)
            if code == 200:
                print(f"Successfully hosted the server at index {number}")
                print("Share this number with your friend to join the server")
            else:
                print("Error in hosting the server...")
                exit()
        break

    elif temp == 'j' or temp == 'J':
        while True:
            serv_numb = int(input("Enter the number of server to join (0-4) : "))
            if serv_numb < 0 or serv_numb > 4:
                print("Invalid server number...")
                continue
            else:
                temp_url = servers[serv_numb]['url']
                response = requests.get(temp_url)
                if response.json()['record'].get("guest_joined") == None:
                    print("The server is already occupied...")
                    continue
                else:
                    server = join_server(serv_numb, servers)
                    if server == -1:
                        print("Error in joining the server...")
                    else:
                        url = server['url']
                        dictionary = {
                            "last_move": ["*", "*"],
                        }
                        code = put_request(url, dictionary, master_key=x_Master_Key)
                        if code == 200:
                            print("Successfully joined the server")
                            ishost = False
                            last_move = [None, None]
                            break
                        else:
                            print("Error in joining the server...")
                            exit()
        break
    else:
        print("Invalid Input...")
        continue
            


# Game Logic
if ishost:
    print("Make the first Move...")
    display(data)
    while True:
        status = True
        while status:
            print("Now your chance...")
            print("Enter row- 'q' and column- 'q' to quit")
            try:
                x = int(input("Enter the Row (0-2): "))
                y = int(input("Enter the Column (0-2): "))
            except:
                exit_game(url, x_Master_Key=x_Master_Key)
            
            if [x, y] in chances:
                data[x][y] = "X"
                chances.pop(chances.index([x, y]))
                last_move = [x, y]
                status = False
                dictionary = {
                    "last_move": last_move,
                }
                print(put_request(url, dictionary, master_key=x_Master_Key))
                time.sleep(2)
                display(data)
                break
        winner = check_winner(data)
        if winner != None:
            break
        time.sleep(5)
        while True:
            temp = last_move_det(get_request(url))
            if temp != last_move:
                last_move = temp
                x, y = last_move
                data[x][y] = "O"
                chances.pop(chances.index([x, y]))
                display(data)
                break
            print("Waiting for guest to enter...")
            time.sleep(5)
        winner = check_winner(data)
        if winner != None:
            break
    print(f"The winner is {winner}")
else:
    print("Waiting for host...")
    while True:
        time.sleep(5)
        while True:
            temp = last_move_det(get_request(url))
            if temp != last_move and temp != ["*", "*"] and temp != [None, None]:
                last_move = temp
                x, y = last_move
                data[x][y] = "X"
                chances.pop(chances.index([x, y]))
                display(data)
                break
            print("Waiting for host to enter...")
            time.sleep(5)
        winner = check_winner(data)
        if winner != None:
            break
        status = True
        while status:
            print("Now your chance...")
            print("Enter row- 'q' and column- 'q' to quit")
            try:
                x = int(input("Enter the Row (0-2): "))
                y = int(input("Enter the Column (0-2): "))
            except:
                exit_game(url, x_Master_Key=x_Master_Key)
            if [x, y] in chances:
                data[x][y] = "O"
                chances.pop(chances.index([x, y]))
                last_move = [x, y]
                status = False
                dictionary = {
                    "last_move": last_move,
                }
                print(put_request(url, dictionary, master_key=x_Master_Key))
                time.sleep(2)
                display(data)
                break
        winner = check_winner(data)
        if winner != None:
            break
    print(f"The winner is {winner}")

dictionary = {
    "last_move": last_move,
}
code = put_request(url, dictionary, master_key=x_Master_Key)


