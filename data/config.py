from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  
ADMINS = env.list("ADMINS")  
IP = env.str("ip")  
DB_Name=env.str("DB_Name")  
DB_password=env.str("DB_password")  
DB_user=env.str("DB_user")  



