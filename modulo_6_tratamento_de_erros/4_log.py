import logging
"""
debug - Só estou enviando informações para desenvolvedores
info - Só enviando informações
warning - Quero alertar sobre algo que está acontecendo, possivelmente fora do esperado, porém ainda não é um erro, mas pode gerar um futuramente.
error - Um erro ocorreu na aplicação.
critical - Um erro com consequências graves acaba de ocorrer na aplicação.
"""
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s')# configurando o nível de mensagens de loggin
logging.debug('Loggin nível debug')
logging.info('Loggin nível info')
logging.warning('Loggin nível warning')
logging.error('Loggin nível error')
logging.critical('Loggin nível critical')