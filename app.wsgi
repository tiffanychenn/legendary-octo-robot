import sys, os, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/legendary-octo-robot')
os.chdir('/var/www/legendary-octo-robot')
from app import app as application