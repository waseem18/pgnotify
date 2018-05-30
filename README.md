# pgnotify

Python package to set triggers and listen to events from a Postgres database and receive the payload as JSON.

`pgnotify` will call the specified callback function whenever there is any event from the table(s) specified in the JSON.

### Installation

`pgnotify` can be installed using `pip`

```
pip install pgnotify
```

### Example

Here's an [example](https://github.com/waseem18/pgnotify/blob/master/examples/example.py) on how to use `pgnotify` to specify the tables on which triggers are to be setup and how to pass callback function to receive the JSON payload.

### License
MIT
