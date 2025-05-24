import pandas as pd

class FulfillmentEngine:
    def __init__(self, filepath):
        self.data = pd.read_excel(filepath, dtype=str)
        self.data.columns = self.data.columns.str.strip()
        self.codes = set(self.data['HSNCode'].astype(str))

    def validate(self, hsn_codes):
        results = []
        for code in hsn_codes:
            code = str(code).strip()
            if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
                results.append((code, "Invalid format"))
            elif code in self.codes:
                desc = self.data[self.data['HSNCode'] == code]['Description'].values[0]
                results.append((code, f"Valid: {desc}"))
            else:
                results.append((code, "Code not found"))
        return results
