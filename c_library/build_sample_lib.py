from cffi import FFI

INCLUDE_DIRS = [ 'c_library' ]
SOURCES = [ 'c_library/sample_lib.c' ]
HEADER = """
    #include "sample_lib.h"
"""

ffibuilder = FFI()

ffibuilder.set_source( "_sample_lib", HEADER, include_dirs = INCLUDE_DIRS, sources = SOURCES, libraries = [] )

ffibuilder.cdef( """
    void a_sample_function( int a );
""" )

ffibuilder.compile( verbose = True )

