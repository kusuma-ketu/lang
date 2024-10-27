import re 

TOKEN_TYPES = [
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'), 
    ('MINUS', r'\-'),
    ('MULTIPLY', r'\*'),
    ('DIVIDE', r'/'), 
    ('IDENTIFIER', r'[a-zA-Z]+'),
    ('ASSIGN', r'=')
]

REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)

def lexer(input_string):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, input_string):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER': 
            tokens.append(('NUMBER', int(value)))
        elif kind == 'IDENTIFIER':
            tokens.append(('IDENTIFIER', value))
        elif kind != 'SKIP':
            tokens.append((kind, value))
        return tokens 