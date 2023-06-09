from selenium import webdriver


def switch_to_cur_handle(driver):
    all_handles = driver.window_handles()
    current_handle = driver.current_window_handle()
    for handle in all_handles:
        if handle != current_handle:
            _handle = handle
            driver.switch_to.window(_handle)