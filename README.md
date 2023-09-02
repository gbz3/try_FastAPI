# try_FastAPI

## 第1章

### 初めての FastAPI アプリケーション

#### インストール

```bash
$ python3.10 -m venv env
$ source env/bin/activate
(env) $ pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
...
Installing collected packages: websockets, uvloop, typing-extensions, sniffio, pyyaml, python-dotenv, idna, httptools, h11, exceptiongroup, click, annotated-types, uvicorn, pydantic-core, anyio, watchfiles, starlette, pydantic, fastapi
Successfully installed annotated-types-0.5.0 anyio-3.7.1 click-8.1.7 exceptiongroup-1.1.3 fastapi-0.100.0 h11-0.14.0 httptools-0.6.0 idna-3.4 pydantic-2.3.0 pydantic-core-2.6.3 python-dotenv-1.0.0 pyyaml-6.0.1 sniffio-1.3.0 starlette-0.27.0 typing-extensions-4.7.1 uvicorn-0.22.0 uvloop-0.17.0 watchfiles-0.20.0 websockets-11.0.3
(env) $ 
```

#### ローカルでの実行

```bash
# サーバ側
(env) $ uvicorn main:app
INFO:     Started server process [8318]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:39048 - "GET /?vscodeBrowserReqId=1693024997150 HTTP/1.1" 404 Not Found
...
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [8318]
(env) $ deactivate
$ rm -rf env
$

# クライアント側
(env) $ curl 127.0.0.1:8000/hello
{"hello":"world"}(env) $
```

## 第２章

- 本章以降では章ごとにディレクトリを作成し、その中で作業する

### GET/POST

```bash
# サーバ側
$ mkdir 2nd && cd 2nd
$ python3.10 -m venv env
$ source env/bin/activate
(env) $ pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
(env) $ mkdir app
(env) $ touch app/__init__.py
(env) $ touch app/main.py
(env) $ uvicorn app.main:app --reload
...
User-Agent:  curl/7.81.0
INFO:     127.0.0.1:46228 - "GET /wallets/1?include_histories=true HTTP/1.1" 200 OK

# クライアント側
$ curl -X GET 127.0.0.1:8000/wallets
[{"wallet_id":1}]

$ curl -X POST 127.0.0.1:8000/wallets
{"wallet_id":2}

# リクエストパラメータの定義
$ curl 127.0.0.1:8000/wallets/1
{"wallet_id":1}

$ curl 127.0.0.1:8000/wallets/2
{"wallet_id":2}

# エンドポイントの優先順位
$ curl 127.0.0.1:8000/wallets/meta
{"meta":{"count":2}}

# クエリパラメータの取得
$ curl '127.0.0.1:8000/wallets/1?include_histories=true'
{"wallet_id":1,"histories":[{"history_id":1}]}

# ヘッダ情報の取得
$ curl '127.0.0.1:8000/wallets/1?include_histories=true'
{"wallet_id":1,"histories":[{"history_id":1}]}

# リクエストパラメータのバリデーション
$ curl '127.0.0.1:8000/wallets/0'
{"detail":[{"type":"greater_than_equal","loc":["path","wallet_id"],"msg":"Input should be greater than or equal to 1","input":"0","ctx":{"ge":1},"url":"https://errors.pydantic.dev/2.3/v/greater_than_equal"}]}

# リクエストデータとレスポンスデータの定義
$ curl -X POST -H 'Content-Type: application/json' -d '{"name": "hoge"}' 127.0.0.1:8000/wallets
{"wallet_id":1,"name":"hoge"}
```

## 第3章 非同期処理

### HTTPX

```bash
$ mkdir 3rd && cd 3rd
$ python3.10 -m venv env
$ source env/bin/activate
(env) $ pip install httpx==0.24.1
(env) $ touch main.py
(env) $ python3 main.py 
main started
1 started
2 started
3 started
3 finished: 0:00:00.301495
2 finished: 0:00:00.354017
1 finished: 0:00:00.403114
result=['1:200', '2:200', '3:200']
main finished: 0:00:00.403467
(env) $
```

### Uvicorn

```bash
# サーバ側
(env) $ pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
(env) $ mkdir app
(env) $ touch app/__init__.py
(env) $ touch app/main.py
(env) $ uvicorn app.main:app --reload
...
started: 1
started: 1
started: 1
started: 2
started: 2
started: 2
started: 3
started: 3
started: 3
finished
finished
INFO:     127.0.0.1:58594 - "GET /awesome_orgs HTTP/1.1" 200 OK
INFO:     127.0.0.1:58592 - "GET /awesome_orgs HTTP/1.1" 200 OK
finished
INFO:     127.0.0.1:58576 - "GET /awesome_orgs HTTP/1.1" 200 OK

# クライアント側
$ for i in {0..2} ; do curl 127.0.0.1:8000/awesome_orgs &  done
[1] 13277
[2] 13278
[3] 13279
[200,200,200][200,200,200][200,200,200]
$ 
```

