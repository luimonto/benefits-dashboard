class TableComponent:

    def __init__(self, page, table_selector):
        self.page = page
        self.table = page.locator(table_selector)

    def wait_until_visible(self):
        self.table.wait_for(state="visible")

    def is_visible(self):
        return self.table.is_visible()

    def get_headers(self):
        return self.table.locator("thead th").all_inner_texts()

    def get_rows(self):
        return self.table.locator("tbody tr")

    def get_row_count(self):
        return self.get_rows().count()

    def get_cell(self, row_index, col_index):
        return self.get_rows().nth(row_index).locator("td").nth(col_index)

    def get_row_by_cell_text(self, text):
        return self.get_rows().filter(has_text=text)

    def is_empty(self):
        return "No employees found." in self.table.inner_text()

    def find_row_by_text(self, text):
        rows = self.get_rows()
        for i in range(rows.count()):
            row = rows.nth(i)
            if text in row.inner_text():
                return row
        return None

    def click_edit(self, row):
        row.locator("i.fa-edit").click()

    def click_delete(self, row):
        row.locator("i.fa-times").click()

