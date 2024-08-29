from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def crawl_news(keyword, page_number):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    url = "https://www.dnews.co.kr/"
    results = []  # 결과를 저장할 배열

    driver.get(url)

    try:
        driver.switch_to.frame("startmain")  # 현재 위치를 frame으로 전환

        # 검색어 입력 및 검색
        search_button = driver.find_element(By.CLASS_NAME, "btn_search")
        search_button.click()

        search_input = driver.find_element(By.NAME, "query")
        search_input.send_keys(keyword)
        search_input.send_keys('\n')

        # 페이지 이동 및 데이터 추출
        for page in range(page_number):
            try:
                page_links = driver.find_elements(By.CSS_SELECTOR, "span.number a")

                if page >= len(page_links):
                    print("입력한 페이지 번호가 범위를 벗어났습니다.")
                    break

                page_links[page].click()
                time.sleep(2)  # 페이지 로드 시간

                news_zone = driver.find_element(By.CLASS_NAME, "newsZone")   # 뉴스 목록의 부모 클래스 가져오기
                img_use_elements = news_zone.find_elements(By.TAG_NAME, "li")

                for element in img_use_elements:
                    href = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                    title = element.find_element(By.CLASS_NAME, "title").text.strip()
                    news_date = element.find_element(By.CLASS_NAME, "news_date").text.strip()

                    results.append({
                        'title': title,
                        'link': href,
                        'date': news_date
                    })

            except Exception as e:
                print(f"페이지 {page + 1} 처리 중 오류 발생: {e}")
                continue

        driver.switch_to.default_content()

    except Exception as e:
        print('오류 발생:', e)
    finally:
        driver.quit()

    return results
