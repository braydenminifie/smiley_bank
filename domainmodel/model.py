class Student:
    def __init__(self, student_id: int, name: str, smiles: int):
        self.student_id = student_id
        self.name = name
        self.smiles = smiles

    @property
    def student_id(self):
        return self.student_id
    
    @property
    def name(self):
        return self.name
    
    @property
    def smiles(self):
        return self.smiles
    
    @student_id.setter
    def student_id(self, new_student_id: int):
        self.student_id = new_student_id

    @name.setter
    def name(self, new_name: str):
        self.name = new_name
    
    @smiles.setter
    def smiles(self, new_smiles: int):
        self.smiles = new_smiles

    
