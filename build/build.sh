# Prepare
inputfile="my_cv_repo/docs/NguyenKiemHung_CV.docx"
file="NguyenKiemHung_CV.pdf"
if [ -f "$file" ] ; then
    rm "$file"
fi
killall ngrok
killall python

# Getting stuff
echo "Setting up..."
sh -c "python -m http.server 8000" & echo "Running HTTP Server"
sh -c "./ngrok http 8000" & echo "Running Ngrok"
echo "Waiting for 5 seconds." && sleep 5
echo "\nFinished setting up!\n"
echo "Getting PDF file."
python build/get_via_htmltopdf.py
#python docs/convert_docx2pdf.py

# abiword --to=pdf $inputfile

libreoffice --headless --covert-to pdf $inputfile

# Clean up
killall python
killall ngrok
echo "Killed ngrok & python processes."