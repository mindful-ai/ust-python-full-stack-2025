# Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.

# Data analysis pipeline — load → process → report.

class DataProcessor:
    
    def process(self):
        self.load_data()
        self.analyze_data()
        self.report()

    def load_data(self):
        pass

    def analyze_data(self):
        pass

    def report(self):
        pass


class SalesDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading sales data...")

    def analyze_data(self):
        print("Analyzing sales trends...")

    def report(self):
        print("Generating sales report...")


processor = SalesDataProcessor()
processor.process()
