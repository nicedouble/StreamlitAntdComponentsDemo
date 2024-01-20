"""Main module."""
import os

import fire
from streamlit import config as _config
from streamlit.web.bootstrap import run


def run_app(app_name: str = 'app'):
    """robyn app."""
    print('run app')
    print(vars())

    _config.set_option("server.headless", True)

    app_name_ = f"{app_name}.py"
    app_name_ = str(app_name_)
    if not os.path.exists(app_name_):
        raise FileNotFoundError(f"File {app_name_} not found")
    run(app_name_, [], args=[], flag_options=[])


def main():
    """Execute main program."""
    fire.Fire(run_app)
    print('\x1b[6;30;42m', 'Success!', '\x1b[0m')


if __name__ == "__main__":
    main()
