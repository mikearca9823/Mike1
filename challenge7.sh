echo "pick a file or folder"
ls 
read file
echo "pick the file permission example 775"
read number
chmod $number $file
echo "granted permission to $file"
ls -l $file 