__author__ = 'Xsank'

SINGLE_NODE=[
    'br','hr','col','input','area','img','meta','link',
    'frame','param','wbr','base','basefont',
]


def render(tag):
    '''Render the diffrent html tags
    '''
    if tag=='div':
        return ''
    elif tag=='nav':
        return ''
    elif tag=='ul':
        return 'o'
    elif tag=='li':
        return 'o'
    elif tag=='a':
        return 'link:'
    elif tag=='h1':
        return 'h1 font:'
    elif tag=='h2':
        return 'h2 font:'
    elif tag=='h3':
        return 'h3 font:'
    elif tag=='p':
        return 'normal font:'
    elif tag=='img':
        return 'image'
    elif tag=='br':
        return '-'*80
    elif tag=='hr':
        return '\n'
    else:
        return ''