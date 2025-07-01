import oxen
import oxen.auth
import os

os.makedirs("models/SEDD-large", exist_ok=True)

oxen.auth.config_auth(token=os.environ["OXEN_API_KEY"])
oxen.clone("https://hub.oxen.ai/models/SEDD-large", path="models/SEDD-large")

print("Model pulled successfully")