#!/bin/bash
# Today we are going to use a case statment instead of a conditional
# Have the program ask how your day is and echo out a response for good or bad
# Case statment format is a little different so please look up how this would be formated
# https://linuxize.com/post/bash-case-statement/
echo "how is your day going (good/bad)"
read mood
case $mood in

  Great | Fantastic | Wonderful)
    echo "good to hear your day is $mood"

    ;;

  Terrible | Bad | Shitty)
    echo "im sorry your day is $mood"
    ;;

  Fine | Okay | Meh)
    echo "im glad your day is $mood, hope it gets better"
    ;;

  *)
    echo  "unknown"
    ;;
esac