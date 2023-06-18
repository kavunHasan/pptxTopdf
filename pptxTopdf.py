import aspose.slides as slides
slidesCount = int(input("how many slides are there"))


for i in range(1,slidesCount+1):
    slideName = "ch" + str(i)      
    slide = slides.Presentation(slideName + ".pptx")
    slide.save(slideName + ".pdf", slides.export.SaveFormat.PDF)

