read -p "Enter Your Name: "  username
echo "Welcome !"

python recording.py <<EOF
$username
EOF
python spilt.py <<EOF
$username
EOF
cd ..
python modeltraining.py

