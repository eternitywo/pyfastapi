# flash 관련 패키지 import
from flask import Flask, Blueprint

# 파일 처리 관련 패키지 import
import os
import pickle
import shutil
import tempfile
import glob

# json을 다루기 윈한 패키지 import
import json
from collections import OrderedDict  # dick key 의 순서를 보장한다. 그냥 dict 보장하지 않는다.

# 수학 모듈
import pandas as pd
import numpy as np
import six
import pytz
from dateutil.parser import parse

# NoSQL : MongoDB / Redis / kafka???
import pymongo as mongo
from rediscluster import RedisCluster as redis


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_flask():
        return 'Hello Flask'

    @app.route('/hi')
    def hi():
        return 'Hi! you found me'

    @app.route('/hahaha', methods=['GET'])
    def hahaha():
        # shutil.copy("app.py", "app_copy1.py") // 파일 카피
        # print(os.path)

        # return "hahaha"

        # print('this is glob output : ', glob("*"))  파일 리스트 가져오기

        for x in glob.glob('*'):
            if os.path.isdir(x):                # 디렉터리인가?
                print(x, '<DIR>')
            else:
                print(x)

        result = {}

        result["name"] = "dongho"
        result["data"] = {'age': 43, 'family': 'seo'}

        # json.loads(value) // json 물자열을 python 객체로 변환,  http body 등을 읽을 때 사용
        # json.dumps(result) // python object를 json 으로 출력한다.
        # json.load(filename) // json file을 python object로 반환
        # json.dump(filename) // python json 을 파일에 저장

        json_string = json.dumps(result, indent=2)
        print(result)
        print(json_string)

        assert result["name"] == "dongho"

        # print(request.method)

        # print(request)

        return json_string

    return app
