# IP and port to bind to.
bind = ['127.0.0.1:5000']

# Maximum number of pending connections.
backlog = 2048

# Number of worker processes to handle connections.
workers = 2

# Fork main process to background.
daemon = True

# PID file to write to.
pidfile = "web.gunicorn.pid"

# Allow connections from any frontend proxy.
# forwarded_allow_ips = '*'

# Logging configuration.
accesslog = "web.gunicorn.access.log"
errorlog = "web.gunicorn.error.log"
loglevel = "warning"

# Gunicorn process name.
proc_name = "rouly.net-gunicorn"
