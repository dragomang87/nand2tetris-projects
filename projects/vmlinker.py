
import vmacker

separator = vmacker.separator
bootloader = (
        f"\n// Bootloader"
        f"\n@256"
        f"\n  D = A"
        f"\n@ARG"
        f"\n M  = A"
        f"\n// frame: return"
        f"\n@return_label.bootloader.shutdown"
        f"\n  D = A"
        f"\n@257"
        f"\n M  = D"
        f"\n// frame: ARG, LCL, THIS, THAT"
        f"\n//  - they are all zero"
        f"\n//  - we simply jump SP"
        f"\n// SP and LCL"
        f"\n@262"
        f"\n  D = A"
        f"\n@SP"
        f"\n M  = D"
        f"\n@LCL"
        f"\n M  = D"
        f"\n// Call Sys.init"
        f"\n@function_label{separator}Sys.vm{separator}Sys.init"
        f"\n0; JMP"
        f"\n(return_label.bootloader.shutdown)"
        f"\n0; JMP"
        )

if __name__ == "__main__":
    # INPUTS
    import sys
    # Remove script name
    sys.argv = sys.argv[1:]
    # Check no input files or folder are given
    if len(sys.argv) == 0:
        print(
            f"\nno input file provided"
            f"\nplease give:"
            f"\n  - one input file : it will be treated as Hack Virtual Machine text file"
            f"\n                     and compiled into a .asm file"
            f"\n  - a list of files: they will be treated as Hack Virtual Machine text file,"
            f"\n                     compiled and merged with a bootloader"
            f"\n  - an input folder: all *.vm files in the folder will be compiled"
            f"\n                     and merged with a bootloader"
            f"\nAll other arguments will be ignored"
            , file=sys.stderr
            )
        sys.exit(1)

    # GET INPUT FILES
    vm_files      = [file   in sys.argv if os.path.isfile(file)]
    asm_libraries = [vmacker.vm_to_asm_filename(file) for file in vm_files]

    # GET INPUT FOLDERS
    # Remove trailing / from folders, otherwise .basename() returns ""
    vm_folders    = [folder in sys.argv if os.path.isdir (folder[:-1] if folder[-1] == "/" else folder)]
    asm_programs  = [f"{folder}/{os.path.basename(folder)}.asm" for folder in vm_folders]

    for file   in vm_files:
        asm_filename = vmacker.vm_to_asm_filename(file)
        vmacker.compile_vm_to_asm(vm_filename, asm_filename)

    for folder in vm_folders:
        # Create a list of the bootloader and libraries filenames
        asm_list = ""
        # Compile the bootloader at the beginning of the file
        asm_filename = f"{folder}/{os.path.basename(folder)}.asm"
        asm_list    += " " + asm_filename
        with open(asm_filename, 'w') as asm_file:
            asm_file.write(bootloader)
        # Compile the libraries
        for vm_library in folder vm_files ...:
            asm_library = vmacker.vm_to_asm_filename(vm_library)
            asm_list   += " " + asm_library
            compile_vm_to_asm(vm_library, asm_library)
        # Join the bootloader and libraries together
        os.system("cat {asm_list} {asm_filename}")


