import resizer
import os

print("\t\t\tAutomatic Image Resizer\t\t\t")
print("\t\t(press enter to submit input)")
print("_"*80)
print("1. In file explorer, open the folder that contains the target images")
print("2. Locate the folder's address: ")
print("\tThe sequence of folders you open to arrive at the current one is known as its 'address'")
print("\t\tLooks like ExamplePC > Example Pictures > Example Folder")
print("\t Right click on the rightmost label (the name of the current folder)")
print("\t Click 'Copy address as text'")
target_dir = input("3. Paste the address here: ")
resize_input = input("4. Pick a percentage size to rescale to\n(30% works well for shrinking A4 scans) Type here: ")
resize_mult = float(resize_input.replace("%", ""))/100

file_list = os.listdir(target_dir)
holding_dir = os.path.join(target_dir, "Resized Versions")
try:
    os.mkdir(holding_dir)
except:
    "Adding to existing resize folder"
    file_list.remove("Resized Versions")

print(file_list)
for image in file_list:
    resizer.resize(target_dir, holding_dir, image, resize_mult)