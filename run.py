import os

from instance import create_app

config = os.getenv('APP_SETTINGS')

app = create_app(config)

port = os.environ.get("PORT",5000)

if __name__ == "__main__":
	app.run(host='127.0.0.1')