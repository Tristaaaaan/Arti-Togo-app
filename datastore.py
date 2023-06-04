import json


class DataStore:
    def __init__(self):
        self.data_file = self.open_file()

    def open_file(self):
        # Read the JSON config file
        with open('data_cfg.json', 'r') as file:
            config = json.load(file)

        return config

    def get_data_step1(self):

        BCrk = self.data_file['Step1']['BCrk']
        Frk = self.data_file['Step1']['Frk']

        return BCrk, Frk

    def update_data_step1(self, BCrk, Frk):
        # Update the data settings with custom values
        self.data_file['Step1']['BCrk'] = BCrk
        self.data_file['Step1']['Frk'] = Frk

        # Write the updated JSON config file
        with open('data_cfg.json', 'w') as file:
            json.dump(self.data_file, file, indent=4)

        return

    def update_data_step2(self, Frc1, BCrc1, Fx1, BCx1):
        # Update the data settings with custom values
        self.data_file['Step2']['Frc1'] = Frc1
        self.data_file['Step2']['BCrc1'] = BCrc1
        self.data_file['Step2']['Fx1'] = Fx1
        self.data_file['Step2']['BCx1'] = BCx1

        # Write the updated JSON config file
        with open('data_cfg.json', 'w') as file:
            json.dump(self.data_file, file, indent=4)

        return

    def reset(self):
        self.data_file['Step1']['BCrk'] = 0
        self.data_file['Step1']['Frk'] = 0

        self.data_file['Step2']['Frc1'] = 0
        self.data_file['Step2']['BCrc1'] = 0
        self.data_file['Step2']['Fx1'] = 0
        self.data_file['Step2']['BCx1'] = 0

        # Write the updated JSON config file
        with open('data_cfg.json', 'w') as file:
            json.dump(self.data_file, file, indent=4)

        return
