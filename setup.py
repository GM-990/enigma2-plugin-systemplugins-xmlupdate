 
from distutils.core import setup
import setup_translate


setup(name = 'enigma2-plugin-systemplugins-xmlupdate',
		version='1.0',
		author='www',
		package_dir = {'SystemPlugins.Xmlupdate': 'src'},
		packages=['SystemPlugins.Xmlupdate'],
		description = 'do update, like you want',
		cmdclass = setup_translate.cmdclass,
	)
