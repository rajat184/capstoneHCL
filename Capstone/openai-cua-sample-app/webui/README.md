CUA Web UI (prototype)

This is a lightweight local frontend prototype for interacting with the CUA agent.

Files:
- `templates/index.html` – main UI
- `static/style.css` – styles
- `static/app.js` – client JS (posts to `/api/send-task`)
- `server.py` – minimal Flask server to serve the UI and a demo endpoint

How to run:

1. Activate the project virtual environment:

```powershell
cd C:\Users\RAJAT JAISWAL\Desktop\CUA\openai-cua-sample-app
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies (if not already):

```powershell
pip install -r requirements.txt
```

3. Start the web UI server:

```powershell
python webui/server.py
```

4. Open http://localhost:5001 in your browser.

Next steps to integrate with CUA:
- Replace the `/api/send-task` endpoint to call the Agent's run loop or enqueue tasks for execution.
- Add websocket or SSE to display screenshots and live updates from the agent.
- Implement authentication if exposing this UI remotely.
