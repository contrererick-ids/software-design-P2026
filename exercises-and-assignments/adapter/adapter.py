import re

class HTMLizable:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def to_html(self):
        return f"<article>\n  <h1>{self.titulo}</h1>\n  <p>{self.contenido}</p>\n</article>"

class Vocalizable:
    def to_ssml(self):
        pass

class HTMLToSSMLAdapter(Vocalizable):
    def __init__(self, html_obj: HTMLizable):
        self.html_obj = html_obj

    def to_ssml(self):
        html_content = self.html_obj.to_html()
        
        ssml = html_content
        ssml = re.sub(r'<h1>(.*?)</h1>', r'<emphasis level="strong">\1</emphasis>', ssml)
        ssml = re.sub(r'<p>(.*?)</p>', r'<paragraph>\1</paragraph>', ssml)
        ssml = ssml.replace("<article>", "<speak>").replace("</article>", "</speak>")
        
        ssml = re.sub('<[^<]+?>', '', ssml) if "speak" not in ssml else ssml
        
        return ssml.strip()

mi_articulo = HTMLizable("Hola Mundo", "Bienvenidos a mi tutorial de Python.")
print("--- Antes del Adaptador (HTML) ---")
print(mi_articulo.to_html())
adaptador = HTMLToSSMLAdapter(mi_articulo)
print("--- Salida del Adaptador (SSML) ---")
print(adaptador.to_ssml())