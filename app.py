from flask import Flask
from dotenv import load_dotenv
from unipath import Path

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # Load env file first if it exists
    env_file = Path('__file__').ancestor(1).child('.env')
    if env_file.exists():
        print('env exist')
        load_dotenv(env_file)
    app.run()
