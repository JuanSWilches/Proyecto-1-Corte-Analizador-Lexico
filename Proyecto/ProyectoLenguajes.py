# Definición de tokens
tokens = [
    ('tk_integer',    '0123456789'),         # Números enteros
    ('tk_float',      '.0123456789'),        # Números flotantes
    ('tk_complex',    '0123456789jJ'),       # Números complejos
    ('tk_cadena',     '\"'),                 # Cadenas de texto
    ('id',            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'),  # Identificadores
    ('NEWLINE',       '\n'),                 # Nueva línea
    ('SKIP',          ' \t'),                # Espacios y tabs (ignorar)
    ('MISMATCH',      ''),                   # Cualquier otro carácter
]

# Palabras reservadas del núcleo de Python
palabras_reservadas = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield', 'object', 'self', 'super', 'bool', 'int', 'float', 'str',
    'print', 'input', 'type', 'list', 'dict', 'tuple', 'set', 'frozenset', 'bytearray', 'bytes', 
    'memoryview', 'len', 'range', 'enumerate', 'zip', 'filter', 'map', 'max', 'min', 'abs',
    'sum', 'round', 'sorted', 'all', 'any', 'bin', 'oct', 'hex', 'chr', 'ord', 'dir', 'help',
    'eval', 'exec', 'open', 'read', 'write', 'append', 'reversed', 'format', 'repr', 'delattr',
    'getattr', 'setattr', 'hasattr', 'issubclass', 'isinstance', 'callable', 'property',
    'staticmethod', 'classmethod', 'super', 'vars', 'globals', 'locals', 'compile', 'complex',
    'divmod', 'pow', 'id', 'hash', 'memoryview', 'iter', 'next', 'slice', 'object', 'classmethod',
    'staticmethod', 'zip', 'map', 'filter', 'print', 'input', 'len', 'type', 'isinstance',
    'issubclass', 'int', 'float', 'str', 'dict', 'list', 'set', 'frozenset', 'tuple', 'complex', 
    'bytes', 'bytearray', 'memoryview', 'open', 'help', 'dir', 'vars', 'repr', 'eval', 'exec',
    'format', 'globals', 'locals', 'super','case','match','math'

    
}

simbolos_especiales = {


    '+': 'TKN_SUMAR',
    '-': 'TKN_RESTAR',
    '*': 'TKN_MULTIPLICAR',
    '/': 'TKN_DIVIDIR',
    '%': 'TKN_MODULO',
    '^': 'TKN_POTENCIA',
    'sqrt': 'TKN_RAIZ_CUADRADA',
    'pow': 'TKN_POW',
    '<<': 'TKN_DESPLAZAMIENTO_IZQ',
    '>>': 'TKN_DESPLAZAMIENTO_DER',
    '+=': 'TKN_ASIGNAR_SUMAR',
    '-=': 'TKN_ASIGNAR_RESTAR',
    '*=': 'TKN_ASIGNAR_MULTIPLICAR',
    '/=': 'TKN_ASIGNAR_DIVIDIR',
    '%=': 'TKN_ASIGNAR_MODULO',
    '^=': 'TKN_ASIGNAR_POTENCIA',
    '&=': 'TKN_ASIGNAR_AND',
    '|=': 'TKN_ASIGNAR_OR',
    '<<=': 'TKN_ASIGNAR_DESPLAZAMIENTO_IZQ',
    '>>=': 'TKN_ASIGNAR_DESPLAZAMIENTO_DER',
    '=': 'TKN_ASIGNAR',
    ';': 'TKN_PUNTO_Y_COMA',
    '.': 'TKN_PUNTO',
    ',': 'TKN_COMA',
    ':': 'TKN_DOSPUNTOS',
    '==': 'TKN_IGUAL',
    '!=': 'TKN_NO_IGUAL',
    '<': 'TKN_MENOR_QUE',
    '>': 'TKN_MAYOR_QUE',
    '<=': 'TKN_MENOR_O_IGUAL',
    '>=': 'TKN_MAYOR_O_IGUAL',
    '(': 'TKN_PAR_IZQ',
    ')': 'TKN_PAR_DER',
    '[': 'TKN_CORCHETE_IZQ',
    ']': 'TKN_CORCHETE_DER',
    '{': 'TKN_LLAVE_IZQ',
    '}': 'TKN_LLAVE_DER',
    '->': 'TKN_FLECHA',
    '...': 'TKN_ELIPSIS',
    '\"': 'TKN_COMILLAS_DOBLES',
    '\'': 'TKN_COMILLA_SIMPLE',
    '¿': 'TKN_INTERROGACION_IZQ',
    '?': 'TKN_INTERROGACION_DER',
    '#': 'TKN_NUMERAL',
    '!': 'TKN_EXCLAMACION_DER',
    '¡': 'TKN_EXCLAMACION_IZQ',
    '&': 'TKN_AMPERSAND',
    '|': 'TKN_PIPE',
    '~': 'TKN_TILDE',
    '`': 'TKN_ACENTO_GRAVE',
    '@': 'TKN_ARROBA',
    '$': 'TKN_DOLAR',
    '%': 'TKN_PORCENTAJE',
    '°': 'TKN_GRADO',
    '^': 'TKN_CARET',
    'bool': 'TKN_BOOL',  # Añadido para completar según instrucciones
    '**': 'TKN_OP_POTENCIA',
    '//': 'TKN_DIVISION_ENTERA',

}

