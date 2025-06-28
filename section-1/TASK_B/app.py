from flask import Flask

app = Flask(__name__)

@app.route("/")
def interactive_terminal():
    return """
    <html>
    <head>
        <title>Hack Console</title>
        <style>
            body {
                background-color: black;
                color: #00ff00;
                font-family: 'Courier New', monospace;
                padding: 40px;
                font-size: 18px;
                outline: none;
            }
        </style>
    </head>
    <body tabindex="0">
        <pre id="terminal"></pre>

        <script>
            const script = `
Connecting to 192.168.1.42...
Connection established.
Launching exploit...
Bypassing firewall...
Access granted.
root@target:~# ls -la
Reading secret.txt...
Uploading payload...
Success. Exiting...
            `.trim();

            let index = 0;
            const terminal = document.getElementById("terminal");

            document.body.focus();

            document.body.addEventListener("keydown", () => {
                if (index < script.length) {
                    terminal.textContent += script[index];
                    index++;
                }
            });
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
