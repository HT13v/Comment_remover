import re

# Define regular expression patterns for C comments
single_line_comment_pattern = re.compile(r'//.*')
multi_line_comment_pattern = re.compile(r'/\*.*?\*/', re.DOTALL)

def remove_comments(c_code):
    # Remove single-line comments
    c_code = single_line_comment_pattern.sub('', c_code)
    # Remove multi-line comments
    c_code = multi_line_comment_pattern.sub('', c_code)
    return c_code

# Function to get user input for C code
def get_user_input():
    print("Enter your C code (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

# Get C code from user input
c_code = get_user_input()

# Remove comments from the user input C code
clean_code = remove_comments(c_code)
print("Code without comments:")
print(clean_code)
