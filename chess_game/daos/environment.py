from environs import Env

env = Env()
try:
    env.read_env(path="./.env")
except IOError as e:
    print(e)
