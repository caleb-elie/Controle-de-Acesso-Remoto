# Key Logger

A simple keylogger that captures keystrokes and serves them via an HTTP server. **For educational purposes only. Use responsibly and ethically.**

## Features

- Logs keystrokes.
- Serves logs via an HTTP server.
- Stops when `Esc` is pressed.

## Requirements

- Python 3.x
- `pynput` library

## Installation

```sh
git clone <repository_url>
cd key-logger
pip install -r requirements.txt
```

## Usage

```sh
python key_logger.py
```

- Access logs at `http://localhost:8000/log`.
- Example request:

```sh
curl http://localhost:8000/log
```

## Stopping the Logger

Press `Esc` to stop.

## Security & Ethics

- **Risk**: Logs all keystrokes, including sensitive data.
- **Ethics**: Only use in controlled environments with explicit permission.
- **Legal**: Unauthorized use is illegal.

## License

MIT License. See [LICENSE](LICENSE).

## Contact

For inquiries: [programming@example.com]

