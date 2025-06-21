# 📸 Instagram Auto Post Script (Python)

This is a simple Python automation script that lets you auto-post an image to Instagram directly from your local machine.

Built using the instagrapi library, this script allows you to:
- Login to your Instagram account
- Upload a photo with a custom caption
- Handle Instagram’s login challenge (verification code)
- Fully automate your posting workflow

---

## 🚀 Features

- ✅ Post any `.jpg` or `.png` image to your IG feed
- ✅ Add your own custom caption
- ✅ Handles verification via email/SMS challenge
- ✅ Beginner-friendly and easy to edit

---

## 📂 File Structure

📁 Project Folder  
├── insta_auto_post.py      # Main source code  
├── README.md               # This file  
└── test.png                # Example image (optional)

---

## ⚙️ How to Use

1. Install the required library:
   pip install instagrapi

2. Open the file `insta_auto_post.py` in your code editor.

3. Edit the following placeholders:

   username = "ENTER_USERNAME_HERE"  
   password = "ENTER_PASSWORD_HERE"  
   image_path = r"C:\Path\To\Your\Image.png"  
   caption = "Write your caption here"

4. Run the script:
   python insta_auto_post.py

5. Enter the 6-digit code sent to your email or phone when prompted (first-time login only).

---

## 🛡 Important Notes

- This script uses Instagram’s private API, so use it responsibly.
- Avoid spamming or posting too frequently to prevent account flags or bans.
- For better security, you can later upgrade this to use `.env` files for credentials.

---

## 🙌 Credits

Made by Abaan
Based on instagrapi by @adw0rd

---

## 📜 License

MIT License – feel free to use, share, and modify!
