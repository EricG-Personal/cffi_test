from cffi_test._sample_lib import ffi, lib



def a_python_function( a ):
    lib.a_sample_function( a )



def main():
    a_python_function( 42 )



if __name__ == "__main__":
    main()

