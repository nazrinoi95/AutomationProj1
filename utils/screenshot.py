import os
from datetime import datetime

def take_screenshot(driver,test_name):
   """Takes a screenshot and save it in the screenshots folder"""
   folder = "screenshots"
   if not os.path.exists(folder):
      os.makedirs(folder)
   timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
   filename = f"{folder}/{test_name}_{timestamp}.png"
   driver.save_screenshot(filename)
   print(f"Screenshot saved: {filename}")
   return filename