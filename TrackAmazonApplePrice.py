import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/500GB-2-5-inch-Internal-Solid-WDS500G2B0A/dp/B073SBZ8YH?ref_=Oct_d_orecs_d_1375379031&pd_rd_w=6Gf3b&pf_rd_p=b03e4d5d-30a1-4b98-9fee-e5c8fa7446f9&pf_rd_r=TETFPT5VHEBJMXT1BT41&pd_rd_r=6ef0a387-ee75-4989-960d-90188e3abcb1&pd_rd_wg=Vvwrl&pd_rd_i=B073SBZ8YH "

headers = {"user.agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.131 Safari/537.36"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
price = float(soup.find(id="priceblock_ourprice").text.split()[0][1:].replace(",", ""))
print(price)
