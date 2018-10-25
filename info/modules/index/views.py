from info import redis_store
from . import index_blu


@index_blu.route('/')
def index():
    # 想redis中保存一个值
    redis_store.set("name", "itcast")
    return 'index'