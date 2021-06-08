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
            if "wy-side-nav-search" in line:
                 in_file.write('\n    <a href="https://networkx.org/">Project Homepage</a> |')
                 in_file.write('\n    <a href="https://github.com/networkx/networkx">Source Code</a>\n')
