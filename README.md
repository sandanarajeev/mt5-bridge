Install the dependencies

WINDOWS

```
py -m pip install MetaTrader5
py -m pip install Flask
```

Start the server

```
py mt5BridgeServer.py
```

MAC

Install the dependencies

```
pip install MetaTrader5
pip install Flask
```

Start the server

```
python mt5BridgeServer.py
```

NOTE: pip3, pythons 3 also works

Start the server

Windows

```
py mt5BridgeServer.py
```

MAC

```
python mt5BridgeServer.py
```

ENDPOINT = http://localhost:5001/mt5

Replace localhost with Machine IP address when in network

Sample Request Body

To call mt5.initialize()

```
{
    "methodName": "initialize"
}
```

To call mt5.initialize(1,2,3)

```
{
    "methodName": "initialize",
    "args":[1,2,3]
}
```

To call mt5.initialize(x=1,y=2,z=3)

```
{
    "methodName": "initialize",
    "args": {
        x:1,
        y:2,
        z:3
    }
}
```
