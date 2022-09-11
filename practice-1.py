# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# # options.add_argument("--no-sandbox")
# # options.add_argument("--disable-dev-shm-usage")

# # ---이 두 줄은 replit에서 동작시키기위한 것이다.

# browser = webdriver.Chrome(options=options)

# browser.get("https://www.indeed.com/jobs?q=python&limit=50")

# print(browser.page_source)

# #indeed가 request를 막고 있어서 request를 사용하지 않음.
# #webdriver를 selenum에서 import하고 selenium webdriver chrome options에서 options를 import함.
# # selenium이 indeed를 브라우저로 열어줌.

# # replit에서 사용하며 아래의 코드를 replit.nix파일에 추가해야함.

# # {pskgs}:{
# # deps=[
# # pkgs.python38Full
# # ---여기애---]}
# # pkgs.chromium
# # pkgs.chromedriver
# # 입력!!