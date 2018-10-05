import os
from app.apiv2.models.foodfast import create_tables,drop_tables
from instance import create_app


config = os.getenv('APP_SETTINGS')

app = create_app(config)


port = os.environ.get("PORT",5000)

if __name__ == "__main__":
	create_tables()
	
	
	app.run(host='127.0.0.1')