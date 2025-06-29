# TODO List – Backtest Repository

This file tracks remaining enhancements and cleanup tasks for this repository.

## ✅ Configuration

- [x] Enforce structured configuration via `config.py`
- [x] Add Vault-based secret handling
- [x] Add retryable message and output logic
- [x] Validate presence of `get_polling_interval()`, `get_output_mode()`, `get_rabbitmq_queue()`

## 🔁 Retry Logic

- [x] Add `tenacity`-based retry wrapper to output handlers
- [x] Apply exponential backoff for transient failures

## 🧪 Testing

- [ ] Add unit tests for:
  - `processor.py` logic
  - Output dispatch and retry flow
- [ ] Add test message generator or fixture
- [ ] Add `make test` and CI test execution

## 📊 Observability

- [x] Integrate Prometheus metrics via `track_*_metrics`
- [ ] Add structured JSON logging for all outputs
- [ ] Optionally forward logs to ELK or Loki

## 🚀 Paper Trading Enhancements

- [ ] Add dry-run toggle via `DRY_RUN` env
- [ ] Simulate fills, slippage, or order book depth
- [ ] Track PnL and log simulated trades

## 📦 Output Enhancements

- [ ] Support dynamic output targets (DB, S3, etc.)
- [ ] Add `output_handler.py` plugin system

## 🧰 Utility

- [x] Finalize shared utility modules from `repo-utils-shared`
- [x] Pin all production dependencies in `requirements.in`
- [x] Add auto-sync support for shared utilities

## 🛡️ Security

- [x] Add `bandit`, `pip-audit`, and SBOM checks
- [ ] Integrate secret scanning (e.g., detect-secrets)
- [ ] Confirm all dependencies pass vulnerability checks

## 📄 Documentation

- [ ] Expand this README with example data flow
- [ ] Add architectural diagram or usage example

---

This document is auto-synced via `repo-utils-shared/.template/backtest/TODO.md`
