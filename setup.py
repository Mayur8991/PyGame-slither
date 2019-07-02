import cx_Freeze 

executables = [cx_Freeze.Executable("mygame.py")] 
cx_Freeze.setup( 
        name = "Slither", 
        options = {"build_exe": {"packages":["pygame"],"include_files":["apple.png","snake.png"]}},
        description = "Slither game tutorial", 
          executables = executables
        )
