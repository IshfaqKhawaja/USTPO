import csv
import urllib3
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# options = Options()
# options.headless = True
import requests
# driver = webdriver.Firefox(options=options, executable_path= r'C:\Users\Administrator.ESNO-HP-LP-066\Desktop\shiv\geckodriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://tsdr.uspto.gov")
LiteralElement = "N/A"
MarkType = "N/A"
Serial = "N/A"
TSDR = "N/A"
InterClass = "N/A"
appfilingdate = "N/A"
Publication_Date = "N/A"
CorrespondentNameAdd = "N/A"
Owner_org = "N/A"
phone = "N/A"
Legal_Entity = "N/A"
TM5_Common_Status = "N/A"
Status_Date = "N/A"
Date_Abandoned = "N/A"
Mail_date = "N/A"
doc_description = "N/A"
mail_recipient = "N/A"
mail_recipient_CC = "N/A"
f_sumvalue = "N/A"
OffAction_date = "N/A"
driver.find_element_by_id("searchNumber").clear()
element = driver.find_element_by_id("searchNumber")
irnis = '72368947'
Serial = irnis
print("--Serial --")
print(Serial)
time.sleep(2)
element.send_keys(Serial, Keys.ENTER)
time.sleep(10)
markText = driver.find_element_by_xpath("//div[@class='value markText']")
mark = markText.get_attribute('innerHTML')
LiteralElement = mark.strip()
print("-- LiteralElement --")
print(LiteralElement)
print("---TSDR---")
TSDR = (driver.current_url)
print(TSDR)
rows = driver.find_elements_by_xpath('//div[@class="row"]')
print("start")
for row in rows:
    # print("row is")
    print(row.text)
    thistxt = row.text

    if ("Mark Type:" in thistxt):
        MarkType = thistxt.replace("Mark Type:", "")
        MarkType = MarkType.strip()
        print("(2).... Mark is --")
        print(MarkType)

    if ("Application Filing Date:" in thistxt):
        thisindex = thistxt.index("Application Filing Date:")
        newstr = thistxt[thisindex:]
        # print("new string is")
        # print(newstr)
        newstr = newstr.replace("Application Filing Date:", "")
        appfilingdate = newstr.strip()
        print("(1).... application filing date--")
        print(appfilingdate)

    if ("TM5 Common Status Descriptor:" in thistxt):
        print("--TM5 Common Status is")
        TM5_Common_Status = thistxt.replace("TM5 Common Status Descriptor:", "")
        TM5_Common_Status = TM5_Common_Status.strip()
        print(TM5_Common_Status)

    if ("Status Date:" in thistxt):
        print("--Status Date is")
        Status_Date = thistxt.replace("Status Date:", "")
        Status_Date = Status_Date.strip()
        print(Status_Date)

    if ("Date Abandoned:" in thistxt):
        print("--Date Abandoned: is")
        Date_Abandoned = thistxt.replace("Date Abandoned:", "")
        Date_Abandoned = Date_Abandoned.strip()
        print(Date_Abandoned)

    if ("Publication Date:" in thistxt):
        print("--Publication Date is")
        Publication_Date = thistxt.replace("Publication Date:", "")
        Publication_Date = Publication_Date.strip()
        print(Publication_Date)

    try:
        keyis = row.find_element_by_xpath('./div[@class="key"]')
        thiskey = keyis.get_attribute('innerHTML')
        #print("key is")
        #print(thiskey)
        valsis = row.find_elements_by_xpath('div[@class="value"]')
        for valis in valsis:
            thisval = valis.get_attribute('innerHTML')
            # print("val is")
            # print(thisval)
            if ("International Class(es):" in thiskey):
                print("--international classes--")
                InterClass = thisval.strip()
                print(InterClass)
                thiskey = ""
            if ("Correspondent Name/Address:" in thiskey):
                print("--Correspondent Name/Address--")
                CorrespondentNameAdd = thisval.strip()
                CorrespondentNameAdd = CorrespondentNameAdd.replace("<div>", "")
                CorrespondentNameAdd = CorrespondentNameAdd.replace("</div>", "")
                CorrespondentNameAdd = (CorrespondentNameAdd.strip())
                print(CorrespondentNameAdd)
                thiskey = ""

            if ("Phone:" in thiskey):
                print("--phone no is")
                phone = thisval.strip()
                phone = (("(" + phone + ")"))
                print(phone)
                thiskey = ""

            if ("Legal Entity Type:" in thiskey):
                print("--Legal Entity Type is")
                Legal_Entity = thisval.strip()
                print(Legal_Entity)
                thiskey = ""

            if ("Owner Name:" in thiskey):
                print("--Correspondent Organization is")
                Owner_org = thisval.strip()
                print(Owner_org)
                thiskey = ""

            if ("Correspondent e-mail:" in thiskey):
                # print("This is email ")
                print(thisval)
                if thisval != "":
                    x = thisval.split("</a>")
                    finalmailis=""
                    counter = 0
                    for c in x:
                        # print("this is starting of c")
                        # print(c)
                        # print("this is ending of c")
                        brackpos = c.find(">")
                        mailis = (c[brackpos+1:]).strip()
                        if mailis != "" :
                            finalmailis = finalmailis +" | "+ (mailis)
                    finalmailis = (finalmailis[2:])
                    print("This is mail id")
                    mail_recipient = (finalmailis)   #for spliting mail in five var
                    # if mail_recipient.find("|"):
                    #     newval=mail_recipient.split("|")
                    #     for mailc in newval:
                    #
                    # print(mail_recipient)
                    # print("End of final mail is here")
                    break

                    # if (finalmailis.find("|"))!=0:
                    #     tomail = ""
                    #     finalmailis.split("|")
                    #     for ii in finalmailis:
                    #         if ii != 0:
                    #             tomail = ii
    except:
        pass

