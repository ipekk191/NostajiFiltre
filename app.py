import cv2 as cv 
import numpy as np 
import gradio as gr

def nostaji(image):
    image=np.array(image)
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    return gray_image

#Gradio ara yüzünü oluştur
with gr.Blocks() as demo:
    gr.Markdown("# Görseli Siyah Beyaza çevir!")
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrisin!!")

    image_input=gr.Image(type='pil',label="Görsel: ")
    image_output=gr.Image(type='numpy',label="Sonuç Görseli: ")

    #Fonksiyonu gradio bileşenlerine bağlayalım 
    btn=gr.Button("Çevir") 
    btn.click(fn=nostaji,inputs=image_input, outputs=image_output)

#Gradio arayüzünü başlat
if __name__=="__main__":
    demo.launch()# ()içine  share=True ile arayüzü paylaşabilirsiniz