### pytest

```bash
(env) $ pip install pytest==7.4.0
(env) $ mkdir app/tests
(env) $ touch app/tests/__init__.py
(env) $ touch app/tests/conftest.py
(env) $ touch app/tests/test_main.py
(env) $ pytest -v app
==================================================================== test session starts ====================================================================
platform linux -- Python 3.10.12, pytest-7.4.0, pluggy-1.3.0 -- ~/repos/github/try_FastAPI/3rd/env/bin/python3.10
cachedir: .pytest_cache
rootdir: ~/repos/github/try_FastAPI/3rd
plugins: anyio-3.7.1
collected 1 item                                                                                                                                            

app/tests/test_main.py::test_get_async_hello PASSED                                                                                                   [100%]

===================================================================== 1 passed in 0.03s =====================================================================
(env) $ 
```

## 第４章  FastAPIの豊富な機能

```bash
# サーバ側
$ mkdir 4th && cd 4th
$ python3.10 -m venv env
$ source env/bin/activate
(env) $ pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
(env) $ mkdir -p app/api/wallets/histories
(env) $ touch app/{__init__,main}.py
(env) $ touch app/api/__init__.py
(env) $ touch app/api/wallets/{__init__,schemas,views}.py
(env) $ touch app/api/wallets/histories/{__init__,schemas,views}.py
(env) $ uvicorn app.main:app --reload

# クライアント側
$ curl -X GET 127.0.0.1:8000/api/wallets
[{"wallet_id":1},{"wallet_id":2}]

$ curl -X GET 127.0.0.1:8000/api/wallets/1
{"wallet_id":1}

$ curl -X GET 127.0.0.1:8000/api/wallets/1/histories
[{"history_id":1},{"history_id":2}]

$ curl -X GET 127.0.0.1:8000/api/wallets/1/histories/2
{"history_id":2}

$ curl -v -X GET 127.0.0.1:8000/api/wallets/0
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
> GET /api/wallets/0 HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< date: Sun, 27 Aug 2023 00:25:24 GMT
< server: uvicorn
< content-length: 22
< content-type: application/json
< 
* Connection #0 to host 127.0.0.1 left intact
{"detail":"Not Found"}

$ curl -v -X GET 127.0.0.1:8000/api/wallets/0
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
> GET /api/wallets/0 HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< date: Sun, 27 Aug 2023 00:44:08 GMT
< server: uvicorn
< content-length: 46
< content-type: application/json
< 
* Connection #0 to host 127.0.0.1 left intact
{"message":"Not Found","details":{"Wallet":0}}
```

### 初期化や後処理

```bash
(env) $ uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['~/repos/github/try_FastAPI/4th']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [43501] using WatchFiles
INFO:     Started server process [43503]
INFO:     Waiting for application startup.
startup!!!
INFO:     Application startup complete.
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
shutdown!!!
INFO:     Application shutdown complete.
INFO:     Finished server process [43503]
INFO:     Stopping reloader process [43501]
(env) $
```

### DI

```bash
# サーバ側
(env) $ uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['~/repos/github/try_FastAPI/4th']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [46992] using WatchFiles
INFO:     Started server process [46994]
INFO:     Waiting for application startup.
startup!!!
INFO:     Application startup complete.
processing time: 0:00:00.000344
INFO:     127.0.0.1:53724 - "GET /api/wallets/1 HTTP/1.1" 403 Forbidden

# クライアント側
$ curl -v -X GET 127.0.0.1:8000/api/wallets/1
Note: Unnecessary use of -X or --request, GET is already inferred.
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
> GET /api/wallets/1 HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 403 Forbidden
< date: Sun, 27 Aug 2023 01:16:52 GMT
< server: uvicorn
< content-length: 30
< content-type: application/json
< 
* Connection #0 to host 127.0.0.1 left intact
{"detail":"Not authenticated"}
```

### Background Tasks

```bash
# サーバ側
$ uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['~/repos/github/try_FastAPI/4th']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [53887] using WatchFiles
INFO:     Started server process [53889]
INFO:     Waiting for application startup.
startup!!!
INFO:     Application startup complete.
processing time: 0:00:00.000641
INFO:     127.0.0.1:44172 - "POST /api/wallets/export HTTP/1.1" 202 Accepted
Exporting...
Completed: hoge

# クライアント側
$ curl -v -X POST -H 'Content-Type: application/json' -d '{"dest": "hoge"}' 127.0.0.1:8000/api/wallets/export
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000 (#0)
> POST /api/wallets/export HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 16
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 202 Accepted
< date: Sun, 27 Aug 2023 01:47:57 GMT
< server: uvicorn
< content-length: 4
< content-type: application/json
< 
* Connection #0 to host 127.0.0.1 left intact
null
```

