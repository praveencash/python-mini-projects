import  os
		
# Create folders if they don't exist
os.makedirs("Images", exist_ok=True)
os.makedirs("Docs", exist_ok=True)
os.makedirs("Codes", exist_ok=True)

for file in os.listdir():
    if os.path.isfile(file):
        ext = os.path.splitext(file)[1].lower()
        
        if ext in [".jpg", ".png", ".gif"]:
            os.rename(file, f"Images/{file}")
        elif ext in [".pdf", ".docx", ".txt"]:
            os.rename(file, f"Docs/{file}")
        elif ext in [".sql", ".py"]:
            os.rename(file, f"Codes/{file}")
		