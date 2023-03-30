# HandyGame

This is the client for the server defined here: https://github.com/Aaron-McGill/HandyGameServer

To run this locally, you'd open three terminals.

In the first terminal, you'd clone the HandyGameServer project above and run one of these commands:

For Windows:

`
py app.py
`

For Linux/Mac:

`
python3 main.py
`

In the other two terminals, you'd open a copy of this project and run one of these commands:

For Windows:

`
py main.py
`

For Linux/Mac:

`
python3 main.py
`

With the server running, you should be able to play a game of Tic-Tac-Toe or Connect Four from the two windows that opened.

NOTE: Currently, you'll need to set an environment variable, SERVER_HOST, to point to the locally running server: http://127.0.0.1:8080.
Alternatively, you can just change the hardcoded default value for SERVER_HOST in the [main.py](main.py) file. The current default value
points to a version of the game server hosted in Render.