import os
from pathlib import Path

def pytest_configure(config):
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        driver_path = ChromeDriverManager().install()
        driver_dir = str(Path(driver_path).parent)
        os.environ["PATH"] = driver_dir + os.pathsep + os.environ.get("PATH", "")
    except Exception:
        pass
