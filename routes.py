from main import app
import os

# Route to 'mine' (post) a new block

# Route to post a new transaction

# Route to register (post) a new neighbor

# Route to resolve neighboring chains (get the longest one from friends)


# Route to shut down our server (don't put these on actual applications, please)
@app.route("/terminate", methods=["GET"])
def shutdown_server():
    try:
        # Emulate a CTRL+C event to stop code function
        CTRL_C_EVENT = 0  # Value storage
        GenerateConsoleCtrlEvent(CTRL_C_EVENT, 0)
        return "Worked"
    except Exception as e:
        # In case of failure, make the operating system shut things down
        os._exit(0)  # This will probably throw a nasty error, but it WILL work
        return e
