__version_info__ = {
    'major': 0,
    'minor': 0,
    'micro': 1,
    'releaselevel': 'developmental',
}


def get_version():
    vers = ['{major}.{minor}'.format(**__version_info__)]

    if __version_info__['micro']:
        vers.append('{micro}'.format(**__version_info__))
    if __version_info__['releaselevel'] != 'final':
        vers.append('{releaselevel}'.format(**__version_info__))
    return ''.join(vers)

__version__ = get_version()
