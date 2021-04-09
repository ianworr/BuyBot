def email(urll):
    if urll == 'www.amazon.com':
        return ''# enter email for this site
    elif urll == 'www.bestbuy.com':
        return ''# enter email for this site
    elif urll == 'www.target.com':
        return ''# enter email for this site
    else:
        return ''# enter email for this site

def password(urll):
    if urll == 'www.amazon.com':
        return ''# enter password for this site
    elif urll == 'www.bestbuy.com':
        return ''# enter password for this site
    elif urll == 'mail.google.com':
        return ''# enter password for this site
    elif urll == 'www.walmart.com':
        return ''# enter password for this site
    elif urll == 'www.gamestop.com':
        return ''# enter password for this site   
    elif urll == 'www.target.com':
        return ''# enter password for this site
    else:
        return ''# enter password for this site

def cardinf(inf):
    if inf == 'card':
        return # enter card number
    elif inf == 'cvv':
        return # enter cvv
    elif inf == 'date':
        return # enter date like: 0210 (ddmm)
    elif inf == 'zip':
        return # enter zip
    elif inf == 'add1':
        return # enter address line 1
    elif inf == 'add2':
        return # enter address line 2
    elif inf == 'city':
        return # city


def urlz(num):
    testsite = 'https://www.bestbuy.com/site/keurig-k-slim-single-serve-k-cup-pod-coffee-maker-black/6397760.p?skuId=6397760'
    bbps5site = 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161'
    bbps5dsite = 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149'
    bbrtx3080 = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
    bbrtx3070 = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'
    bbrtx3060 = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
    bbxboxx = 'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324'
    azps5site =  'https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62?ref_=ast_sto_dp'
    azps5dsite = 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp'
    wmps5site = 'https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815'
    wmps5dsite = 'https://www.walmart.com/ip/PlayStation-5-Console/363472942'
    gmps5site = 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html'
    gmps5dsite = 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html'
    gmps5bundle1site = 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-action-collection-system-bundle-with-20-gamestop-gift-card/B225170G.html'
    gmps5bundle2site = 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition-with-ps-plus-system-bundle-with-20-gamestop-gift-card/B225171T.html'
    tgps5site = 'https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596#lnk=sametab'
    tgps5dsite = 'https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab'
    aops5bundle = 'https://www.antonline.com/Sony/Electronics/Gaming_Devices/Gaming_Consoles/1421247'
    asdf = 'https://www.walmart.com/ip/PowerA-Wired-Controller-for-Xbox-One-Black/362568419'
    sites = [testsite, bbps5site, bbps5dsite, azps5site, azps5dsite, wmps5site, wmps5dsite, gmps5site, gmps5dsite, gmps5bundle1site, gmps5bundle2site, aops5bundle, asdf]
    if num == False:
        sites = [
            bbps5dsite,
            bbxboxx,
            bbrtx3080,
            azps5dsite,
            wmps5dsite#,
            #gmps5dsite,
            #tgps5dsite,
            #aops5bundle,
            ]
        #sites = [bbps5dsite, bbxboxx]
    else:
        sites = [
            testsite,
            # bbps5site,
            # bbps5dsite,
            # azps5site,
            # azps5dsite,
            # wmps5site,
            # wmps5dsite,
            # gmps5site,
            # gmps5dsite,
            # gmps5bundle1site,
            # gmps5bundle2site,
            # aops5bundle,
            asdf
            ]

    # domin = []
    # for n in range(len(sites)):
        
    #   domin.append(sites[n].split('/')[2])
    # if num == True:
    #   return sites[num],domin[num]
    # else:
    return sites#,domin

