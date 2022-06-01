import requests

response = requests.get(url='https://api.themoviedb.org/3/trending/all/day?api_key=b7c72ad37773a8eb3a0254f31fafb0fd')
response.raise_for_status()
product_page = response.text

print(response.json())