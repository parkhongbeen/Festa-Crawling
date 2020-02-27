daemon = False

chdir = '/srv/Festa-crawling/app'
bind = 'unix:/run/festa.sock'
accesslog = '/var/log/gunicorn/festa-access.log'
errorlog = '/var/log/gunicorn/festa-error.log'
capture_output = True
