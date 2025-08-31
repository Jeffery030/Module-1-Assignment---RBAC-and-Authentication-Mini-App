# Hardcoded login
username, role = "alice", "admin"   # change to "bob", "user"

def admin_panel():
    if role == "admin":
        print("\n--- Admin Panel ---\n1. Users\n2. Camera Settings")
    else:
        print("❌ Admins only.")

def user_dashboard():
    if role == "user":
        print("\n--- User Dashboard ---\nWelcome to your profile!")
    else:
        print("❌ Users only.")

print(f"\nLogged in as: {username} ({role})")
choice = input("1=Admin Panel, 2=User Dashboard: ")

if choice == "1": admin_panel()
elif choice == "2": user_dashboard()
else: print("Invalid choice.")

"""
Shows CIA triad: Confidentiality.
Only the right role can access its area.
"""