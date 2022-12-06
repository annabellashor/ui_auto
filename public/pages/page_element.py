# coding=utf-8



class Page_elem(object):
    username=["id","userAccount"]
    password=["name","loginPwd"]
    loginbtn=["xpath",'//*[@id="loginBtn"]']
    user_center=["xpath",'//*[@id="menu-user"]/dt']
    user_manage=["xpath",'//*[@id="menu-user"]/dd/ul/li[1]/a']
    iframe_box=["xpath",'//*[@id="iframe_box"]/div[2]/iframe']
    adduser=["xpath",'/html/body/div/div[2]/span[1]/a[2]']
    iframe1=['xpath','//*[@id="xubox_iframe1"]']
    userName=['xpath','//*[@id="userName"]']
    sex_nv=['xpath','/html/body/div/div/form/table/tbody/tr[2]/td/label[2]/input']
    user_email=['id','user-email']
    userAccount=['id','userAccount']
    loginPwd=['id','loginPwd']
    submitBtn=['id','submitBtn']
    confirmPwd=['id','confirmPwd']
    user_tel=['id','user-tel']
    searchValue=['id','searchValue']
    searchBtn=['id','searchBtn']
p=Page_elem()


