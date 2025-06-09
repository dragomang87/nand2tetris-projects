
import vmacker

separator = vmacker.separator
bootloader = (
        f"\n// Bootloader"
        f"\n// Sys.init ARG = bootloader SP = 256"
        f"\n// Sys.init has 0 arguments and ARG WILL BE EMPTY!! not like other functions"
        f"\n// Sys.init return: at 256"
        f"\n@return_label.bootloader.shutdown"
        f"\n  D = A"
        f"\n@256"
        f"\n M  = D"
        f"\n// Bootloader frame: LCL, ARG, THIS, THAT"
        f"\n//  - CANNOT assume that they are zero"
        f"\n@LCL"
        f"\n  D = M"
        f"\n@257"
        f"\n M  = D"
        f"\n@ARG"
        f"\n  D = M"
        f"\n@258"
        f"\n M  = D"
        f"\n@THIS"
        f"\n  D = M"
        f"\n@259"
        f"\n M  = D"
        f"\n@THAT"
        f"\n  D = M"
        f"\n@260"
        f"\n M  = D"
        f"\n// Sys.init frame:"
        f"\n//  - LCL = SP = 261"
        f"\n//  - ARG = 256"
        f"\n@261"
        f"\n  D = A"
        f"\n@SP"
        f"\n M  = D"
        f"\n@LCL"
        f"\n M  = D"
        f"\n@256"
        f"\n  D = A"
        f"\n@ARG"
        f"\n M  = D"
        f"\n// Call Sys.init"
        f"\n@function_define_label{separator}Sys.init"
        f"\n0; JMP"
        f"\n// Sys.init return label"
        f"\n(return_label.bootloader.shutdown)"
        f"\n// Bootloader loop forever"
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
            f"\nplease give one or more files or folders:"
            f"\n  - all files and all *.vm files in each folder"
            f"\n    will be treated as Hack Virtual Machine text files"
            f"\n    and compiled into *.asm files"
            f"\n  - if <folder>/<folder>.vm does not exist in the folder"
            f"\n    all compiled *.asm files will be merged"
            f"\n    into <folder>/<folder>.vm with a bootloader"
            f"\nAll other arguments will be ignored"
            , file=sys.stderr
            )
        sys.exit(1)

    import os

    # GET INPUT FILES
    vm_files     = [arg for arg in sys.argv if os.path.isfile(arg)]

    # GET INPUT FOLDERS
    vm_folders   = [arg for arg in sys.argv if os.path.isdir (arg)]
    # Remove trailing / from folders, otherwise .basename() returns ""
    clean_folder = lambda folder: folder[:-1] if folder[-1] == "/" else folder
    vm_folders   = [clean_folder(folder) for folder in vm_folders]
    print(vm_files, vm_folders)

    # COMPILE INPUT FILES
    for file   in vm_files:
        # Reset compiler
        vmacker.reset_compiler_variables()
        # Compile
        vmacker.compile_vm_to_asm(vm_filename)

    # COMPILE INPUT FOLDERS
    for folder in vm_folders:
        # Reset compiler
        vmacker.reset_compiler_variables()
        # Create a variable for the list of the generated *.asm files
        asm_files = ""
        # Find all .vm files in folder
        import glob
        vm_files = glob.glob(f"{folder}/*.vm")
        # Compile all files
        # (the compiler function returns the output filename)
        for vm_file in vm_files:
            asm_files += " " + vmacker.compile_vm_to_asm(vm_file)
        print(vmacker.ASM['functions'])
        print(vmacker.ASM['calls'])
        # If "folder/folder.vm" is missing
        # create bootable "folder/folder.vm"
        vm_program =  f"{folder}/{os.path.basename(folder)}.vm"
        if vm_program not in vm_files:
            # The bootloader will not work if
            #   - file Sys.vm is missing
            #   - Sys.vm does not have a Sys.init function
            # thus warn if Sys.vm is missing
            if f"{folder}/Sys.vm" not in vm_files:
                import warnings
                warnings.warn(
                        f"{folder}/Sys.vm MISSING: "
                        f"assembly program will likely fail")
            # Create the .asm program file
            asm_program = f"{folder}/{os.path.basename(folder)}.asm"
            # Compile the bootloader into the program file
            with open(asm_program, 'w') as asm_file:
                asm_file.write(bootloader)
            # Add Sys.init to the called functions
            vmacker.filename_label = vmacker.ASM['filename_label'](f"{folder}/Sys.vm")
            vmacker.ASM['calls'][vmacker.function_label("Sys.init")] = True
            # Join the bootloader and libraries together
            os.system(f"cat {asm_files} >> {asm_program}")
        # Final Warnings
        vmacker.warn_undefined_functions()
        vmacker.warn_undefined_labels()


