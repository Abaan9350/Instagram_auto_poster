from instagrapi import Client

# --- EDIT THESE VALUES BEFORE RUNNING ---
username = "ENTER_USERNAME_HERE"
password = "ENTER_PASSWORD_HERE"

image_path = r"C:\Users\User\Desktop\test.png"  # Change path to your image
caption = "Automated post via Python 🤖 #testupload"

# --- LOGIN & CHALLENGE HANDLING ---
cl = Client()

try:
    cl.login(username, password)
except Exception as e:
    print("⚠️ Login challenge triggered:", e)

    # Resolve login challenge (code sent to email/phone)
    challenge_info = cl.challenge_resolve()
    print("📩 Challenge info:", challenge_info)

    code = input("Enter the verification code you received: ")
    cl.challenge_send_code(code)
    cl.challenge_code(code)

# --- UPLOAD IMAGE ---
cl.photo_upload(image_path, caption)
print("✅ Post uploaded successfully.")
