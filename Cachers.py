import os
import pickle
import hashlib
from functools import wraps
# import sys

class Cacher():
    def __init__(self, cache_dir='./cached'):
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        self.cache_dir = cache_dir

    def rm_cache(self):
        for file in os.listdir(self.cache_dir):
            os.remove(os.path.join(self.cache_dir, file))
        print(f'All cache files removed from {self.cache_dir}')
class CacheDecorator(Cacher):
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate a unique cache file name based on function name and arguments
            
            # TODO: further improvement
            # 根据函数名和hash值范围分箱存储
            # print(str(args).encode() + str(kwargs).encode())
            # raise Exception('debug')
            cache_key = f"{func.__name__}_{hashlib.md5(str(args).encode() + str(kwargs).encode()).hexdigest()}.pickle"
            cache_file = os.path.join(self.cache_dir, cache_key)
            
            # Check if cache file exists
            if os.path.exists(cache_file):
                with open(cache_file, 'rb') as f:
                    # print(f'Loading result from cache file: {cache_file}')
                    return pickle.load(f)
            
            # Call the original function
            result = func(*args, **kwargs)
            
            # Write result to cache file
            with open(cache_file, 'wb') as f:
                pickle.dump(result, f)
                # print(f'Saving result to cache file: {cache_file}')
            
            return result
        return wrapper
    
    
    

class VariableCacher(Cacher):
    def cacheVar(self, data, cache_key):
        # 生成 cache_key 的哈希值
        hash_object = hashlib.sha256(cache_key.encode())
        hashed_key = hash_object.hexdigest()
        
        cache_file = os.path.join(self.cache_dir, hashed_key)
        with open(cache_file, 'wb') as f:
            pickle.dump(data, f)
            print(f'Saving result to cache file: {cache_file}')
    
    def loadVar(self, cache_key):
        # 生成 cache_key 的哈希值
        hash_object = hashlib.sha256(cache_key.encode())
        hashed_key = hash_object.hexdigest()
        
        cache_file = os.path.join(self.cache_dir, hashed_key)
        if not os.path.exists(cache_file):
            raise Exception(f'Cache file not found for key: {cache_key}')
        
        with open(cache_file, 'rb') as f:
            data = pickle.load(f)
            print(f'Loaded result from cache file: {cache_file}')
            return data