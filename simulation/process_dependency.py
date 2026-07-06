class ProcessDependency:

    def __init__(self, process_name, depends_on=None):
        self.process_name = process_name
        self.depends_on = depends_on or []
