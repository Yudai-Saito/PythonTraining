import logging.config

#loggingへlogging.confを適用
logging.config.fileConfig("../logging.conf")

logger = logging.getLogger("__name__")

logging.debug("動作の診断に関する詳細情報")
logging.info("想定通りの動作の確認")
logging.warning("想定外のことが発生、問題が起こりそう")
logging.error("重大なエラーにより、機能の一部が停止")
logging.critical("プログラム全体がダウン、重大なエラー")
