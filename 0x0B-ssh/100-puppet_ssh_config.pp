# Configures SSH for no password and specifying IdentityFile

$line_string = "Host 3.85.54.241\n\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no"

file {"/home/vagrant/.ssh/config":
    ensure => file,
    content => $line_string
}
