# 🧠 Assessment: Command-based Client-Server Application (Socket Programming)

## 🎯 Problem Statement
Design and implement a simple **command-based client-server application** using Python’s `socket` module.

### Requirements
1. **Server (server.py)**
   - Listens on a specific port (e.g., 5050).
   - Accepts one client connection at a time.
   - Supports the following commands from the client:
     - `TIME` → Server responds with the current system time.
     - `DATE` → Server responds with the current date.
     - `RANDOM` → Server responds with a random number between 1 and 100.
     - `EXIT` → Ends the client connection gracefully.
     - Any other command → `INVALID COMMAND`.

2. **Client (client.py)**
   - Connects to the server using IP and port.
   - Continuously asks the user to input a command.
   - Sends the command to the server and prints the response.
   - When the user types `EXIT`, the client should close the connection.

---

## 🧩 Skeleton Code for Students

### server_skeleton.py
```python
import socket
import datetime
import random

HOST = '127.0.0.1'
PORT = 5050

# TODO 1: Create a socket and bind it to host and port
# server_socket = ...

# TODO 2: Listen for incoming connections
# server_socket.listen(1)
# print(...)

# TODO 3: Accept client connection
# conn, addr = server_socket.accept()
# print(...)

while True:
    # TODO 4: Receive command from client
    # data = ...

    # TODO 5: Handle commands - TIME, DATE, RANDOM, EXIT
    # if data.upper() == 'TIME':
    #     response = ...
    # elif ...
    # else:
    #     response = "INVALID COMMAND"

    # TODO 6: Send response to client
    # conn.send(...)

    # TODO 7: Break loop on 'EXIT' and close connection
    pass
```

---

### client_skeleton.py
```python
import socket

HOST = '127.0.0.1'
PORT = 5050

# TODO 1: Create a socket and connect to the server
# client_socket = ...

# TODO 2: Loop to send commands to server
while True:
    # TODO 3: Take input command
    # command = ...

    # TODO 4: Send command to server
    # client_socket.send(...)

    # TODO 5: Receive and print response
    # response = ...

    # TODO 6: If command == 'EXIT', close connection and break
    pass
```

---

## 🧠 Assessment Criteria
- Correct use of `socket` module for both client and server.
- Proper handling of message encoding/decoding.
- Graceful connection closing on both ends.
- Code readability and comments.

---

### 💡 Expected Output Example

**Client Terminal:**
```
Connected to server at 127.0.0.1:5050
Enter command (TIME, DATE, RANDOM, EXIT): TIME
Server Response: 10:42:17
Enter command (TIME, DATE, RANDOM, EXIT): RANDOM
Server Response: 57
Enter command (TIME, DATE, RANDOM, EXIT): EXIT
Connection closed.
```

**Server Terminal:**
```
Server listening on port 5050...
Connection established with ('127.0.0.1', 56321)
Received command: TIME
Received command: RANDOM
Received command: EXIT
Client disconnected.
```
