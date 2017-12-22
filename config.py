import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you can not guess string'
    VEPC_FILE_PATH = os.path.join(
        basedir, 'app', 'info', 'vepc_flexible_communication_bsp_vsfo.cfg')
    BCAT_GIT_URL = os.environ.get('BCAT_GIT_URL')

    UPLOAD_FOLDER = '/tmp/uploads/'
    ALLOWED_EXTENSIONS = set(['yml', 'yaml'])
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    @staticmethod
    def init_app(app):
        pass


class DebugConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class ProductCconfig(Config):
    DEBUG = False


config = {"default": Config,
          "debug": DebugConfig,
          "product": ProductCconfig}

if __name__ == '__main__':
    print basedir
    print Config.VEPC_FILE_PATH
