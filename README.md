
#### 启动redis
```redis-server.exe C:\Users\ZD\Redis-x64-5.0.14.1\redis.windows.conf```

#### 启动celery
```celery -A udm worker -l INFO -P eventlet```

#### 开发环境启动项目
```python manage.py runserver```


#### 生产环境启动项目
###### 1、普通启动
```gunicorn -c gunicorn.conf.py udm.wsgi:application```

###### 2、指定远程访问主机、4进程、gevent模式启动
```gunicorn udm.wsgi:application -b 0.0.0.0:8989 -w 4 -k gevent```

###### 3、指定远程访问主机、4进程、gevent模式、40个处理请求的工作线程数、4096最大请求数、启动
```gunicorn udm.wsgi:application -b 0.0.0.0:8989 -w 4 -k gevent  --thread 40 --max-requests 4096 --max-requests-jitter 512```

###### 4、查看进程
```ps aux | grep gunicorn```

###### 5、退出 gunicorn
```pkill gunicorn```