import sys
import os
from pypdf import PdfReader, PdfWriter

if len(sys.argv) < 2:
    print("Usage: python main.py input.pdf [password]")
    sys.exit(1)

input_file = sys.argv[1]
password = sys.argv[2] if len(sys.argv) > 2 else ""

name, ext = os.path.splitext(input_file)
output_file = f"{name}_unlocked{ext}"

reader = PdfReader(input_file)

# ---- decrypt properly ----
if reader.is_encrypted:
    result = reader.decrypt(password)

    if result == 0:
        print("❌ Wrong password or decryption failed")
        sys.exit(1)
    else:
        print("✅ Decryption successful")

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open(output_file, "wb") as f:
    writer.write(f)

print(f"✅ Unlocked file saved as: {output_file}")
