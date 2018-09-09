from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


Type_of_service = input("\n\nNormal_service  ======== [1]\nRBT_service  =========== [2]\nRRBT_Service  ========== [3]\nEvenTrigger_service  === [4]\nTrynBuy_Service  ======= [5]\nEventCharging service == [6]\nNetwork Service ======== [7]\n\nEnter any one type of service .......\n")
sname = input("Enter service name :: \n")
Billing=sname.replace('_','').replace('@','').replace('!','').replace('%','').replace('#','').replace('$','').replace('^','').replace('&','').replace('*','').replace('-','').replace('-','').replace('+','').replace('|','').replace(':','').replace(';','')

if Type_of_service == "2":
    cpid = input("Enter the CP \nRealNetwork === [1]\nOnmobile ===[2]\n")

elif Type_of_service == "3":
    cpid = input("Enter the CP \nRealNetwork === [1]\nOnmobile ===[2]\n")

elif Type_of_service == "4":
    Trigger_service= input("Enter the trigger service::\n")

elif Type_of_service == "6":
    charging_event= input("Enter the Charging Event::\n")

elif Type_of_service =="7":
    Netowrk_service= input("Select one Network service\n\nRBT ====== [1]\nRRBT ===== [2]\nMCA ====== [3]\nPRETONE == [4]\nSC ======= [5]\n\n\n")


d = webdriver.Firefox()
baseurl = "https://ideasit.gui.ibmse.com:6005/users/login.html"
d.get(baseurl)

a = d.find_element(By.XPATH, "//input[@name='USuser']")
a.send_keys("ibmse_user2")

b = d.find_element(By.XPATH, "//input[@name='Password']")
b.send_keys("Fkdyk74r")

c = d.find_element(By.XPATH, "// input[ @ name = 'Submit']")
c.click()

print("Logged in successfully")

parentHandle = d.current_window_handle
print("Parent Handle: " + parentHandle)
start_time = time.time()

servicedashboard = d.find_element(By.XPATH,"/ html / body / table[2] / tbody / tr[1] / td[1] / table[2] / tbody / tr[41] / td / font / b / a")
servicedashboard.click()

d.switch_to.frame("homeFrame")

time.sleep(2)

i = d.find_element(By.XPATH, "//a[contains(text(),'Create Combo')]")
i.click()
time.sleep(1)






