# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs #다른 웹페이지로 설정되어 있으므로 여기서는 사용하지 못함. 구도를 맞추기 위함이니 참고만하기! 원래는 두개의 extract가 같은 키를 사용(여기서는 'job data' 요소들)해서 딕셔너리를 만들고 있어야함.
# from file import save_to_file

# keyword  = input("What do you want to search for?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)

# jobs = indeed + wwr

# save_to_file(keyword,jobs)

# #여기까지가 webscrapper