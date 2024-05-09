import requests
import time

# Function to print text with a delay between each letter
def print_with_delay(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to create an H&M membership account
def create_hm_membership_account(email, first_name, last_name, gender, postal_code, birth_date, password):
    url = 'https://www2.hm.com/en_us/register/newcustomer'
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-PH,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://www2.hm.com',
        'referer': 'https://www2.hm.com/en_us/register',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'dnt': '1',
        'priority': 'u=1, i',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'cookie': 'AKA_A2=A; bm_mi=DC0108C3148420BF1C246208A6D81982~YAAQFfAgFwFxphCPAQAA9qjaKRc7+68qb2O6mlcfFBzHIILExZHS0Fyjqs6+iSjqWrCYgrQKLI7NdkZucOlqU2ya4Wqt1zbVIHqF7PMIvm6mBXxXZ8wVj6+YXG2ZOu7+BW98yGm1aq35rZOJ5w0kHs6fT7UYgTlR5sRUMtpMBjfMkQc05Ey3KQlufGBAQUbRqcw9PwJ3IwVNXkbrSr8cGQ8NwZx61+W/RuWSdvjHZtyuInyoIlG3kL729DyV4pVtQKJITsp7iivrsFI/JyPyABNC7Q6V5oYTGjav2aSX0lfEXfILnGheuqXXYBW5gOPBJl2h2WLb5BH/C0VlHg==~1; HMCORP_locale=en_MO; INGRESSCOOKIE=1714394149.672.277.890179|495c85ead688f15d9d2c89bdc8134031; agCookie=7352e8d5-94a8-44c8-82bb-8681ebbe0995; hm-asia1-favourites=""; utag_main__sn=1; utag_main_ses_id=1714394153646%3Bexp-session; dep_sid=s_8531938601965960.1714394153663; utag_main_segment=normal%3Bexp-session; utag_main_cart_active=No%3Bexp-session; akavpau_www2_asia1=1714394457~id=67b66743c80e93f3abbb72d0d779f52c; akainst=AM; utag_main__ss=0%3Bexp-session; OptanonAlertBoxClosed=2024-04-29T12:36:38.137Z; hmid=5DEA8A6B-FA85-4B65-A46D-3AD828962838; _cs_mk_ga=0.5682086554528054_1714394201221; _ga=GA1.2.441625954.1714394202; _gid=GA1.2.1961115514.1714394202; _scid=f5ba1b18-5dcd-4d75-bb94-075bac04b3d3; _tt_enable_cookie=1; _ttp=APrODOCB4veFjCGIUL3lgFSBhCE; _pin_unauth=dWlkPVptSm1ZVFUwTjJFdE5qa3daQzAwT1RrMkxUaGtOemd0WkRjM056bGpPV1V4TkdGag; _cs_c=0; clubFullJoinCookie=##eyJkZWxheSI6NywiZGF0ZSI6MTcxNDk5OTA3NzE0MiwidXNlciI6InNhcm1pZW50b2x1aXNtYXJpbzJAZ21haWwuY29tIiwic3RhdHVzIjoiMiIsImNvdW50ZXIiOjAsIm1heENvdW50ZXIiOjJ9##; uuidCookie=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..n2qT2sATSXLT714IASr6XA.YVBqTtmEbC1TbHba0LhwJsb-2Q2z_GOZByExbhkfYCET0_8OAjSh_2sOz0JztRZiD-3TZv075B1-wg0JWggFQUx6PQL6uIDjeIGWINs-Hlsz25hrLOoXKjBufB2Orj7pzNF_WajfHTKaNrupOt9IRJMH30QUUB8gBit7pFO6ygCHwf0veWCp8vgjjWHnVzAwveDAe4Vg02yyHiOMJShjM3qb8i49wurqxk4mbIiKD_zCb5_MbgpCEGds9u-NKis0tLw_lWn1V9_6Cc4jdBsCX-oSmQIbibyeKdrn83K66Gg.kDKz3tbXV2zKwl1yWVMoqg; optimizelyEndUserId=oeu1714394302569r0.22615328774000343; WelcomeOfferABCookie=lca_welcome_offer_login_banner; utag_main_vapi_domain=hm.com; AMCVS_32B2238B555215F50A4C98A4%40AdobeOrg=1; s_ecid=MCMID%7C88248568378116905281907206323187485198; cpsegs=cpsegs%3D18391804%3B20212035; AMCV_32B2238B555215F50A4C98A4%40AdobeOrg=179643557%7CMCIDTS%7C19843%7CMCMID%7C88248568378116905281907206323187485198%7CMCAAMLH-1714999162%7C3%7CMCAAMB-1714999162%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1714401562s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-1848928539%7CvVersion%7C5.5.0; __attentive_id=b87efff54fb543febbe804280bf1e472; _attn_=eyJ1Ijoie1wiY29cIjoxNzE0Mzk0MzY0MzA2LFwidW9cIjoxNzE0Mzk0MzY0MzA2LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImI4N2VmZmY1NGZiNTQzZmViYmU4MDQyODBiZjFlNDcyXCJ9In0=; __attentive_cco=1714394364309; __attentive_ss_referrer=https://www2.hm.com/en_us/account?showOptIn=true; __attentive_dv=1; _sctr=1%7C1714320000000; ak_bmsc=399936949CC02A537C0990F65CDBD27E~000000000000000000000000000000~YAAQVK9qfC8JnR+PAQAAsenpKRcejZtmdZuaiLDVpEte1GpWNSGj2gl4NKUSIl+W/7k0HmfvrDB38oANLTn4dfNNduMT1Lee2vZOUby55qFvWYOGUWQvaWTO3Kl1bTAjgFEd1ZWt6pmLCA9Lkohx8WwGLGFDKfoU+9pOoL0047eCOSdHNnoT19MVHVi5ja02Kz963GASGblqR0VGURcb5qNopTNF39rW6boGKoOdFUsdd+zDUwclskNMYoPZRQWpkPX2xSHaoCRLa56Isxr9APGJRqAiNotfdmmUJcV2fubBga/wqqPNIg3aNwbJv0DURWqXyC78rd0BK5H2bhTMLRhUkHAvA8fIUNdwPPZlPXXnz2rG4IlO3RmNpgmR5OtRbd+EQTb8QhId5UYRy34EndONnBVbiiJw4PbaEujuzDABvtve+Z3kuROO6f+MEoGSLjz30SQL6UovnEf08oGVz3lGJyVhPz+oKqrp/rFyIW+A3T0YVNd+sUu1NRnSWRJXGYjZbyPaYyhCpGO079s=; utag_main__pn=13%3Bexp-session; JSESSIONID=A5D825F13A3C9756E20730436F933088657F660B0380384CDEC30B8C33323AED80FFCCD428F637BC104AC4A430F34E01CD959B36F7241B12584E006FC22ED94F.hybris-ecm-web-6bc645c756-6dflm; userCookie=##eyJjYXJ0Q291bnQiOjB9##; hm-us-favourites=""; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+29+2024+20%3A53%3A38+GMT%2B0800+(Philippine+Standard+Time)&version=202401.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=25ce346a-f0b6-4e88-bb62-e354feec3f84&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=PH%3B00; RT="z=1&dm=hm.com&si=46dbd958-c6b2-48e0-b845-499571d730ff&ss=lvky0c6k&sl=d&tt=2why&bcn=%2F%2F684d0d47.akstat.io%2F&obo=1&ld=n1e5"; _uetsid=22847110062511efbe624527557d87a3; _uetvid=22848e60062511efabb4f7a1ca9cc0c5; _scid_r=f5ba1b18-5dcd-4d75-bb94-075bac04b3d3; __attentive_pv=10; _ga_Z1370GPB5L=GS1.2.1714394280.1.1.1714395223.57.0.0; attntv_mstore_email=sarmientoluismario2@gmail.com:0; _gat_GA_GLOBAL=1; _gat_GA_LOCAL=1; akamref=en_us; akavpau_www2_en_us=1714395588~id=cf3eda38b146fee6a19c33a928137785; _abck=4D04290A767444F450966EFA6A53513D~0~YAAQnK9qfPCG2wiPAQAA4BLsKQtTS9o0WorsTLlKsRqzwiW6+iIf2ndGGNwLkYcaa0hQhqYhigDjuBoBn6bOTQ7dqDNx9ZHegDClWPBFo+X1TfhXLctH0Q0K1nxc/xYrmQFak4tEN9vHEG5IwXVjqKn5uWvQLfEqcwFFCPV8Yn1Ah6xu4Zwns5CZs+lYy6+iRwjxS/VPSjp+FxEvwbFg1Y7ae+PryRWJk+7b/8nSBT4XLy6l1KrLVKxhW/O/0gRnNs5GvfuiMrNEBpaM7vlokUbqbwWKRw8ZTHesZqWtgBYvz8qDEGrMxAOhqMZrg83P1nIZyUn7zpP69vdjDPcRygYfaykj3AqBpvJFmY1ei+i6+l3tWLIMQjRSd17838cgsxXU0M7y5zDr374/BVZJyPuRFaA=~-1~-1~1714398838; bm_sv=9C598FDDD54AC81AD25CC86FBB103C8F~YAAQnK9qfPGG2wiPAQAA4BLsKReRJCpOVXO8tud19RuiJPUbxnxj8+l7zWFVDxmAd/Cl4spMcF9GruG8E1ohYNVSqktUyQAImdLvNYAF80auZUaaFvAQ1EZvMrAdmG0qdLzxZmw/5PGBX4sO/vDodTxykjMFNud6xc0FWSZs3CErx+clThPyyYk01JdyzUnI5Vqd43zj/Iak2EUioQjKtBQLyRBc9n32s00j4uwo/GmQyHeEVn6wPlv6XV3M~1; _gcl_au=1.1.187019544.1714394277.1973654922.1714394279.1714395289; utag_main__se=48%3Bexp-session; utag_main__st=1714397096151%3Bexp-session; dep_exp=Thu, 27 June 2024 13:24:56 GMT; _cs_id=81b2f312-0ffe-ae58-8c58-db2ceef02f36.1714394203.1.1714395296.1714394203.1671006191.1748558203806.1; _cs_s=12.0.0.1714397096201',
    
    }
    data = {
        "email": email,
        "firstName": first_name,
        "lastName": last_name,
        "gender": gender,
        "postalCode": postal_code,
        "hmNewsSubscription": True,
        "birthDate": birth_date,
        "pwd": password,
        "year": birth_date[:4],
        "month": birth_date[5:7],
        "day": birth_date[8:10],
        "hmClubJoin": True,
        "termsAndCondition": True,
        
    }
    response = requests.post(url, headers=headers, json=data)
    return response

# Simulating the process of creating an H&M membership account
print_with_delay("Welcome to H&M Membership Account Creation")
print_with_delay("-----------------------------------------\n")

time.sleep(1)

print_with_delay("Step 1: Provide Personal Information")
time.sleep(1)
email = input("Enter your email: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
gender = input("Enter your gender: ")
postal_code = input("Enter your postal code: ")
birth_date = input("Enter your birth date (YYYY-MM-DD): ")

print("\nProcessing...\n")
time.sleep(2)

print_with_delay("\nStep 2: Create Your Password")
time.sleep(1)
password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")

print("\nProcessing...\n")
time.sleep(2)

print_with_delay("\nStep 3: Join H&M Club")
time.sleep(1)

print("\nJoining H&M Club...")
time.sleep(2)

# Create H&M membership account
response = create_hm_membership_account(email, first_name, last_name, gender, postal_code, birth_date, password)

if response.status_code == 200:
    print("\nCongratulations! Your H&M Membership Account has been successfully created!")
else:
    print("\nAn error occurred while creating your account or Email Exist. Please try again later.")
