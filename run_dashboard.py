"""
Entry point.

Run from the project root:   python run_dashboard.py
Or serve it properly with:   gunicorn run_dashboard:server
"""

from __future__ import annotations

from dashboard.app import create_app

app = create_app()

# gunicorn and other WSGI servers look for the underlying Flask object.
server = app.server

if __name__ == "__main__":
    app.run(debug=True, port=8050)
