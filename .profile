# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

#===User-defined

# set environment vars
export JAVA_HOME=/usr/lib/jvm/java-6-openjdk-i386
export MOZILLA_FIVE_HOME=/media/sf_oc/xulrunner-1.9.2
export LD_LIBRARY_PATH=$MOZILLA_FIVE_HOME

# modify path
PATH=".:$PATH:$JAVA_HOME/bin"

