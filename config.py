import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24335028")

API_HASH = os.environ.get("API_HASH", "b204ec833fb451fb913fc8e683b232d0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7531498113:AAESwZ-J9SX92mvjO7risOzFYvnDrc727OM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","aadarshkumar1234768")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://aadarshkumar1234768:Q8ptH5spkMkR93eg@cluster0.0ntbfcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
