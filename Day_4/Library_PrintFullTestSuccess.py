
"""
Just contains a simple print statement which is intended for use at the end of test files:
"""
def Main(FullTestSuccess):
    print("\n\n\n")
    if ( FullTestSuccess ):
        print("Full Test Success")
    else:
        print("Full Test Failure")
    print("\n\n\n")   
