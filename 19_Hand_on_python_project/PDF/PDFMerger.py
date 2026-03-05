from PyPDF2 import PdfWriter

merger = PdfWriter()
pdf_1=[]

n=int(input("How Many Pdf Do You want To Merge??\n"))

for i in range(0,n):
    name=input(f"Enter The Name Of pdf:{i+1}")
    pdf_1.append(name)
    
for pdf in pdf_1:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
