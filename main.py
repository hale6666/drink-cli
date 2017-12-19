import api
import os

def main():
    if not os.path.isfile('./api.key'):
        raise SystemExit('Please put your API key in ./api.key and execute again.')


if __name__ = '__main__':
    main()
