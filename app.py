#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import os 
app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot (ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def app():
    results_url = "https://www.jamb.org.ng/efacility_/Login"
    browser.get(results_url)
    user = browser.find_element_by_id("email")
    user.send_keys("oluwashaeyhoon@gmail.com")
    pas = browser.find_element_by_id("password")
    pas.send_keys("renaissance")
    login = browser.find_element_by_id('lnkLogin')
    login.click()
    sts = browser.find_element_by_partial_link_text("Check Admission Status")
    sts.click()
    reg = browser.find_element_by_id('MainContent_RegNumber')
    reg.clear()
    reg.send_keys('96503384CF')
    access = browser.find_element_by_id('MainContent_btnCAPS')
    access.click()
    sts = browser.find_element_by_partial_link_text("Admission Status")
    sts.click()
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    res = soup.find_all("div","col-lg-6")
    mm = res[4].text
    
    browser.get(results_url)
    user = browser.find_element_by_id("email")
    user.send_keys("ademorotis@gmail.com")
    pas = browser.find_element_by_id("password")
    pas.send_keys("renaissance")
    login = browser.find_element_by_id('lnkLogin')
    login.click()
    sts = browser.find_element_by_partial_link_text("Check Admission Status")
    sts.click()
    reg = browser.find_element_by_id('MainContent_RegNumber')
    reg.send_keys('99117852EB')
    access = browser.find_element_by_id('MainContent_btnCAPS')
    access.click()
    sts = browser.find_element_by_partial_link_text("Admission Status")
    sts.click()
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    res = soup.find_all("div","col-lg-6")
    kk = res[4].text
    
    # me == my email address
    # you == recipient's email address
    me =  "owoeyepo@gmail.com" 
    to = 'Data Bot <oluwashaeyhoon@gmail.com>'
    cc = ""
    bcc = ""
    
    
    
    
    
    # Create message container - the correct MIME type is multipart/alternative.
    rcpt = cc.split(",") + bcc.split(",") + [to]
    msg = MIMEMultipart('alternative')
    msg['Subject'] = kk
    msg['From'] = me
    msg['To'] = to
    msg['Cc'] = cc
    msg['Bcc'] = bcc
    msg['Date'] = formatdate(localtime = True) 
    
    
    
    
    #Define a function for local time to be embedded in the email body 
    def today():
        return formatdate(localtime=True)
    text = "Swift"
    html = """<html>
    <body>
    
     <h1><p><img src="https://www.jamb.org.ng/images/banner.png" width="400" height="42"></P> </h1> 
     <small><p>Here are the <b>JAMB CAPS details </b> for Today<br></small>
      """ + today() + """
       
      <hr>
      <br>
      <p></P>  
      """ + "<b>DE:</b> <i>" + kk + "</i>//// <b>UTME:</b> <i>" + mm + """</i></p>
      <br>
      
      <hr>
      
      <br>
    
         
      <br>
    
    
     
    <footer>
      <p>Brewed by: <b>AutoCAPS</b></p>
      <p>Contact information: <a href="autocaps.herokuapp.com">AutoCAPS.herokuapp.com</a>.</p>
    </footer>
    
    <p><strong>Note:</strong> <kbd>Copyright 2018-2019 by AutoCAPS. All Rights Reserved..</kbd></p>
    
            
      </body>
    </html>
    """
    
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    #part3 = MIMEImage(("C:\Ice Packs\data\myfig.jpeg").read())
    
    
    
    
    
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    #msg.attach(part3)
    
    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls() 
    s.login(me, PESS)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, rcpt, msg.as_string())
    s.quit()
    
    
    # In[ ]:
    dt.datetime.now().strftime("%d %B %Y")
    
if __name__ == '__main__':
    mk = 0
    while True:
        app.run()
        mk += 1
        print(mk)
        for i in range(60):
            print(str(i) + "[sec]")
            time.sleep(1)
