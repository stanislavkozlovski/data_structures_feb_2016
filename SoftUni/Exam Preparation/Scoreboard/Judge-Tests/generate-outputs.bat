FOR %%f in ("*.in.txt") DO (
	SETLOCAL EnableDelayedExpansion
    SET "file=%%f"
    ..\Scoreboard.Solution\bin\debug\Scoreboard.Solution.exe < "%%f" > "!file:.in.txt=.out.txt!"
)
