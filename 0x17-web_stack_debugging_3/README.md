# Debugging is fun only when you know how to do it

First find the pid of the apache2 process
```bash
ps aux
```

use that <pid> in the following command
```bash
strace -p <pid> -o output.txt
```

This will run run strace of that program, and save the ouput to output.txt file in the current working directory.

Then, by inspecting it, from the bottom, you notice a file having the wrong extension.
And since this is found in the php settings file... just correct it and you are good to go.
