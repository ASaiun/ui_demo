import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you can not guess string'
    VEPC_FILE_PATH = os.path.join(
        basedir, 'app', 'info', 'vepc_flexible_communication_bsp_vsfo.cfg')

    UPLOAD_FOLDER = '/tmp/uploads/'
    ALLOWED_EXTENSIONS = set(['yml','yaml'])


    @staticmethod
    def init_app(app):
        pass

config = {"default": Config}

if __name__ == '__main__':
    print basedir
    print Config.VEPC_FILE_PATH
