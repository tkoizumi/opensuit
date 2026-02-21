import os

import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
from opensuit.main import run

if __name__ == "__main__":
    run()
