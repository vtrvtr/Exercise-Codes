from string import maketrans






def splitOriginLinks(originLink):
	b = originLink.split(':')
	splitted = []
	for s in b:
		splitted.append(s.split('/'))
	return splitted[0], splitted[1]


def splitDestLinks(destLink):
	l = destLink.split('/')
	return l


def joinTwoPaths(origin, dest):
	pathO1, pathO2 = splitOriginLinks(origin)
	pathD = splitDestLinks(dest)
	joined = []
	print 'origin', origin
	print 'patho1', pathO1
	for path in pathD:
		# print 'joined:', joined
		# print 'path01:', pathO1
		if joined == pathO1:
			# print 'here'
			joined = pathO2	
		joined.append(path)
	return '/'.join(joined)

a = ['/bin:/usr/bin',
         '/usr/bin:/usr/local/bin/',
         '/usr/local/bin/log:/var/log-2014',
         '/bin/log/rc']
b = joinTwoPaths(a[0], a[-1])
c = joinTwoPaths(a[1], b)
d = joinTwoPaths(a[2], c)
print d

print splitOriginLinks(a[2])