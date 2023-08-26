# try_FastAPI

## 第1章

### 初めての FastAPI アプリケーション

#### インストール

```shell
$ python3.10 -m venv env
$ source env/bin/activate
(env) $ pip install fastapi==0.100.0 'uvicorn[standard]==0.22.0'
...
Installing collected packages: websockets, uvloop, typing-extensions, sniffio, pyyaml, python-dotenv, idna, httptools, h11, exceptiongroup, click, annotated-types, uvicorn, pydantic-core, anyio, watchfiles, starlette, pydantic, fastapi
Successfully installed annotated-types-0.5.0 anyio-3.7.1 click-8.1.7 exceptiongroup-1.1.3 fastapi-0.100.0 h11-0.14.0 httptools-0.6.0 idna-3.4 pydantic-2.3.0 pydantic-core-2.6.3 python-dotenv-1.0.0 pyyaml-6.0.1 sniffio-1.3.0 starlette-0.27.0 typing-extensions-4.7.1 uvicorn-0.22.0 uvloop-0.17.0 watchfiles-0.20.0 websockets-11.0.3
(env) $ 
```

#### ローカルでの実行

```shell
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

```shell
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

```shell
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

```shell
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
