# Prepare
file="LeThienTrung_CV.pdf"
if [ -f "$file" ] ; then
    rm "$file"
fi
killall ngrok
killall python

# Getting stuff
echo "Setting up..."
sh -c "python -m http.server 80" & echo "Done HTTP Server"
sh -c "ngrok http 80" & echo "Done Ngrok"
sleep 5
echo "\nFinished setting up!\n"
echo "Getting PDF file."
python get_pdf.py

# Clean up
killall python
killall ngrok