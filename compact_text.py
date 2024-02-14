import re

# Your input text with line breaks
input_text = """
And that could be a concatenation of account code and contract code, maybe. 
3:36
But we'll need something because yeah, even then that's two different addresses, right? 
3:44
"""

# Use regular expressions to join lines containing timestamps with the preceding lines
output_text = re.sub(r'(\d+:\d+)\n', r'\1 ', input_text)

# Remove remaining line breaks to create a compact paragraph
output_text = output_text.replace('\n', ' ')

# Print or use the output_text as needed
print(output_text)
