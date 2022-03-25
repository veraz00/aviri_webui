
import os 
from app import create_app

if __name__ == '__main__':
    app = create_app('develop')
    app.jinjia_env.cache = {} # if front is installed in crystalvu, remove the cache limit 
    app.run(debug = True)
