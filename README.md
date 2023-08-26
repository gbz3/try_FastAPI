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
```
