# coding=utf-8

from os import path
import logging



# ===================================
#   LOGGING
# ===================================

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger('researchKit')
handler = logging.FileHandler(path.join(path.dirname(__file__),
                              "../logs/researchKit.log"))
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.ERROR)

# ===================================
#   TORNADO
# ===================================

TORNADO = dict(
    db_name="",
    db_uri="",
    db_user="",
    db_pass="",
    login_url="/auth/login",
    static_path=path.join(path.dirname(__file__)+"/../", "output"),
    template_path=path.join(path.dirname(__file__)+"/../", "templates"),
    cookie_secret="SOMETHING HERE",
    debug=False,
    debug_pdb=False,
)


def __subdir_as_abs_path(subdir):
    PROJECT_DIR = path.dirname(path.abspath(__file__))
    return path.abspath(path.join(PROJECT_DIR, '..', subdir)) + '/'


