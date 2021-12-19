import PyPDF2

with open('dummy.pdf', 'rb') as file:  # read binary
    # print(file)
    reader = PyPDF2.PdfFileReader(file)
    writer = PyPDF2.PdfFileWriter()
    print(reader.numPages)
    # print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

