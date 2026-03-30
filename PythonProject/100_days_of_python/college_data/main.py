import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# --- 1. SETUP ---
chrome_options = Options()
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.google.com/search?q=list+of+engineering+colleges+in+thanjavur&udm=1&sxsrf=ANbL-n6B1ughpFqeuJukFBkf1yKDeTky8g:1771991147021&start=20"
driver.get(url)
college_data = []


def scrape_page():
    # Find all college blocks
    listings = driver.find_elements(By.CLASS_NAME, 'VkpGBb')

    for listing in listings:
        name, address, phone = "N/A", "N/A", "N/A"
        try:
            # --- 2. INTERACTION ---
            # Click the listing to open the sidebar
            click_target = listing.find_element(By.CSS_SELECTOR, 'a.vwVdIc')
            driver.execute_script("arguments[0].click();", click_target)
            sleep(5)

            # Name is safely taken from the list view
            name = listing.find_element(By.CLASS_NAME, "OSrXXb").text

            # --- 3. EXTRACTION FROM SIDEBAR ---
            try:
                # Wait for sidebar to load content
                sidebar = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.qsMfcd"))
                )
                sidebar_text = sidebar.text

                # Try finding address by specific Google class
                try:
                    address = sidebar.find_element(By.CSS_SELECTOR, "span.LrzXr").text
                except:
                    pass

                # Try finding phone by specific Google class or attribute
                try:
                    phone = sidebar.find_element(By.CSS_SELECTOR, "span.LrzXr.kno-fv, [data-dtype='dphone']").text
                except:
                    # REGEX FALLBACK: Look for a phone pattern in the sidebar text if tags fail
                    # Matches patterns like 0422 236 7890 or +91 98765 43210
                    phone_match = re.search(r'(\+?\d[\d\s-]{8,15}\d)', sidebar_text)
                    if phone_match:
                        phone = phone_match.group(1).strip()

            except Exception as e:
                print(f"Sidebar not found for {name}, moving to fallback.")

            # --- 4. FALLBACK TO LIST TEXT (If sidebar extraction failed) ---
            if address == "N/A" or phone == "N/A":
                try:
                    details = listing.find_element(By.CLASS_NAME, "rllt__details")
                    # Usually the 3rd div contains 'Address · Phone'
                    info_line = details.find_elements(By.TAG_NAME, "div")[2].text
                    if "·" in info_line:
                        parts = info_line.split("·")
                        if address == "N/A": address = parts[0].strip()
                        if phone == "N/A": phone = parts[1].strip()
                except:
                    pass

            # --- 5. FINALIZE ---
            college_data.append({"Name": name, "Address": address, "Contact": phone})
            print(f"Scraped: {name}")
            sleep(10)

        except Exception as e:
            print(f"Error processing listing: {e}")


# --- 6. PAGINATION LOOP ---
for page in range(3):
    print(f"--- Scraping Page {page + 1} ---")
    scrape_page()
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "pnnext"))
        )
        next_button.click()
        time.sleep(5)  # Allow page to settle
    except:
        print("No more pages.")
        break

# --- 7. EXPORT ---
df = pd.DataFrame(college_data)
df.to_excel("thanjavur_colleges.xlsx", index=False)
driver.quit()

# import pandas as pd
#
# # Load the two files
# df1 = pd.read_excel('combined_colleges.xlsx')
# duplicates = df1[df1.duplicated(subset=['Phone_Number'], keep=False)]
#
# print(f"Found {len(duplicates)} duplicate rows:")
# print(duplicates)