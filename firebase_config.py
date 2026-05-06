import firebase_admin
from firebase_admin import credentials, firestore
import os
from datetime import datetime

# Initialize Firebase
# NOTE: You must place your 'serviceAccountKey.json' file in the same directory
# or update the path below.
CRED_PATH = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')

db = None

def init_firebase():
    global db
    if not firebase_admin._apps:
        if os.path.exists(CRED_PATH):
            try:
                # Attempt to load credentials
                cred = credentials.Certificate(CRED_PATH)
                firebase_admin.initialize_app(cred)
                db = firestore.client()
                print("Firebase initialized successfully.")
            except Exception as e:
                # Gracefully handle invalid/dummy keys
                print("\n" + "="*50)
                print(f"WARNING: Firebase initialization failed.")
                print(f"Reason: {e}")
                print("INFO: The app will run in 'OFFLINE MODE'.")
                print("Results will be shown on screen but NOT saved to the database.")
                print("To fix this, download a valid 'serviceAccountKey.json' from Firebase Console.")
                print("="*50 + "\n")
                db = None
        else:
            print(f"WARNING: Firebase service account key not found at {CRED_PATH}.")
            print("Results will NOT be saved to database.")
            db = None
    else:
         try:
            db = firestore.client()
         except Exception:
            db = None

def save_analysis_result(data):
    """
    Saves the analysis result to Firebase Firestore.
    """
    if db is None:
        print("Database not initialized. Skipping save.")
        return False
    
    try:
        # Add timestamp
        data['timestamp'] = datetime.now()
        
        # Add to collection 'skill_analysis'
        db.collection('skill_analysis').add(data)
        print("Result saved to Firebase.")
        return True
    except Exception as e:
        print(f"Error saving to Firebase: {e}")
        return False

# Initialize on module load
init_firebase()