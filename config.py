import os, sys

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-guess-forever'
    SQLALCHEMY_TRACK_MODICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    BOOTSTRAP_SERVE_LOCAL = True
    UPLOAD_FOLDER = os.path.join(basedir ,'app/static/uploads')
    HEATMAP_FOLDER = os.path.join(basedir ,'app/static/heatmaps')
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    if not os.path.exists(HEATMAP_FOLDER):
        os.mkdir(HEATMAP_FOLDER)

class DevelopmentConfig(Config):
    DEBUG =True
    # CKEDITOR_ENABLE_CSRF = True
    # CKEDITOR_CODE_THEME = 'monokai_sublime'
    # CKEDITOR_FILE_UPLOADER = 'admin_bp.upload_image' # view function

class ProductionConfig(Config):
    None

config_map = {
    'develop': DevelopmentConfig, 'product': ProductionConfig
}
