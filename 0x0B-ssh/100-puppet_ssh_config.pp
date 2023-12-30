# Configures SSH for no password and specifying IdentityFile

$line_string = "Host 3.85.54.241\n\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no"

file {"./2-ssh_config":
    path => "/etc/2-ssh_config",
    content => $line_string
}
