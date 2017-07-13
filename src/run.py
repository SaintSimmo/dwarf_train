from app.dwarf_train import app, socketio
from multiprocessing import Process, Value


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=False)
