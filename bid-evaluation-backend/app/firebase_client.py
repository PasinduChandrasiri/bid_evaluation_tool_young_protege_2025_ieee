import os
import firebase_admin
from firebase_admin import credentials, storage

cred_path = os.getenv("FIREBASE_CREDENTIALS_JSON")
if not cred_path or not os.path.exists(cred_path):
    raise FileNotFoundError(f"Firebase credentials JSON file not found at path: {cred_path}")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET")
})

bucket = storage.bucket()

def upload_file_to_firebase(file, destination_path):
    blob = bucket.blob(destination_path)
    blob.upload_from_file(file)
    blob.make_public()
    return blob.public_url