def obtener_tipo_token(token):
    if token in palabras_reservadas:
        return 'PALABRA_CLAVE'
    elif token.replace('.', '', 1).isdigit() and '.' in token and token.count('.') == 1:
        return 'FLOTANTE'
    elif 'j' in token.lower() and any(char.isdigit() for char in token):
        return 'COMPLEJO'
    elif token.isdigit():
        return 'ENTERO'
    elif token.startswith('\"') and token.endswith('\"'):
        return 'STRING'
    elif token[0].isdigit():
        return 'MISMATCH'
    else:
        return 'ID'

def analizador_lexico(texto_entrada):
    lista_tokens = []  # Lista para almacenar los tokens generados
    lineas = texto_entrada.split('\n')  # Divide el texto en líneas
    fila = 1  # Inicializa el número de la fila
    for linea in lineas:
        columna = 1  # Inicializa la columna en la línea actual
        palabra = ''  # Variable para acumular caracteres de un token
        posicion_comentario = linea.find('#')  # Busca la posición del símbolo de comentario

        if posicion_comentario != -1:  # Se encontró el símbolo de comentario
            linea = linea[:posicion_comentario]  # Ignora todo después del símbolo de comentario

        while columna <= len(linea):  # Procesa cada carácter en la línea
            caracter = linea[columna - 1]  # Obtiene el carácter actual

            if caracter == '\"':  # Inicio de una cadena
                if palabra:  # Si había una palabra acumulada antes de la comilla, procesarla.
                    lista_tokens.append((obtener_tipo_token(palabra), palabra, fila, columna - len(palabra)))
                    palabra = ''  # Reinicia la palabra

                inicio = columna  # Guarda la posición de inicio de la cadena
                columna += 1  # Salta la comilla inicial
                while columna <= len(linea) and linea[columna - 1] != '\"':  # Acumula caracteres hasta la comilla final
                    palabra += linea[columna - 1]
                    columna += 1
                lista_tokens.append(('STRING', palabra, fila, inicio))  # Añade la cadena como token
                palabra = ''  # Reinicia la palabra para el siguiente token
                columna += 1  # Salta la comilla final

            if columna != len(linea) and caracter == '.' and linea[columna].isalnum() and palabra.isalpha():
                # Procesa la palabra antes del punto
                if palabra:
                    lista_tokens.append((obtener_tipo_token(palabra), palabra, fila, columna - len(palabra)))
                    palabra = ''

                # Procesa el punto
                lista_tokens.append((simbolos_especiales[caracter], caracter, fila, columna))

            elif caracter in tokens[4][1] or caracter.isdigit() or caracter in '.jJ':
                palabra += caracter
                if columna == len(linea) or not (linea[columna].isdigit() or linea[columna] in '.jJ' or linea[columna].isalpha()):
                    # Determina el tipo de token basado en la palabra acumulada
                    if '.' in palabra and palabra.replace('.', '', 1).isdigit() and palabra.count('.') > 1:
                        for c in palabra:
                            lista_tokens.append(('MISMATCH', c, fila, columna - len(palabra) + 1))
                            palabra = ''  # La palabra se reinicia después de procesarla
                    else:
                        tipo_token = obtener_tipo_token(palabra)
                        # Añade el número o identificador completo como un solo token
                        lista_tokens.append((tipo_token, palabra, fila, columna - len(palabra) + 1))
                        palabra = ''  # Reinicia la palabra para el siguiente token

            else:
                if palabra:
                    # Si había una palabra acumulada antes de encontrar un carácter no palabra, procesarla.
                    lista_tokens.append((obtener_tipo_token(palabra), palabra, fila, columna - len(palabra)))
                    palabra = ''
                if caracter in simbolos_especiales:
                    # Procesa directamente los símbolos especiales individuales
                    lista_tokens.append((simbolos_especiales[caracter], caracter, fila, columna))
                elif caracter not in ' \t':
                    # Maneja caracteres no reconocidos
                    pass  # Aquí se puede agregar el manejo de errores para caracteres no reconocidos

            columna += 1  # Avanza a la siguiente columna

        fila += 1  # Pasa a la siguiente fila

    return lista_tokens


# Implementación de la lectura de archivos .txt
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        texto_entrada = archivo.read()
    return texto_entrada

<<<<<<< HEAD
nombre_archivo = 'texto.txt'  # El nombre del archivo a leer
=======
nombre_archivo = 'texto3.txt'  # El nombre del archivo a leer
>>>>>>> 960f7aeb2a34ee3f26920928ad91f9d5a13643b8
texto_entrada = leer_archivo(nombre_archivo)

tokens = analizador_lexico(texto_entrada)

def corrector(tokens):
    error_encontrado = False
    for token in tokens:
        if token[0] == 'PALABRA_CLAVE':
            print("<{}, {}, {}>".format(token[1], token[2], token[3]))
        elif token[1] in simbolos_especiales:
            print("<{}, {}, {}>".format(token[0], token[2], token[3]))
        elif token[0] == 'MISMATCH':
            print("Error léxico: <{}, {}, {}>".format(token[1], token[2], token[3]))
            error_encontrado = True
            break
        else:
            print("<{}, {}, {}, {}>".format(token[0], token[1], token[2], token[3]))

    if error_encontrado:
        return

corrector(tokens)

