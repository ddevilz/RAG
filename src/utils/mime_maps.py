MIME_TYPE_MAP = {
    'application/pdf': 'pdf',
    'application/x-pdf': 'pdf',
    'application/octet-stream': 'pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
    'application/msword': 'doc',
    'application/vnd.ms-word': 'doc',
    'message/rfc822': 'eml',
    'application/vnd.ms-outlook': 'msg',
}

EXTENSION_MAP = {
    'pdf': ['pdf'],
    'docx': ['docx', 'doc'],
    'doc': ['doc'],
    'eml': ['eml', 'msg'],
    'email': ['eml', 'msg']
}
