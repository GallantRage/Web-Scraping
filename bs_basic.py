# BeautifulSoup(html_string, "html.parser") - parse HTML
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" class="special">
	<title>First HTML Page</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text.</p>
	</div>
	<ol>
		<li class="special super-special">This list item is special.</li>
		<li class="special">This list item is also special.</li>
		<li>This list item is not special.</li>
	</ol>
	<div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Basics of navigation ------------------------------------------

#print(soup.body.div)
#print(soup.find_all("div"))

# d = soup.find(id="first")
# print(d)

# d = soup.find_all(class_="special")
# print(d)

# d = soup.find_all(attrs={"data-example": "yes"})
# print(d)

# d = soup.select("[data-example]")
# print(d)

# Basics of accessing data ------------------------------------------

#el = soup.select(".special")[0]
# for el in soup.select(".special"):
# 	print(el.name)
# 	print(el.get_text())
# 	print(el.attrs["class"])

attr = soup.find("h3")["data-example"]
attr2 = soup.find("div")["id"]
print(attr)
print(attr2)
attr2 = soup.find("div").attrs
print(attr2)