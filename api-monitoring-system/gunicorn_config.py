import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
timeout = 30
keepalive = 5
errorlog = "-"
accesslog = "-"
loglevel = "info"