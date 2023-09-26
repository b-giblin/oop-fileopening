# Brian Giblin
# Filemanager
# 9/23/2023


import os

class FileChecker:
  def __init__(self, path):
    self.path = path

  def is_file(self):
    return os.path.isfile(self.path)
  
  def check_file(self):
    if self.is_file():
      print(f"{self.path} is a file")
    else:
      print(f"{self.path} is not a file")


class Filemanager:
  def __init__(self, filename): 
    self.filename = filename
    self.file_checker = FileChecker(self.filename)
  

  def create_sample_file(self):
    with open(self.filename, 'w') as f: # 'w' for write
      f.write('Hello World')

  def open_in_read_mode(self):
    with open(self.filename, 'r') as f: # 'r' for read
      content = f.read()
      print(f"Content in read mode: {content}")
  

  def open_in_write_mode(self):
    with open(self.filename, 'w') as f: # 'w' for write
      f.write('Overwritten Content')


  def open_in_append_mode(self): 
    with open(self.filename, 'a') as f: # 'a' for append
      f.write('\nAppended Content')

  def open_in_readwrite_mode(self):
      with open(self.filename, 'r+') as file:
          content_before = file.read()
          file.write('\nAdditional content in read-write mode')
          file.seek(0)
          content_after = file.read()
      print("Content before writing in read-write mode:", content_before)
      print("Content after writing in read-write mode:", content_after)

  def demonstrate_file_modes(self):
    self.file_checker.check_file() # check if file exists
    self.create_sample_file() # create sample file
    self.open_in_read_mode() # open file in read mode
    self.open_in_write_mode() # open file in write mode
    self.open_in_append_mode() # open file in append mode
    self.open_in_readwrite_mode() # open file in read-write mode


if __name__ == "__main__":
  f = Filemanager('sample.txt')
  f.demonstrate_file_modes()


