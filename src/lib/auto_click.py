import pyautogui
import time
import random
import threading

class AutoClick:
    def __init__(self, interval: float, random_interval: float):
        self.interval = interval
        self.random_interval = random_interval
        self._running = False
        self._thread = None

    def _click_loop(self):
        while self._running:
            wait_time = self.interval + random.uniform(0, self.random_interval)
            pyautogui.click()
            time.sleep(wait_time)

    def run(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join()