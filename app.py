from src import create_app
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
  "--config", dest = "config", type = str,
  help = "Specify the configuration (prod, dev, test)"
)

args = parser.parse_args()

app = create_app(args.config)

app.run(
  host = app.config['HOST'],
  port = app.config['PORT'],
  debug = app.config['DEBUG']
)