#print("in try condition")
driver.find_element_by_id("documentsTabBtn").click()
time.sleep(1)
page_src = driver.page_source
soup = BeautifulSoup(page_src, "html.parser")
#print("soup is")
#print(soup)
tableval = soup.find('table', {"class": "tablesorter"})
#print("This is")
#print(tableval)
thisvalue= soup.find_all("tr", {"class": "doc_row dataRowTR odd"})
for tr in thisvalue:
    #print("//////")
    #print(tr)
    finalval = tr.find_all("td",{"class": ""})
    # print("tr value")
    # print(finalval)
    # print("end of tr value")
    for e in finalval:
        # print("Testing")
        # print(e)
        print("end of testing")
        print(e.text[-4:])
        if (e.text[-4:]).isnumeric() == True:
            Mail_date = (e.text).strip()
            Mail_date = Mail_date.strip()
            print("Mail date is")
            print(Mail_date)
        else:
            doc_description = (e.text).strip()
            print("document name is")
            print(doc_description)
            break
            #print(e)
            # l = e.find("a", {"class": ""})
    break

docval = soup.find_all("tr")
for trval in docval:
    # print("in tr value is")
    # print(trval)
    if "Offc Action Outgoing" in (trval.text):
        #print("this is date tag")
        off_date = trval.find_all("td", {"class": ""})
        #print(trval)
        for dd in off_date:
            if (dd.text[-4:]).isnumeric() == True:
                OffAction_date = (dd.text).strip()
                print("Office action date is")
                print(OffAction_date)
                break
        # need to add break here
        print("End of date tag ")
        doclink = trval.find("a", {"class": ""})
        linkis = (doclink.get('href'))
        print("this is next page link")
        linkis = ("https://tsdr.uspto.gov/" + linkis)
        print(linkis)
        # Open document link
        driver.get(linkis)
        time.sleep(5)
        frame = driver.find_elements_by_xpath("//iframe[@id='docPage']")
        # switch the webdriver object to the iframe.
        driver.switch_to.frame(frame[0])
        page_src = driver.page_source
        soup = BeautifulSoup(page_src, "html.parser")
        # print(soup.text)
        sum_tag = soup.find_all("p", {"class": "MsoNormal"})
        summarycounter=0
        for tval in sum_tag:
            # print("this is t val")
            # print(tval)
            if "SUMMARY  OF ISSUES" in (tval.text) or "SUMMARY OF ISSUES" in (tval.text) :
                print("Summary val is")
                print(tval.text)
                summarycounter = 1
                break
        if summarycounter == 1:
            ulval = soup.find_all("ul")
            counter = 0
            for v in ulval:
                print(counter)
                print(v)
                counter = counter + 1
                break
            allli = v.find_all("li")
            sumvalue=""
            for c in allli:
                sumvalue = sumvalue +"\n"+ (c.text)
            print("Final list is value is ")
            f_sumvalue = sumvalue.strip()
            print(f_sumvalue)
        break

        # print ("this is final ul index  " + str(counter) )

    #         tdval = soup.findAll("td")
    #         counterval = 0
    #         for T in tdval:
    #             if counterval == 1:
    #                 print("This is mail recipent")
    #                 mail_recipient = (T.text).strip()
    #                 print(mail_recipient)
    #                 counterval = 0
    #
    #             if "To:" in (T.text):
    #                 counterval = 1
    #                 # print(T.text)
    #
    #             if counterval == 2:
    #                 print("This is mail CC")
    #                 mail_recipient_CC = (T.text).strip()
    #                 print(mail_recipient_CC)
    #                 counterval = 0
    #
    #             if "Cc:" in (T.text) or "Cc:" == (T.text):
    #                 print("in cc condition")
    #                 counterval = 2
    #                 # print(T.text)
    #
    #         # print("this is second page data")
    #         # print(soup)

driver.get("https://tsdr.uspto.gov")
time.sleep(1)
##
##writer.writerow(
##    {'Literal Element': LiteralElement, "Mark Type": MarkType, 'Serial': Serial, 'TSDR': TSDR,
##     "International Class(es)": InterClass, 'Filing Date': appfilingdate,
##     "Publication Date": Publication_Date, "Correspondent Name/Address": CorrespondentNameAdd,
##     "Correspondent Organization": Owner_org, "Correspondent Phone Number": phone
##        , "Legal Entity Type / Is Corporate Filer": Legal_Entity,
##     "TM5 Common Status / Alt Legal Status": TM5_Common_Status,
##     "Status Date / Alt Legal Status Date": Status_Date, "Date_Abandoned": Date_Abandoned, "Mail Date": Mail_date, "Latest Document Description": doc_description,"Summary of issues in latest office action":f_sumvalue,"Date of lastest office action" : OffAction_date, "E-Mail 1":mail_recipient,"E-Mail 2":"","E-Mail 3":"","E-Mail 4":"","E-Mail 5":""})

LiteralElement = "N/A"
MarkType = "N/A"
Serial = "N/A"
TSDR = "N/A"
InterClass = "N/A"
appfilingdate = "N/A"
Publication_Date = "N/A"
CorrespondentNameAdd = "N/A"
Owner_org = "N/A"
phone = "N/A"
Legal_Entity = "N/A"
TM5_Common_Status = "N/A"
Status_Date = "N/A"
Date_Abandoned = "N/A"
Mail_date = "N/A"
doc_description = "N/A"
mail_recipient = "N/A"
mail_recipient_CC = "N/A"
f_sumvalue = "N/A"
OffAction_date = "N/A"