def paths(urll):
    # get xpaths and other information specific to each site
    addtocrtbtn2 = ''
    qtyval = '2' # number you would like to buy if allowed more than 1
    cardinp = ''
    expinp = ''
    zipinf = ''
    cpchid = ''
    #purcontBtn = ''
    if urll == 'www.amazon.com':
        loginpage       = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'
        addtocrtbtn     = ''
        crt             = 'gp/cart/view.html/ref=lh_'   
        qtyxp           = '/html/body/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[4]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/span[1]/span/select'
        checkoutxpath   = '/html/body/div[1]/div[4]/div[1]/div[3]/div/div[1]/div[2]/div/form/div/div[3]/span/span/input'
        checkoutxpath2  = '/html/body/div[1]/div[4]/div[1]/div[7]/div/div[1]/div[2]/div/form/div/div[3]/span/span/input'
        emailid         = 'ap_email'
        passwid         = 'ap_password'
        continueid      = 'continue'
        loginid         = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input'
        purchacebtn     = '/html/body/div[5]/div[1]/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span'
        purcont         = '/html/body/div[5]/div/div/div[2]/table/tbody/tr/td/div/form/div/div/div[1]/div[2]/a'
        sndto           = ''
        revorder        = ''
        cvvinput        = '/html/body/div[5]/div[1]/div[2]/form/div/div/div/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/input[1]'
        passwid2        = ''
        #/html/body/div[1]/div[4]/div[1]/div[7]/div/div[1]/div[2]/div/form/div/div[3]/span/span/input
    elif urll == 'www.bestbuy.com':
        loginpage = 'https://www.bestbuy.com/identity/signin?token=tid%3Ad7de314c-8b41-11eb-875a-0edcc4f1498f'
        addtocrtbtn = ''
        crt = ''
        checkoutxpath = "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button"
        checkoutxpath2 = ''
        qtyxp = "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[3]/div/select"
        emailid = 'fld-e'
        passwid = 'fld-p1'
        continueid = ''
        loginid = '/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button'
        purchacebtn = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/button'
        purcont = ''
        sndto = ''
        revorder = ''
        cvvinput = '/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/input'
        passwid2 = ''
        #/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]/div/input
    elif urll == 'www.walmart.com':
        loginpage = 'https://www.walmart.com/account/login?tid=0&returnUrl=%2Fsearch%2F%3Fquery%3Dps5'
        addtocrtbtn = '/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div[5]/div/div[3]/div/div[2]/div[2]/div[1]/section/div[1]/div[3]/button'
        crt = ''
        checkoutxpath = "/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/button[1]"
        checkoutxpath2 = ''
        qtyxp = "/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/div/div/select"
        emailid = 'email'
        passwid = 'password'#'sign-in-password-no-otp'
        #sign-in-password-no-otp
        continueid = ''
        loginid = '/html/body/div[1]/div/div[2]/form[1]/button[1]'
        purchacebtn = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button'
        purcont = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[3]/button'
        sndto = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div[2]/button'
        revorder = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/button'
        cvvinput = '/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div[3]/div[2]/div/div/div/div[1]/div/input'
        passwid2 = 'sign-in-password-no-otp'
        #add-on-atc-container > div:nth-child(1) > section > div.valign-middle.display-inline-block.prod-product-primary-cta.primaryProductCTA-marker > div.prod-product-cta-add-to-cart.display-inline-block > button > span > span
    elif urll == 'www.gamestop.com':    
        loginpage = ''
        addtocrtbtn = '/html/body/div[6]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[8]/div[3]/div/div[1]/button'
        crt = ''
        checkoutxpath = '/html/body/div[7]/div[6]/div[1]/div[2]/div[5]/div[2]/div/a'
        checkoutxpath2 = ''
        qtyxp = '/html/body/div[7]/div[6]/div[1]/div[1]/div[1]/div[3]/div/div/div/div[3]/div/div[1]/div[1]/div/div[2]'
        emailid = 'login-form-email'
        passwid = 'login-form-password'
        continueid = ''
        loginid = ''
        purchacebtn = '/html/body/div[7]/div[1]/div[1]/div[1]/div[8]/div/div/div/div[11]/form/button'
        purcont = ''
        sndto = '/html/body/div[7]/div[1]/div[2]/div/div/div/button[1]'
        revorder = '/html/body/div[7]/div[1]/div[1]/div[1]/div[8]/div/div/div/div[11]/button[2]'
        cvvinput = '/html/body/div[7]/div[1]/div[1]/div[1]/div[5]/div[2]/div/form/fieldset[3]/div/div[2]/ul/li[1]/div/div/div/div/div[1]/div[1]/div[1]/div/div/input'
        passwid2 = ''
    elif urll == 'www.target.com':  
        loginpage = ''
        addtocrtbtn = '/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div[1]/div/div[1]/div[2]/button'
        #               '/html/body/div[1]/div/div[4]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/button'
        crt = 'co-'
        checkoutxpath = '/html/body/div[1]/div/div[4]/div[1]/div[2]/div/div/div/div[2]/button'
        checkoutxpath2 = '/html/body/div[14]/div/div/div[1]/div/div[2]/div/form/button'
        qtyxp = '/html/body/div[1]/div/div[4]/div[1]/div[1]/div[2]/div[8]/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/select'
        emailid = 'username'
        passwid = 'password'
        continueid = ''
        loginid = ''
        purchacebtn = '/html/body/div[1]/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div/button'
        purcont = ''
        sndto = ''
        revorder = '/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/button'
        cvvinput = '/html/body/div[1]/div/div[3]/div[1]/div[1]/div/div/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div/form/div/div[1]/div/input'
        passwid2 = '/html/body/div[14]/div/div/div[1]/div/div[2]/div/form/div[2]/input'
        qtyval = '1'
        
    elif urll == 'www.antonline.com':   
        loginpage = ''
        addtocrtbtn = '/html/body/div[4]/div[2]/button'
        addtocrtbtn2 = '/html/body/b/div[3]/div/div[2]/div/div/button[1]'
        crt = ''
        checkoutxpath = '/html/body/div[3]/div[5]/div[3]/div/form/div[1]/div/div[1]/div[5]/div[4]/div/div[1]'
        checkoutxpath2 = ''
        qtyxp = '/html/body/div[3]/form/div[1]/div/div/div/div/div[2]/div/div/p[2]/input'
        emailid = 'bemail'
        passwid = ''
        continueid = ''
        loginid = ''
        purchacebtn = '/html/body/div[3]/div[5]/div[3]/div/form/button[1]'
        purcont = ''
        sndto           = ''
        revorder        = ''
        cvvinput        = '//*[@id="cvv"]'
        passwid2        = ''
        qtyval          = '1'
        cpchid          = 'checkbox-label'
        cardinp         = '//*[@id="credit-card-number"]'
        expinp          = '//*[@id="expiration"]'
        zipinf          = 'bzip'#'//*[@id="postal-code"]'


    return [
        loginpage,
        addtocrtbtn,
        addtocrtbtn2,
        crt,
        qtyxp,
        qtyval,
        checkoutxpath,
        checkoutxpath2,
        emailid,
        continueid,
        passwid,
        passwid2,
        loginid,
        purcont,
        sndto,
        cvvinput,
        cpchid,
        cardinp,
        expinp,
        zipinf,
        revorder,
        purchacebtn   
        ]