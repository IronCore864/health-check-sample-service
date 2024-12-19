# Health Check Sample Service

A sample service written in Python listening on port 5000 with a `/health` endpoint that:

- always returns success on the first access;
- 20% chance to fail;
- once fails, it always returns failure and could not recover.

Usage:

```bash
pip install -r requirements.txt
python main.py
```
