import threading
import time
import random
import pyautogui

class AutoClick:
    def __init__(self):
        self._start = False
        self._thread = None

    def _click_loop(self, interval, random_interval):
        while self._start:
            start_time = time.time()
            wait_time = interval + random.uniform(0, random_interval)
            while self._start and time.time() - start_time < wait_time:
                time.sleep(0.05)  # Pequeño delay para verificar constantemente si se detiene

            if self._start:
                pyautogui.click()

    def run(self, interval: float, random_interval: float):
        if not self._start:
            self._start = True
            self._thread = threading.Thread(target=self._click_loop, args=(interval, random_interval), daemon=True)
            self._thread.start()

    def stop(self):
        self._start = False
        if self._thread:
            self._thread.join(timeout=0.1)  # Pequeño timeout para no bloquear
