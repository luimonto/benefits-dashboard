class ModalComponent:

    def __init__(self, page, modal_selector):
        self.page = page
        self.modal = page.locator(modal_selector)

    def wait_until_visible(self):
        self.modal.wait_for(state="visible")

    def is_visible(self):
        return self.modal.is_visible()

    def close(self):
        self.modal.locator("button.close").click()

    def click_cancel(self):
        self.modal.locator("text=Cancel").click()
