import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()
# Firebase Configuration
config = {
    "apiKey": "AIzaSyD2JB_D5QhVDcAK0F0gPVDT7NfKOsOVPdY",
    "authDomain": "verificationhub-5e6da.firebaseapp.com",
    "databaseURL": "https://verificationhub-5e6da.firebaseio.com",
    "projectId": "verificationhub-5e6da",
    "storageBucket": "verificationhub-5e6da.appspot.com",  # Corrected the storage bucket URL
    "messagingSenderId": "1079805441326",
    "appId": "1:1079805441326:web:552beb23185a88d4f1b6bf",
    "measurementId": "G-T80CQT2PYN"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# Register Function
def register(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

# Login Function
def login(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        return "success"
    except Exception as e:
        print(f"Error: {e}")
        return "failure"

# Test the functions (optional)
if __name__ == "__main__":
    email = "testuser@example.com"
    password = "testpassword123"

    print("Registering user...")
    print(register(email, password))

    print("Logging in user...")
    print(login(email, password))
