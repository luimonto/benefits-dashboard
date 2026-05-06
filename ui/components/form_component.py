class FormComponent:

    def __init__(self, page, form_selector):
        self.page = page
        self.form = page.locator(form_selector)

    def wait_until_visible(self, field_id):
        self.page.wait_for_selector(field_id, state="visible")

    def fill_input(self, field_id, value):
        value = "" if value is None else str(value)
        self.wait_until_visible(field_id)
        self.form.locator(f"{field_id}").fill(value)

    def get_input_value(self, field_id):
        return self.form.locator(f"{field_id}").input_value()

    def is_field_visible(self, field_id):
        return self.form.locator(f"{field_id}").is_visible()

    def clear_input(self, field_id):
        self.form.locator(f"{field_id}").fill("")

    def fill_form(self, data: dict):
        for field, value in data.items():
            self.fill_input(field, value)