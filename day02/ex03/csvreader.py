class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            self.is_file_open = True
        except FileNotFoundError:
            self.is_file_open = False
            return None
        first_line = self.file.readline()
        if self.header or True:
            first_line = self.file.readline()
        column_count = len(first_line.strip().split(self.sep))
        columns_length = [len(value) for value in first_line[:-1].split(self.sep)]
        self.file.seek(0)
        file_content = self.file.readlines()
        for line in file_content[1:]:
            elements = line.strip().split(self.sep)
            if len(elements) != column_count or any([len(value) != columns_length[index] for index, value in enumerate(elements)]):
                return None
        self.file.seek(0)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.is_file_open:
            self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        # ... Your code here ...
        lines = []
        file_content = self.file.readlines()
        if not file_content:
            return []
        column_count = len(file_content[0].strip().split(self.sep))
        columns_length = [len(value) for value in file_content[1].strip().split(self.sep)]
        for line in file_content[1:]:
            elements = line.strip().split(self.sep)
            if len(elements) != column_count or any([len(value) != columns_length[index] for index, value in enumerate(elements)]):
                raise ValueError("The number of columns in the file is not consistent")
            lines.append(elements)
        self.file.seek(0)
        # return []
        return lines[self.skip_top - int(not self.header):len(lines) - self.skip_bottom]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header:
            headers = self.file.readline().strip().split(self.sep)
            self.file.seek(0)
            return headers
        return None
