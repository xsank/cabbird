
def simplifyPath(path):
    names=[]
    tmp=path.strip('/').split('/')
    for i in tmp:
        if not i or i=='.':
            continue
        elif i=='..':
            if names:
                names.pop(-1)
        else:
            names.append(i)
    res='/'.join(names)
    return '/' if not res else '/'+res


if __name__=="__main__":
    print simplifyPath("/home/")
    print simplifyPath("/a/./b/../../c/")
    print simplifyPath("/../")
    print simplifyPath("/home//foo/")
    print simplifyPath("/home/foo/hello")
    print simplifyPath("/")
    print simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/")


