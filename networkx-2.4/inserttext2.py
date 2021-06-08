from pathlib import Path

file_name = "index.html"

paths = Path('.').glob('**/*.html')
for path in paths:
    file_name = str(path)
    print(file_name)

    with open(file_name) as in_file:
        old_content = in_file.readlines()
    
    with open(file_name, "w") as in_file:
        for line in old_content:
            in_file.write(line)
            if 'role="main" class="document"' in line:
                 in_file.write('\n<div class="admonition warning">')
                 in_file.write('\n<p class="admonition-title">Warning</p>')
                 in_file.write('\n  <p>This documents an unmaintained version of NetworkX. Please upgrade to a maintained version and see <a href="https://networkx.org/documentation/stable/">the current NetworkX documentation</a>.</p>')
                 in_file.write('\n</div>\n')
