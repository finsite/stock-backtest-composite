# Stock Backtest Repository

This repository implements a production-ready backtesting module used to
simulate trading strategies on historical stock data. It is part of the larger
stock data ecosystem and supports:

- Clean integration with RabbitMQ for message input/output
- Pluggable strategy logic for signal generation and execution
- Paper trading and data enrichment
- Retry logic and metrics support

## Features

- 🧠 Strategy computation or ML model-based decision logic
- 📈 Optional database and message output support
- 🧪 Full testability and configurable dry-run mode
- 📊 Prometheus metrics instrumentation
- 🔁 Retry support via `tenacity`
- 🔐 Vault-based secure configuration

## Structure

```
.
├── src/
│   └── app/
│       ├── config.py
│       ├── main.py
│       ├── processor.py
│       └── utils/
│           ├── setup_logger.py
│           └── ...
├── tests/
├── requirements.in
├── requirements.txt
└── Makefile
```

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the processor (main entrypoint)
python -m app.main
```

## Development

```bash
# Format and lint
make lint

# Type check
make typecheck

# Run tests
make test
```

## Notes

- Messages are consumed from RabbitMQ or SQS depending on configuration.
- Outputs are routed via `output_handler.py`.
- Add new strategy logic under `processor.py`.
