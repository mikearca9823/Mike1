#!/bin/bash
# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 
echo "How is the weather today (hot/cold/raining)"
read weather
case $weather in
hot | scorching | miserable)
    echo "make sure to bring water if it is $weather"

    ;;

    cold | Freezing)
    echo "Bundle Up if it is going to be $weather"

    ;;

    (raining)
    echo "Don't forget to bring a towel...just joking, bring an umbrella"
    ;;
 *)
    echo  "You are on your own"
    ;;
esac