class Service_creation():

    def test1(self):

        handles = d.window_handles
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                d.switch_to.window(handle)
                print("switched to window ::" + handle)
                Handle = d.current_window_handle
                stype = d.find_element(By.XPATH, "//select[@class='gwt-ListBox']")

                if Type_of_service == ("1","4","5","6"):
                    sel = Select(stype)
                    sel.select_by_visible_text("Single")

                elif Type_of_service == "2":
                    sel = Select(stype)
                    sel.select_by_visible_text("Combo4-RBT")

                elif Type_of_service == "3":
                    sel = Select(stype)
                    sel.select_by_visible_text("Combo4-RRBT")
                elif Type_of_service == "7":
                    if Netowrk_service== ("3","4","5"):
                        sel = Select(stype)
                        sel.select_by_visible_text("Single")
                    elif Netowrk_service== "1":
                        sel = Select(stype)
                        sel.select_by_visible_text("Combo4-RBT")

                    elif Netowrk_service== "2":
                        sel = Select(stype)
                        sel.select_by_visible_text("Combo4-RRBT")




                time.sleep(1)
                next = d.find_element(By.XPATH, "//a[@class='gwt-Anchor']")
                next.click()
                time.sleep(2)
                break
        newhandle = d.window_handles
        for new in newhandle:
            print("new :" + new)
            if new not in (parentHandle, Handle):
                d.switch_to.window(new)
                print("Switched to window ::" + new)
                break






    def test4(self):

        service_name = d.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input")

        service_name.send_keys(sname)

        service_code = d.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/input")
        service_code.send_keys("1234")
        # time.sleep(2)

        service_desc = d.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[4]/td[2]/textarea")
        service_desc.send_keys("Test Service")
        # time.sleep(5)

        date = d.find_element(By.XPATH, "//input[@class='gwt-DateBox gwt-DateBox-readonly']")
        date.click()
        # time.sleep(2)

        date = d.find_element(By.CSS_SELECTOR, ".datePickerDayIsToday")
        date.click()
        # time.sleep(2)
        print("Date selected")

        if Type_of_service =="2":

            if cpid == "1":

                # d.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/select").click()
                CP = d.find_element(By.XPATH,
                                    "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/select")
                ccpp = Select(CP)
                ccpp.select_by_value("B5")

            elif cpid == "2":
                CP = d.find_element(By.XPATH,
                                    "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/select")
                ccpp = Select(CP)
                ccpp.select_by_value("03")

        if Type_of_service =="3":

            if cpid == "1":

                # d.find_element_by_xpath("/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/select").click()
                CP = d.find_element(By.XPATH,
                                    "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/select")
                ccpp = Select(CP)
                ccpp.select_by_value("B5")

            elif cpid == "2":
                CP = d.find_element(By.XPATH,
                                    "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/select")
                ccpp = Select(CP)
                ccpp.select_by_value("03")

        validity = d.find_element(By.XPATH, "//input[@id='gwt-uid-2']")
        validity.click()

        mail = d.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input")
        mail.click
        mail.send_keys("viki@gmail.com")

        msisdn = d.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/input")
        msisdn.click()
        msisdn.send_keys("9000000000")

        if Type_of_service== "3":
            usage_type = d.find_element(By.XPATH,
                                        "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select")

            utype = Select(usage_type)
            utype.select_by_visible_text("RRBT")

        elif Type_of_service== "7":

            SUsage_type = d.find_element(By.XPATH, "//option[@value='Other']")
            SUsage_type.click()

            #utype = Select(usage_type)

            usage_type = d.find_element(By.XPATH,
                                        "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/select")
            # time.sleep(3)
            utype = Select(usage_type)

            if Netowrk_service=="2":
                utype.select_by_visible_text("RRBT")

            elif Netowrk_service=="3":
                utype.select_by_visible_text("MCA")
            elif Netowrk_service=="4":
                utype.select_by_visible_text("PRETONE")
            elif Netowrk_service=="5":
                utype.select_by_visible_text("SC")

            # if Netowrk_service=="1":
            #     utype.select_by_visible_text("RBT")






        radio = d.find_element(By.XPATH, "// input[ @ id = 'gwt-uid-4']")
        radio.click()

        uup1 = d.find_element(By.XPATH, "// input[ @ id = 'gwt-uid-6']")
        uup1.click()

        uup2 = d.find_element(By.XPATH, "// input[ @ id = 'gwt-uid-7']")
        uup2.click()

        uup3 = d.find_element(By.XPATH, "// input[ @ id = 'gwt-uid-8']")
        uup3.click()

        Next = d.find_element(By.XPATH, "// button[ @ type = 'button'][contains(text(), 'Next >>')]")
        Next.click()
        # time.sleep(2)

        Active = d.find_element(By.XPATH, "// option[ @ value = '1'][contains(text(), 'ACTIVE')]")
        Active.click()
        # time.sleep(2)

        shortcode = d.find_element(By.XPATH, "//*[@name='AL_sc_0']")
        shortcode.click()
        shortcode.send_keys("5196162")
        # time.sleep(2)

        keyword = d.find_element(By.XPATH, "//*[@name= 'AL_kw_0']")
        keyword.click()
        keyword.send_keys(sname)
        # time.sleep(2)

        billing = d.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td/table/tbody/tr[5]/td[2]/input")
        billing.click()
        billing.send_keys(Billing)




    def test5(self):

        fetch = d.find_element(By.XPATH, "//option[@value='2'][contains(text(),'By CP')]")
        fetch.click()
        # time.sleep(2)

    def test6(self):
        trigger = d.find_element(By.XPATH, ".//*[@id='gwt-uid-11']")
        trigger.click()

        event_name = d.find_element(By.XPATH,
                                    "//table[@class='gwt-DecoratedTabPanel']//table//td//div//td//table//td//tbody//tr[2]//td[1]//table[1]//tbody[1]//tr[1]//td[2]//input[1]")
        event_name.click()
        event_name.send_keys(Trigger_service)

        trig_act = d.find_element(By.XPATH,
                                  "/html/body/div[1]/div[4]/div/div/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/table/tbody/tr/td/table/tbody/tr/td[1]/select")
        tri = Select(trig_act)

        tri.select_by_value("2")

    def test7(self):

        DOD = d.find_element(By.XPATH, "// *[ @ id = 'gwt-uid-22']")
        DOD.click()
        # time.sleep(2)

        act = d.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[6]/td[1]/table[1]/tbody[1]/tr[5]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/select[1]")
        sel = Select(act)
        # time.sleep(2)

        sel.select_by_value("2")
        # time.sleep(2)

        ren = d.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[7]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[5]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/select[1]")
        vel = Select(ren)
        vel.select_by_value("2")


    def chargig(self):

        Charging_name = d.find_element(By.XPATH,
                                       "//tbody//tr[10]//td[1]//table[1]//tbody[1]//tr[2]//td[1]//table[1]//tbody[1]//tr[1]//td[2]//input[1]")
        Charging_name.click()
        Charging_name.send_keys(charging_event)
        chg_act = d.find_element(By.XPATH,
                                 "//tbody//tr[10]//td[1]//table[1]//tbody[1]//tr[2]//td[1]//table[1]//tbody[1]//tr[1]//td[4]//table[1]//tbody[1]//tr[1]//td[1]//select[1]")
        chg = Select(chg_act)
        chg.select_by_value("2")
        time.sleep(2)

    def test8(self):

        tryandbuy = d.find_element(By.XPATH, "//tbody//tr[12]//td[1]//table[1]//tbody[1]//tr[2]//td[2]//select[1]")
        tryvalidity = Select(tryandbuy)
        tryvalidity.select_by_value("2")

        tryoptin = d.find_element(By.XPATH, "//*[@id='gwt-uid-24']")
        tryoptin.click()

    def provisioning(self):
        if Netowrk_service== "1":
            prov = d.find_element(By.XPATH, "//label[(text() = 'RBT')]")
            prov.click()
            time.sleep(2)
        elif Netowrk_service== "2":
            prov = d.find_element(By.XPATH, "//label[(text() = 'RRBT')]")
            prov.click()
            time.sleep(2)
        elif Netowrk_service== "3":

            prov = d.find_element(By.XPATH, "//label[(text() = 'MCA')]")
            prov.click()
            time.sleep(2)
        elif Netowrk_service== "4":
            prov = d.find_element(By.XPATH, "//label[(text() = 'PreTone')]")
            prov.click()
            time.sleep(2)
        elif Netowrk_service== "5":
            prov = d.find_element(By.XPATH, "//label[(text() = 'SC')]")
            prov.click()
            time.sleep(2)

        d.find_element_by_xpath("//button[contains(text(),'Ok')]").click()




    def test9(self):



        if Type_of_service =="2":
            if cpid == "1":

                d.find_element_by_xpath("//option[(text()='RealNetwork_RealNetwork')]").click()
                time.sleep(2)
                d.find_element_by_xpath("//button[@type='button'][contains(text(),'Ok')]").click()

            elif cpid == "2":
                d.find_element_by_xpath("//option[(text()='Phonytunes_delhi')]").click()
                time.sleep(2)
                d.find_element_by_xpath("//button[@type='button'][contains(text(),'Ok')]").click()

        elif Type_of_service =="3":
            if cpid == "1":

                d.find_element_by_xpath("//option[(text()='RealNetwork_RealNetwork')]").click()
                time.sleep(2)
                d.find_element_by_xpath("//button[@type='button'][contains(text(),'Ok')]").click()

            elif cpid == "2":
                d.find_element_by_xpath("//option[(text()='Phonytunes_delhi')]").click()
                time.sleep(2)
                d.find_element_by_xpath("//button[@type='button'][contains(text(),'Ok')]").click()

        elif Type_of_service != "2" or "3":
            CPa = d.find_element(By.XPATH, "//option[@value='129'][contains(text(),'AccessMobile_accessmobile')]")
            CPa.click()
            time.sleep(2)
            d.find_element_by_xpath("//button[@type='button'][contains(text(),'Ok')]").click()










        CS = d.find_element(By.XPATH, "// button[ @ type = 'button'][contains(text(), 'Create Service')]")
        CS.click()
        #time.sleep(2)

        done = d.find_element(By.XPATH, "//table[@class='FlexTable']//tbody//tr//td//table//tbody//tr//td//button[@type='button'][contains(text(),'Create')]")
        done.click()
        time.sleep(15)

        alert1 = d.switch_to.alert
        alert1.accept()
        #time.sleep(2)

        d.switch_to.window(parentHandle)
        d.switch_to.default_content()


        #time.sleep(3)

        e = d.find_element(By.XPATH, "//img[@src='/users/images/logout.gif']")
        e.click()

        end_time = time.time()
        print("Time Taken = ", end_time - start_time, "sec")



