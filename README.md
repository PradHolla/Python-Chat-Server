# Python Chat Server
A simple, Python based, one to one chat application built using Flask.


## Setup

```bash
git clone https://github.com/PradHolla/Python-Chat-Server.git
```

```bash
cd Python-Chat-Server
```

```bash
pip install -r requirements.txt
```

## Running the Chat Server

```bash
python main.py
```

## Running the Application
To run the application, enter:

```bash
127.0.0.1:5000
```
This project can also be run on a LAN. To do so, change SERVER parameter in `.env` file from 127.0.0.1 to `0.0.0.0`.
Execute `ipconfig` to get your IP address. Now enter your IP Address:5000 to run the application.

## Message History
The history page specifically contains the messages of a particular user who is logged in, unlike the homepage where all the chats are displayed.

Your messages are stored in the `messages.db` file. Delete the file if you want to erase chats.
