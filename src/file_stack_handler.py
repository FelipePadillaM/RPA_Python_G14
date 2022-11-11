from src.file_service import FileService
from src.stack_service import StackService
from src.utils.lifo import Stack

stack = Stack()
file_service = FileService()
stack_service = StackService(stack)

def get_files():
    
    txt_files = file_service.get_only_txt_files()
    return txt_files

def add_files_to_stack():
    
    txt_files = file_service.get_only_txt_files()

    for filename in txt_files:
        name = filename
        size = file_service.get_size_from_filename(filename)
        path = file_service.get_standard_path()

        file = file_service.create_file(name, size, path)
        stack_service.stack.push(file)

def sort_stack():
    stack_service.stack.sort_stack()
    return stack_service.stack.items()