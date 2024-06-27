import re
import os
def comment_remover(source_code):
    source_code = re.sub(r'//.*,','',source_code)
    source_code = re.sub(r'/\*.*?\*/','',source_code,flags=re.DOTALL)
    return source_code
print("enter c code")
user_input = ""
while True:
    line=input()
    if not line:
        break
    user_input+=line+"\n"
com_code = comment_remover(user_input)
desktop_path = os.path.join(os.path.expanduser("~", "Desktop"))
output_file = os.path.join(desktop_path,"cleaned_code.txt")
with open(output_file,'w')as output_file:
    output_file.write(com_code)
print(f"cleaned code saved as{output_file}")
