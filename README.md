
# Tic Tac Toe

A classic multiplayer Tic-Tac-Toe game that you can play with a friend over the internet, right from your command-line interface! This project uses the `jsonbin.io` API as a simple, real-time backend to synchronize the game state between two players.

## Features

-   **Real-time Multiplayer:** Play against a friend from anywhere in the world.
    
-   **Host/Join System:** Easily start a game as a host or join a friend's game using a simple server number.
    
-   **CLI-Based:** A lightweight, no-frills interface that runs in any terminal.
    
-   **Dynamic Game Board:** The board is printed and updated in the console after every move.
    
-   **Win & Tie Detection:** The game automatically detects and announces a win, loss, or tie.
    

## How It Works

The game leverages the [jsonbin.io](https://jsonbin.io/ "null") service to act as a shared state manager. When a player makes a move, the script sends a `PUT` request to a specific JSON bin, updating it with the coordinates of the last move. The opponent's script continuously polls this bin with `GET` requests. Once a new move is detected, it updates its local game board and allows the player to take their turn. This simple yet effective mechanism allows for real-time gameplay between two separate terminals.

## Prerequisites

-   Python 3.6+
    
-   The `requests` library
    

## Setup & Installation

1.  **Clone the repository:**
    
    ```
    git clone [https://github.com/r-bharathikannan-2006/Tic-Tac-Toe-CLI-Python.git](https://github.com/r-bharathikannan-2006/Tic-Tac-Toe-CLI-Python.git)
    cd Tic-Tac-Toe-CLI-Python
    
    ```
    
2.  **Install the required package:**
    
    ```
    pip install requests
    
    ```
    

## How to Play

The game requires two players to run the script on their respective computers.

#### Player 1 (The Host)

1.  Run the script from your terminal:
    
    ```
    python main.py
    
    ```
    
2.  When prompted `Host or Join (h or j) :`, type `h` and press **Enter**.
    
3.  The game will connect to an available server and display a message like:
    
    ```
    Successfully hosted the server at index 2
    Share this number with your friend to join the server
    
    ```
    
4.  Share the **server number** (e.g., `2`) with Player 2.
    
5.  As the host, you play as 'X' and get to make the first move.
    

#### Player 2 (The Guest)

1.  Run the script from your terminal:
    
    ```
    python main.py
    
    ```
    
2.  When prompted `Host or Join (h or j) :`, type `j` and press **Enter**.
    
3.  When prompted `Enter the number of server to join (0-4) :`, enter the server number you received from the host.
    
4.  Once connected, wait for the host to make their move. You will play as 'O'.
    

### Gameplay

-   Players take turns entering their move.
    
-   When it's your turn, you will be prompted to enter the row number (0, 1, or 2) and then the column number (0, 1, or 2).
    
-   The game board will be displayed in the terminal after each move.
    
-   The game concludes when one player wins or the board is full (a tie).
    

### Quitting the Game

To quit the game mid-play, when prompted to enter a row, type any non-integer character (like `q`) and press **Enter**. This will gracefully reset the server for the next players.

## IMPORTANT: API Keys Configuration

The provided script contains placeholder API keys and bin URLs for `jsonbin.io`. For reliability and security, it is **highly recommended** that you create your own free account and use your own keys.

1.  **Sign Up:** Go to [jsonbin.io](https://jsonbin.io/ "null") and create a free account.
    
2.  **Get Your Master Key:** After signing in, click on your avatar in the top-right, go to **API Keys**, and copy your `X-Master-Key`.
    
3.  **Create Bins:**
    
    -   Go to your dashboard and create at least 5 new, private JSON bins.
        
    -   For each bin, click the **"Copy ID"** button to get its unique ID.
        
4.  **Update the Script (`main.py`):**
    
    -   Open `main.py` and replace the placeholder `x_Master_Key` value with your own Master Key.
        
    -   Update the `servers` list with the URLs for the bins you created. The URL format is `https://api.jsonbin.io/v3/b/YOUR_BIN_ID`.
        
    
    ```
    # Example update in main.py
    
    x_Master_Key = '$2a$10$YOUR_OWN_MASTER_KEY_HERE'
    
    servers = [
        {
            "url": "[https://api.jsonbin.io/v3/b/FIRST_BIN_ID](https://api.jsonbin.io/v3/b/FIRST_BIN_ID)",
        },
        {
            "url": "[https://api.jsonbin.io/v3/b/SECOND_BIN_ID](https://api.jsonbin.io/v3/b/SECOND_BIN_ID)",
        },
        # ... and so on for all your bins
    ]
    
    ```
    

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
    
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
    
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
    
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
    
5.  Open a Pull Request
    

Some ideas for contributions include:

-   Enhancing the command-line interface (e.g., adding color, clearing the screen).
    

-   Implementing a "play again" feature.
    
-   Adding a simple AI for a single-player mode.
    