## 第5章 SQLAlchemy

### install

```bash
# DB
$ mkdir 5th && cd 5th
$ python3.10 -m venv env
$ source env/bin/activate
(env) $ pip install 'SQLAlchemy[aiosqlite]==2.0.18'
(env) $ sudo apt install sqlite3
(env) $ sqlite3 database.db << EOF
CREATE TABLE wallets (
 wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(64) NOT NULL
);
CREATE TABLE histories (
 history_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(64) NOT NULL,
 amount INTEGER NOT NULL,
 wallet_id INTEGER NOT NULL,
 FOREIGN KEY (wallet_id) REFERENCES wallets(wallet_id)
);
INSERT INTO wallets(name) VALUES
 ('Wallet 1'),
 ('Wallet 2')
;
INSERT INTO histories(name, amount, wallet_id) VALUES
 ('Tea', 140, 1),
 ('Juice', '200', 1)
;
EOF

# シンプルなクエリの実行
(env) $ python3
>>> from sqlalchemy import create_engine, text
>>> engine = create_engine("sqlite+pysqlite:///database.db", echo=True)
>>> stmt = text("SELECT * FROM wallets;")
>>> with engine.connect() as conn:
...     result = conn.execute(stmt)
... 
2023-09-03 07:34:47,800 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-09-03 07:34:47,801 INFO sqlalchemy.engine.Engine SELECT * FROM wallets;
2023-09-03 07:34:47,801 INFO sqlalchemy.engine.Engine [generated in 0.00043s] ()
2023-09-03 07:34:47,802 INFO sqlalchemy.engine.Engine ROLLBACK
>>> list(result)
[(1, 'Wallet 1'), (2, 'Wallet 2')]
>>> stmt = text("""INSERT INTO wallets(name) VALUES('Wallet 3'), ('Wallet 4');""")
>>> with engine.begin() as conn:
...     _ = conn.execute(stmt)
... 
2023-09-03 07:38:49,789 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-09-03 07:38:49,790 INFO sqlalchemy.engine.Engine INSERT INTO wallets(name) VALUES('Wallet 3'), ('Wallet 4');
2023-09-03 07:38:49,790 INFO sqlalchemy.engine.Engine [generated in 0.00028s] ()
2023-09-03 07:38:49,790 INFO sqlalchemy.engine.Engine COMMIT
>>> from sqlalchemy import MetaData, Table, select
>>> meta = MetaData()
>>> wallets = Table("wallets", meta, autoload_with=engine)
2023-09-03 07:41:18,906 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-09-03 07:41:18,907 INFO sqlalchemy.engine.Engine PRAGMA main.table_xinfo("wallets")
2023-09-03 07:41:18,907 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,908 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
2023-09-03 07:41:18,908 INFO sqlalchemy.engine.Engine [raw sql] ('wallets',)
2023-09-03 07:41:18,909 INFO sqlalchemy.engine.Engine PRAGMA main.foreign_key_list("wallets")
2023-09-03 07:41:18,909 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,909 INFO sqlalchemy.engine.Engine PRAGMA temp.foreign_key_list("wallets")
2023-09-03 07:41:18,909 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,909 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
2023-09-03 07:41:18,909 INFO sqlalchemy.engine.Engine [raw sql] ('wallets',)
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("wallets")
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("wallets")
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("wallets")
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine PRAGMA main.index_list("wallets")
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list("wallets")
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,910 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("wallets")
2023-09-03 07:41:18,911 INFO sqlalchemy.engine.Engine [raw sql] ()
2023-09-03 07:41:18,911 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
2023-09-03 07:41:18,911 INFO sqlalchemy.engine.Engine [raw sql] ('wallets',)
2023-09-03 07:41:18,912 INFO sqlalchemy.engine.Engine ROLLBACK
>>> stmt = select(wallets).where(wallets.c.name == "Wallet 3")
>>> with engine.connect() as conn:
...     result = conn.execute(stmt)
... 
2023-09-03 07:45:23,208 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-09-03 07:45:23,208 INFO sqlalchemy.engine.Engine SELECT wallets.wallet_id, wallets.name 
FROM wallets 
WHERE wallets.name = ?
2023-09-03 07:45:23,208 INFO sqlalchemy.engine.Engine [generated in 0.00052s] ('Wallet 3',)
2023-09-03 07:45:23,209 INFO sqlalchemy.engine.Engine ROLLBACK
>>> list(result)
[(3, 'Wallet 3')]
>>> 

```
