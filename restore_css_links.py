from pathlib import Path
p = Path('/home/min/code/me/index.html')
s = p.read_text()
old = '    <link rel="stylesheet" type="text/css" href="stylesheet.css">\n    <style>\n'
new = '    <link rel="stylesheet" type="text/css" href="stylesheet.css">\n    <link rel="stylesheet" href="css/ionicons.min.css">\n    <link rel="stylesheet" href="css/style.css">\n    <style>\n'
p.write_text(s.replace(old, new, 1))
