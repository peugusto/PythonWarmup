def valitador(file):
    
    format_file = file.split('.')
    formats_allowed = ['png','jpg','pdf']

    isAllowed = format_file[1] in formats_allowed

    print(isAllowed)

if __name__ == "__main__":
    valitador("formato.texto") #false
    valitador("file.pdf") #true

    