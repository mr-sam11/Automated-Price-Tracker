import smtplib
import requests
from bs4 import BeautifulSoup

# make a string of URL of desired product
url = "https://www.amazon.in/500GB-2-5-inch-Internal-Solid-WDS500G2B0A/dp/B073SBZ8YH?ref_=Oct_d_orecs_d_1375379031&pd_rd_w=6Gf3b&pf_rd_p=b03e4d5d-30a1-4b98-9fee-e5c8fa7446f9&pf_rd_r=TETFPT5VHEBJMXT1BT41&pd_rd_r=6ef0a387-ee75-4989-960d-90188e3abcb1&pd_rd_wg=Vvwrl&pd_rd_i=B073SBZ8YH"

# ------------------------creating header---------------------------------------------

'''
HTTP headers User-Agent :It is a request header that allows a characteristic 
        string that allows network protocol peers to identify the Operating System and 
        Browser of the web-server.  


for more info : https://www.geeksforgeeks.org/http-headers-user-agent/#:~:text=The%20HTTP%20headers%20User%2DAgent,Browser%20of%20the%20web%2Dserver.
'''
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3729.169 Safari/537.36"}
'''
The following conclusions can be drawn with the help of user-agent header:

The user agent application is Mozilla version 5.0.
The operating system is NT version 10.0 (and is running on a Windows(64-bit) Machine).
The engine responsible for displaying content on this device is AppleWebKit version 537.36 (KHTML, an open-source layout engine, is present too).
The client is Chrome version 74.0.3729.169
The client is based on Safari version 537.36.

'''
# --------------------------End----------------------------------------------------------------


# ----------------Getting the webpage which is specified in "url"-----------------------------
page = requests.get(url, headers=headers)
# -----------------END-------------------------------------------------------------------


# ------------creating BeautifulSoup Object---------------------------------------------
# This is done by passing the html to the BeautifulSoup() function.The BeautifulSoup
# package is used to parse the html, that's take the raw html text and break into python
# objects.
soup = BeautifulSoup(page.content, 'html.parser')

# soup object allows us to extract interesting information about the website you're
# scraping such as getting the title of the page, you can also get the text of
# webpage and quickly print it out to check if it is what you expect

# --------------END---------------------------------------------------------------------


'''
#----------------product information----------------------------------
#produxt title
print(soup.title)

#get attribute
print(soup.title.name)

#get value
print(soup.title.string)

#beginning navigation
print(soup.title.parent.name)

#getting specific values
print(soup.p)


#all paragraph tag value
print(soup.find_all('p'))


# In[8]:


for paragraph in soup.find_all('p'):
    print(paragraph.string)
    #  or print(str(paragraph.text))


# In[9]:


for url in soup.find_all('a'):
    print(url.get('href'))


# In[10]:


print(soup.get_text())


# In[11]:


a = soup.find(id = "productTitle")
b = a.get_text()


# In[12]:


print(b.strip())


# In[13]:

----------------------------------END-----------------------------------------------

'''


price = float(soup.find(id="priceblock_ourprice").get_text().split()[0][1:].replace(",", ""))



# Sending mail to the user

def send_mail():

    SMTP_SERVER = "smtp.gmail.com"
    PORT = 587

    EMAIL_ID = "XYZ@gmail.com"
    PASSWORD = "1234"


    server = smtplib.SMTP(SMTP_SERVER, PORT)

    # start TLS for security 
    server.starttls()


    # Authentication 
    # from which Email Id you want to send the mail(sender_mail_id, Password)
    server.login(EMAIL_ID, PASSWORD )
    subject = "Price down!"
    body = "https://www.amazon.in/500GB-2-5-inch-Internal-Solid-WDS500G2B0A/dp/B073SBZ8YH?ref_" \
           "=Oct_d_orecs_d_1375379031&pd_rd_w=6Gf3b&pf_rd_p=b03e4d5d-30a1-4b98-9fee-e5c8fa7446f9&pf_rd_r" \
           "=TETFPT5VHEBJMXT1BT41&pd_rd_r=6ef0a387-ee75-4989-960d-90188e3abcb1&pd_rd_wg=Vvwrl&pd_rd_i=B073SBZ8YH "
    msg = f"Subject:{subject}\n\n{body}"

    # sending the mail
    server.sendmail(
        EMAIL_ID,
        EMAIL_ID,
        msg
    )
    # for our acknowledgement
    print("mail send")
    # Don't forget to terminate the session
    server.quit()


# main condition to check whether the prize goes down or not if it is, then send the mail
#   to specified mails id

# 6,400.0017499 is cur price when you checked at first time
# (if price doesn't drop )for getting the mail ,you have to use '=='
if price < 6500.0:
    send_mail()