ff = Service_creation()

if Type_of_service == "1":
    ff.test1()
    ff.test4()
    ff.test5()
    ff.test7()
    ff.test9()

elif Type_of_service == "2":
    ff.test1()
    ff.test4()
    ff.test7()
    ff.test9()
elif Type_of_service == "3":
    ff.test1()
    ff.test4()
    ff.test7()
    ff.test9()

elif Type_of_service == "4":
    ff.test1()
    ff.test4()
    ff.test5()
    ff.test6()
    ff.test7()
    ff.test9()

elif Type_of_service == "5":
    ff.test1()
    ff.test4()
    ff.test5()
    ff.test7()
    ff.test8()
    ff.test9()

elif Type_of_service == "6":
    ff.test1()
    ff.test4()
    ff.test5()
    ff.test7()
    ff.chargig()
    ff.test9()

elif Type_of_service =="7":
    if Netowrk_service== "1":
        ff.test1()
        ff.test4()
        ff.test7()
        ff.provisioning()
        ff.test9()
    elif Netowrk_service== "2":
        ff.test1()
        ff.test4()
        ff.test7()
        ff.provisioning()
        ff.test9()
    elif Netowrk_service== "3":
        ff.test1()
        ff.test4()
        ff.test7()
        ff.provisioning()
        ff.test9()
    elif Netowrk_service== "4":
        ff.test1()
        ff.test4()
        ff.test7()
        ff.provisioning()
        ff.test9()
    elif Netowrk_service== "5":
        ff.test1()
        ff.test4()
        ff.test7()
        ff.provisioning()
        ff.test9()





d.quit()






