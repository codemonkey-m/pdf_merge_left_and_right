from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2.generic import RectangleObject

a = PdfReader('1.pdf')
b = PdfReader('2.pdf')

file_merger = PdfWriter()
for page in range(len(a.pages)):
    p1 = a.pages[page]
    p2 = b.pages[page]

    width = p1.cropbox.width
    op = Transformation().translate(tx=width, ty=0)
    p2.add_transformation(op)
    cb = p2.cropbox
    p2.mediabox = RectangleObject((cb.left+width, cb.bottom, cb.right+width, cb.top))
    p2.cropbox = RectangleObject((cb.left+width, cb.bottom, cb.right+width, cb.top))
    p1.merge_page(p2, expand=True)
    mb = p1.mediabox
    p1.mediabox = RectangleObject((mb.left, mb.bottom, mb.right + cb.left, mb.top))
    p1.cropbox = RectangleObject((mb.left, mb.bottom, mb.right + cb.left, mb.top))

    file_merger.add_page(p1)

file_merger.write("./merge.pdf")
