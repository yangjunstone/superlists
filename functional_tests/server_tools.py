from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

ROOT_PASSWORD_FOR_SERVER = 'yangjun'

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status',
            '--password={}'.format(ROOT_PASSWORD_FOR_SERVER)
        ],
        cwd=THIS_FOLDER
    ).decode().strip()


def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host), '--password={}'.format(ROOT_PASSWORD_FOR_SERVER)],
        cwd=THIS_FOLDER
    )