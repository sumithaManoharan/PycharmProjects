from datetime import datetime
from datetime import time as t
from selenium import webdriver
import os,time
from selenium.webdriver.common.by import By
import argparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class GymBooking:
    def __init__(self):
        self.args = {}
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.user_data_dir = os.path.abspath(os.path.join(os.getcwd(), "chrome_profile"))
        self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.classes_booked = 0
        self.waitlist_joined = 0
        self.already_booked = 0
        self.already_waitlisted = 0
        self.total_tue_6pm_classes = 0
        self.retries = 0

    # def retry_login(self,reties = 7):


    def login(self):
        # try:
        self.driver.find_element(By.CSS_SELECTOR, "button.Home_heroButton__3eeI3").click()
        self.driver.find_element(By.CSS_SELECTOR, "input#email-input").send_keys("sumitha@test.com")
        self.driver.find_element(By.CSS_SELECTOR, "input#password-input").send_keys("sumitha123")
        self.driver.find_element(By.CSS_SELECTOR, "button#submit-button").click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/gym"))
        print("Login successful! Redirected to:", self.driver.current_url)

        self.book_classes()

    def booking_track(self,button,cls, dt_object):
        if button.is_enabled():
            button.click()
            if cls.get_attribute("data-is-fully-booked") == "true":
                print(f"Waitlisted for {cls.get_attribute('data-class-type')} class: on {dt_object.date().strftime("%A, %B %d")}")
                self.waitlist_joined += 1
                return f"[New waitlisted] {cls.get_attribute('data-class-type')} class on {dt_object.date().strftime("%A, %B %d")}"
            else:
                print(f"Booked {cls.get_attribute('data-class-type')} class: Booking successful! date:{dt_object.date().strftime("%A, %B %d")}")
                self.classes_booked += 1
                return f"[New Booked] {cls.get_attribute('data-class-type')} class on {dt_object.date().strftime("%A, %B %d")}"

    def display_summary(self,new_booking):
        # Create the detailed list string first
        detailed_list = "\n".join(new_booking) if new_booking else "No new bookings made."

        print(f"""
        ------------ SUMMARY ------------
        Previous Bookings:
        - Already Booked:     {self.already_booked}
        - Already Waitlisted: {self.already_waitlisted}

        New Bookings:
        - Classes Booked:     {self.classes_booked}
        - Waitlist Joined:    {self.waitlist_joined}

        Total Tue/Thur 6pm processed: {self.total_tue_6pm_classes}

        ----------- DETAILED LIST -----------
        {detailed_list}
        -------------------------------------
        """)

    def verify_result(self):
        self.driver.find_element(By.CSS_SELECTOR,"a#my-bookings-link").click()
        time.sleep(8)
        confirmed = self.driver.find_elements(By.CSS_SELECTOR,'div[data-booking-status="confirmed"]')
        waitlist = self.driver.find_elements(By.CSS_SELECTOR,'div[data-booking-status="waitlisted"]')
        if len(confirmed) == self.already_booked + self.classes_booked and len(waitlist) == self.waitlist_joined+self.already_waitlisted and len(confirmed) + len(waitlist) == self.total_tue_6pm_classes:
            print("Verified!")
        else: print("There is a count mismatch!")

    def book_classes(self):
        # print("Booking Classes")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div.ClassCard_card__KpCx5")))
        class_list = self.driver.find_elements(By.CSS_SELECTOR, "div[class*=ClassCard_card__KpCx5]")
        new_booking = []
        for cls in class_list:
            button = cls.find_element(By.CSS_SELECTOR, "div.ClassCard_cardActions__tVZBm button")
            if button.text.strip() == "Waitlisted":
                self.already_waitlisted += 1
                self.total_tue_6pm_classes += 1
            elif button.text.strip() == "Booked":
                self.already_booked += 1
                self.total_tue_6pm_classes += 1

            text = cls.get_attribute("id").split("-")
            date = f"{text[3]}-{text[4]}-{text[5]} {text[6]}"
            dt_object = datetime.strptime(date, "%Y-%m-%d %H%M")

            if (dt_object.weekday() == 1 or dt_object.weekday() == 3) and dt_object.time() == t(18,0):
                if button.text.strip() not in ["Booked", "Waitlisted"]:
                    self.total_tue_6pm_classes += 1
                    text = self.booking_track(button, cls, dt_object)
                    new_booking.append(text)
        self.verify_result()
        self.display_summary(new_booking)

    def main(self, args):
        self.args = args
        retry = True

        while retry and self.retries < 7:
            try:
                # Re-open browser if it was closed in a previous failed attempt
                if self.driver is None:
                    self.__init__()

                self.driver.get("https://appbrewery.github.io/gym/")
                time.sleep(5)
                self.login()
                retry = False  # If login and booking finish, stop the loop

            except Exception as e:
                self.retries += 1
                print(f"Attempt {self.retries} failed: {e}")
                self.driver.quit()
                self.driver = None  # Mark driver as gone
                self.retries += 1
                time.sleep(2)  # Short pause before trying again

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gym Booking Web Developer Project")
    # parser.add_argument("-d", "--booking_days", help="Gym Booking days",type=str,seperator=",",choices=("mon","tue","wed","thur","fri","sat","sun"))
    # parser.add_argument("-t", "--booking_time", help="Gym Booking time")
    args = parser.parse_args()
    gym_obj = GymBooking()
    gym_obj.main(args)
